# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import os

import Artus.KappaAnalysis.kappaanalysiswrapper as kappaanalysiswrapper
import Artus.Utility.jsonTools as jsonTools
import Artus.Utility.tools as tools

import sys

class HiggsToTauTauAnalysisWrapper(kappaanalysiswrapper.KappaAnalysisWrapper):

	def __init__(self):
		#self._config = jsonTools.JsonDict()
		self._config = {}
		self._executable = executable

		self._parser = None
		#Load default argument parser
		self._initArgumentParser(userArgParsers)
		#Parse command line arguments and return dict
		self._args = self._parser.parse_args()
		logger.initLogger(self._args)

		# expand the environment variables only at the batch node
		if self._args.batch:
			self._args.envvar_expansion = False

		date_now = datetime.now().strftime("%Y-%m-%d_%H-%M")

		# write repository revisions to the config
		if not self._args.disable_repo_versions:
			self.setRepositoryRevisions()
			self._config["Date"] = date_now

		#Expand Config
		self.expandConfig_python()
		self.projectPath = None
		self.localProjectPath = None
		self.remote_se = False

		if self._args.batch:
			self.projectPath = os.path.join(os.path.expandvars(self._args.work), date_now+"_"+self._args.project_name)
			self.localProjectPath = self.projectPath
			if self.projectPath.startswith("srm://"):
				self.remote_se = True
				self.localProjectPath = os.path.join(os.path.expandvars(self._parser.get_default("work")), date_now+"_"+self._args.project_name)


	def _initArgumentParser(self, userArgParsers=None):
		super(HiggsToTauTauAnalysisWrapper, self)._initArgumentParser(userArgParsers)

	def modify_replacing_dict(self):
		self.replacingDict["areafiles"] += " -data/Samples auxiliaries/mva_weights ZZMatrixElement/MELA"

	def remove_pipeline_copies(self):
		pipelines = self._config.get("Pipelines", {}).keys()
		pipelines_to_remove = []
		pipeline_renamings = {}
		for index1, pipeline1 in enumerate(pipelines):
			if pipeline1 in pipelines_to_remove:
				continue

			for pipeline2 in pipelines[index1+1:]:
				if pipeline2 in pipelines_to_remove:
					continue

				difference = jsonTools.JsonDict.deepdiff(self._config["Pipelines"][pipeline1],
				                                         self._config["Pipelines"][pipeline2])
				if len(difference[0]) == 0 and len(difference[1]) == 0:
					pipelines_to_remove.append(pipeline2)
					new_name = tools.find_common_string(pipeline_renamings.get(pipeline1, pipeline1),
					                                    pipeline_renamings.get(pipeline2, pipeline2))
					# Needed for systematic shifts that are only applied to certain samples.
					# In that case we do not want an extra pipeline with the same configuration
					# as the nominal one.
					if "Down" not in new_name or "Up" not in new_name:
						new_name = new_name.replace(new_name.split("_")[-1], "")
					# Add "nominal" to pipelines without systematic shifts
					if new_name.endswith("_"):
						new_name += "nominal"
					elif "_" not in new_name:
						new_name += "_nominal"
					pipeline_renamings[pipeline1] = new_name.strip("_").replace("__", "_")

		for pipeline in pipelines_to_remove:
			self._config["Pipelines"].pop(pipeline)

		for old_name, new_name in pipeline_renamings.iteritems():
			self._config["Pipelines"][new_name] = self._config["Pipelines"].pop(old_name)

	def expandConfig_python(self):

		# merge all base configs into the main config
		if self._args.base_configs!=None:
			self._config = jsonTools.JsonDict(self._config)
			self._config += jsonTools.JsonDict.mergeAll(self._args.base_configs)

		self._gridControlInputFiles = {}

		#Set Input Filenames
		if self._args.input_files:
			self._config["InputFiles"] = [] #overwrite settings from config file by command line
			inputFileList = self._args.input_files
			for entry in range(len(inputFileList)):
				inputFileList[entry] = inputFileList[entry].replace('"', '').replace("'", '').replace(',', '')
			self.setInputFilenames(self._args.input_files)
		else:
			tmpInputFiles = self._config["InputFiles"]
			self._config["InputFiles"] = []
			self.setInputFilenames(tmpInputFiles)

		if not self._args.n_events is None:
			self._config["ProcessNEvents"] = self._args.n_events

		# shrink Input Files to requested Number
		self.removeUnwantedInputFiles()

		if self._args.output_file:
			self.setOutputFilename(self._args.output_file)

		# treat pipeline configs
		"""		
		pipelineJsonDict = {}
		
		if self._args.pipeline_configs and len(self._args.pipeline_configs) > 0:
			pipelineJsonDict = []
			print self._args.pipeline_configs
			for pipelineConfigs in self._args.pipeline_configs:
				pipelineJsonDict.append(jsonTools.JsonDict.expandAll(*map(lambda pipelineConfig: jsonTools.JsonDict.mergeAll(*pipelineConfig.split()), pipelineConfigs)))
			pipelineJsonDict = jsonTools.JsonDict.mergeAll(*pipelineJsonDict)
			pipelineJsonDict = jsonTools.JsonDict({"Pipelines": pipelineJsonDict})
		pipelineJsonDict = jsonTools.JsonDict(pipelineJsonDict)
		"""

		nickname = self.determineNickname(self._args.nick)
		print nickname
		print self._args.channels
		if nickname != "auto":
			if self._args.channels and len(self._args.channels) > 0:
				pipeline_config = {} #TODO add systematic option, extra loop or in pipelines?
				syst_python_config = systematics.Systematics_Config()

				for selected_channel in self._args.channels:
					if selected_channel == "mt":
						channel_python_config = mt.mt_ArtusConfig() 
						channel_python_config.build_config(nickname)
					
					elif selected_channel == "et":
						channel_python_config = et.et_ArtusConfig() 
						channel_python_config.build_config(nickname)
					
					elif selected_channel == "em":
						channel_python_config = em.em_ArtusConfig() #TODO change to the em config but for now let it be
						channel_python_config.build_config(nickname)

					elif selected_channel == "tt":
						channel_python_config = tt.tt_ArtusConfig() 
						channel_python_config.build_config(nickname)

					elif selected_channel == "mm":
						channel_python_config = mm.mm_ArtusConfig() #TODO change to the mm config but for now let it be
						channel_python_config.build_config(nickname)

					elif selected_channel == "gen":	
						channel_python_config = gen.gen_ArtusConfig()
						channel_python_config.build_config(nickname)
					else:	
						log.error("COULD NOT FIND CHANNEL")
					#Ideas:
					#TODO add function that adds list of quantities to the pipeline_python_config
					"""
					if len(args.add_quantities)>0:
						pipeline_python_config["Quantities"]+= args.add_quantities
					if len(args.add_processors)>0:
						pipeline_python_config["Processors"]+= args.add_processors
					#TODO: add function that lets you run artus for variables which are not in allready processed output files such that you can merge them later into the old outputs
					if len(args.new_quantities)>0:
						pipeline_python_config["Quantities"] = args.new_quantities
					if len(args.new_processors)>0:
						pipeline_python_config["Processors"] = args.add_processors
					
					"""
					if selected_channel != "gen":	
						for systematic_shift in self._args.systematics:

							if systematic_shift != "nominal":
								for shiftdirection in ["Up", "Down"]:
									systematic_name = systematic_shift+shiftdirection
									syst_python_config.clear_config()
									syst_python_config.build_systematic_config(nickname, systematic_name)
									pipeline_config[selected_channel+"_"+systematic_name] = copy.deepcopy(syst_python_config)
									pipeline_config[selected_channel+"_"+systematic_name].update(copy.deepcopy(channel_python_config))


							elif systematic_shift == "nominal":
								syst_python_config.clear_config()
								pprint(syst_python_config)
								pipeline_config[selected_channel+"_"+systematic_shift] = copy.deepcopy(syst_python_config)
								pipeline_config[selected_channel+"_"+systematic_shift].update(channel_python_config)

	
					elif selected_channel == "gen":
						pipeline_config["gen"] = channel_python_config
				

			self._config["Pipelines"] = pipeline_config	
			

			# treat pipeline base configs

			pipelineBaseDict = baseconfigcp.Baseconfig_cp(nickname)
			globalProcessorsDict = globalprocessors.globalProccesors(nickname)

			# merge pipeline config and baseline config
			self._config.update(pipelineBaseDict)
			self._config.update(globalProcessorsDict)
			
	
		self._config = jsonTools.JsonDict(self._config)

		# treat includes, nicks and comments
		self.tmp_directory_remote_files = None
		if self._args.batch:
			self._config = self._config.doIncludes().doComments()
			self._config["BatchMode"] = True
		else:
			log.debug("Prepare config for \""+nickname+"\" sample...")
			self._config = self._config.doIncludes().doNicks(nickname).doComments()
			self._config["Nickname"] = nickname

			#read in external values
			self.readInExternals()

		# remove all but one of similar pipeline copies
		self.remove_pipeline_copies()

		# treat environment variables
		if self._args.envvar_expansion:
			self._config = self._config.doExpandvars()

		# treat remote files
		if self._args.copy_remote_files and (not self._args.batch):
			self.useLocalCopiesOfRemoteFiles()

		# set log level
		self._config["LogLevel"] = self._args.log_level

	def readInExternals(self):
		if not "NumberGeneratedEvents" in self._config or (int(self._config["NumberGeneratedEvents"]) < 0):
			from Kappa.Skimming.registerDatasetHelper import get_n_generated_events_from_nick
			from Kappa.Skimming.datasetsHelper2015 import isData
			n_events_from_db = get_n_generated_events_from_nick(self._config["Nickname"])
			if(n_events_from_db > 0):
				self._config["NumberGeneratedEvents"] = n_events_from_db
			elif not isData(self._config["Nickname"]):
				log.fatal("Number of Generated Events not set! Check your datasets.json for nick " + self._config["Nickname"])
				sys.exit(1)

		if not ("CrossSection" in self._config) or (self._config["CrossSection"] < 0):
			from Kappa.Skimming.registerDatasetHelper import get_xsec
			from Kappa.Skimming.datasetsHelper2015 import isData
			xsec = get_xsec(self._config["Nickname"])
			if(xsec > 0):
				self._config["CrossSection"] = xsec
			elif not isData(self._config["Nickname"]):
				log.fatal("Cross section for " + self._config["Nickname"] + " not set! Check your datasets.json")
				sys.exit(1)

		if not ("GeneratorWeight" in self._config):
			from Kappa.Skimming.registerDatasetHelper import get_generator_weight
			from Kappa.Skimming.datasetsHelper2015 import isData
			generator_weight = get_generator_weight(self._config["Nickname"])
			if(generator_weight > 0 and generator_weight <= 1.0):
				self._config["GeneratorWeight"] = generator_weight


	def run(self):
		#symlinkBaseDir = os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/ArtusOutputs")
		#if not os.path.exists(symlinkBaseDir):
		#	os.makedirs(symlinkBaseDir)
		
		#if not self.projectPath is None:
		#	symlinkDir = os.path.join(symlinkBaseDir, "recent")
		#	if os.path.islink(symlinkDir):
		#		os.remove(symlinkDir)
		#	os.symlink(self.projectPath, symlinkDir)
		
		exitCode = super(HiggsToTauTauAnalysisWrapper, self).run()
		
		#if not self.projectPath is None:
		#	symlinkDir = os.path.join(symlinkBaseDir, os.path.basename(self.projectPath))
		#	os.symlink(self.projectPath, symlinkDir)
		
		return exitCode
