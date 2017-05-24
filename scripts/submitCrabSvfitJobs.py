#!/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import datetime
from httplib import HTTPException
from multiprocessing import Process
import os
import re
import shutil
import shlex
import string

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
import CRABClient.UserUtilities
from CRABClient.UserUtilities import getUsernameFromSiteDB

import Artus.Utility.tools as tools


def build_configs(args):
	base_path, sample = args[0], args[1]

	today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
	max_n_files_per_task = 8000
	filename_replacements = {
		"srm://grid-srm.physik.rwth-aachen.de:8443/srm/managerv2?SFN=/pnfs/physik.rwth-aachen.de/cms/store/user/" : "root://grid-vo-cms.physik.rwth-aachen.de:1094//store/user/"
	}
	
	configs = []
	jobfiles = []
	
	stdout, stderr = tools.subprocessCall(shlex.split("gfal-ls " + os.path.join(base_path, sample)))
	filenames = [filename for filename in stdout.decode().strip().split("\n") if (("SvfitCache" in filename) and filename.endswith(".root"))]
	if len(filenames) > 0:
		filenames = [os.path.join(base_path, sample, filename) for filename in filenames]
		pipelines_filenames = {}
		for filename in filenames:
			for src, dst in filename_replacements.iteritems():
				filename = filename.replace(src, dst)
			pipeline = re.search("SvfitCache(?P<pipeline>.*)\d+.root", filename).groupdict()["pipeline"]
			pipelines_filenames.setdefault(pipeline, []).append(filename)
		
		for pipeline, filenames in pipelines_filenames.iteritems():
			filenames_chunks = [filenames[index:index+max_n_files_per_task] for index in xrange(0, len(filenames), max_n_files_per_task)]
			for index, filenames_chunk in enumerate(filenames_chunks):
				
				# create job scripts
				jobfiles.append(str("svfit_%s_%s_%s_%d.sh" % (today, sample, pipeline, index)))
				with open(jobfiles[-1], "w+") as jobfile:
					jobfile.write(read_file(os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/templates/crab_userjob_prefix.sh")))
					
					svfit_code = string.Template(read_file(os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/templates/crab_svfit.sh")))
					jobfile.write(svfit_code.safe_substitute(
							input_files = "\n".join("arr[%d,0]=%s" % (i+1, f) for i, f in enumerate(filenames_chunk)),
							cwd=os.getcwd()
					))
					
					jobfile.close()
				
				# crab configuration
				configs.append(CRABClient.UserUtilities.config())
				configs[-1].General.workArea = os.path.abspath(os.path.expandvars("$ARTUS_WORK_BASE/../svfit_caches/%s/" % (today)))
				configs[-1].General.transferOutputs = True
				configs[-1].General.transferLogs = True
				configs[-1].General.requestName = ("%s_%s_%d" % (sample, pipeline, index))[:100]
				log.debug("Job name: " + configs[-1].General.requestName)
				configs[-1].Data.outputPrimaryDataset = "Svfit"
				configs[-1].Data.splitting = "EventBased"
				configs[-1].Data.unitsPerJob = 1
				configs[-1].Data.totalUnits = len(filenames_chunk)
				configs[-1].Data.publication = False
				configs[-1].Data.outputDatasetTag = configs[-1].General.requestName
				configs[-1].Data.outLFNDirBase = "/store/user/%s/higgs-kit/Svfit/%s/"%(getUsernameFromSiteDB(), today)
				log.debug("Output directory: " + configs[-1].Data.outLFNDirBase)
				configs[-1].Data.publication = False
				configs[-1].User.voGroup = "dcms"
				configs[-1].JobType.pluginName = "PrivateMC"
				configs[-1].JobType.psetName = os.environ["CMSSW_BASE"]+"/src/CombineHarvester/CombineTools/scripts/do_nothing_cfg.py"
				configs[-1].JobType.inputFiles = [os.path.expandvars("$CMSSW_BASE/bin/$SCRAM_ARCH/ComputeSvfit"), jobfiles[-1]]
				configs[-1].JobType.allowUndistributedCMSSW = True
				configs[-1].JobType.scriptExe = jobfiles[-1]
				configs[-1].JobType.outputFiles = ["SvfitCache.tar"]
				configs[-1].Site.storageSite = "T2_DE_DESY"
	
	return [configs, jobfiles]

def submit(args):
	config, jobfile = args[0], args[1]
	
	try:
		crabCommand("submit", config=config)
	except HTTPException as hte:
		log.error("Failed submitting task: %s" % (hte.headers))
	except ClientException as cle:
		log.error("Failed submitting task: %s" % (cle))
	
	os.remove(jobfile)

def read_file(filename):
	content = ""
	with open(filename) as input_file:
		content = input_file.read()
	return content

def submission(base_path, n_processes=1):
	
	# retrieve and prepare input files
	stdout_directories, stderr_directories = tools.subprocessCall(shlex.split("gfal-ls " + base_path))
	configs_jobfiles = tools.parallelize(
			build_configs,
			[[base_path, sample] for sample in stdout_directories.decode().strip().split("\n")],
			n_processes=n_processes,
			description="Retrieving inputs and building crab configs"
	)
	
	# submit tasks
	submit_args = []
	for tmp_configs_jobfiles in configs_jobfiles:
		for config, jobfile in zip(*tmp_configs_jobfiles):
			submit_args.append([config, jobfile])
	tools.parallelize(submit, submit_args, n_processes=n_processes, description="Submitting crab tasks")


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="crab submission script for standalone Svfit calculation.",
	                                 parents=[logger.loggingParser])
	
	parser.add_argument("base_path",
	                    help="/pnfs/[path to storage element with SvfitCache input files]")
	parser.add_argument("-n", "--n-processes", type=int, default=1,
	                    help="Number of (parallel) processes. [Default: %(default)s]")
	
	args = parser.parse_args()
	logger.initLogger(args)
	
	submission(args.base_path, args.n_processes)

