#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import glob
import os

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gErrorIgnoreLevel = ROOT.kError

import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot


def get_quantities(input_filename, folder):
	input_file = ROOT.TFile(glob.glob(input_filename.split()[0])[0])
	tree = input_file.Get(folder)
	
	quantities = []
	for leaf in sorted(tree.GetListOfLeaves(), key=lambda leaf: leaf.GetName()):
		quantity = leaf.GetName()
		if leaf.GetBranch().GetMother().GetName() != leaf.GetName():
			quantity = leaf.GetBranch().GetMother().GetName()+"."+quantity
		quantities.append(quantity)
	
	input_file.Close()
	return quantities


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Make sync plots.",
	                                 parents=[logger.loggingParser])

	parser.add_argument("--input-1", help="Input files 1.", required=True)
	parser.add_argument("--input-2", help="Input files 2.", required=True)
	parser.add_argument("--folder-1", help="Folder for input 1.", required=True)
	parser.add_argument("--folder-2", help="Folder for input 2.", required=True)
	parser.add_argument("--quantities-1", help="Quantities for input 1. [Default: all in common]", nargs="+")
	parser.add_argument("--quantities-2", help="Quantities for input 2. [Default: all in common]", nargs="+")
	parser.add_argument("-e", "--event-matching", action="store_true", default=False,
	                    help="Show four histograms per plot using the output of eventmatching.py. [Default: %(default)s]")
	parser.add_argument("-a", "--args", default="--plot-modules PlotRootHtt",
	                    help="Additional Arguments for HarryPlotter. [Default: %(default)s]")
	parser.add_argument("-n", "--n-processes", type=int, default=1,
	                    help="Number of (parallel) processes. [Default: %(default)s]")
	parser.add_argument("-f", "--n-plots", type=int,
	                    help="Number of plots. [Default: all]")
	parser.add_argument("-o", "--output-dir",
	                    default="$CMSSW_BASE/src/plots/sync_plots/",
	                    help="Output directory. [Default: %(default)s]")
	parser.add_argument("-k", "--keep-eventmatching-output", action="store_true", default=False,
						help="Keep eventmatching.root. [Default: %(default)s]")
	
	args = parser.parse_args()
	logger.initLogger(args)
	
	quantities1 = args.quantities_1 if args.quantities_1 else get_quantities(args.input_1, args.folder_1)
	quantities2 = args.quantities_2 if args.quantities_2 else get_quantities(args.input_2, args.folder_2)
	if (not args.quantities_1) or (not args.quantities_2):
		common_quantities = list(set(quantities1).intersection(set(quantities2)))
		quantities1 = common_quantities
		quantities2 = common_quantities
	
	plot_configs = []
	event_matching_output = "eventmatching.root"
	for index, (quantity_1, quantity_2) in enumerate(zip(quantities1, quantities2)):
		plot_config = {}
		
		if args.event_matching:
			if index == 0:
				command = "eventmatching.py {input1} {input2} -t {folder1} {folder2} -f {output} --n-max-entries {n_max_entries}".format(
					input1=args.input_1,
					input2=args.input_2,
					folder1=args.folder_1,
					folder2=args.folder_2,
					output=event_matching_output,
					n_max_entries=100000
				)
				log.info(command)
				logger.subprocessCall(command, shell=True)
			
			plot_config["files"] = [event_matching_output]
			plot_config["folders"] = ["common1", "common2", "only1", "only2"]
			plot_config["nicks"] = ["common1", "common2", "only1", "only2"]
			plot_config["x_expressions"] = [quantity_1, quantity_2]
			plot_config["weights"] = ["("+quantity_1+"> -990)", "("+quantity_2+"> -990)"]
			
			plot_config.setdefault("analysis_modules", []).append("Ratio")
			plot_config["ratio_numerator_nicks"] = plot_config["nicks"][0]
			plot_config["ratio_denominator_nicks"] = plot_config["nicks"][1]
			
			plot_config["labels"] = ["common in 1", "common in 2", "only in 1", "only in 2", ""]
			plot_config["legend_markers"] = ["LP", "F", "F", "F", ""]
			plot_config["legend"] = [0.7, 0.55, 0.9, 0.85]
			plot_config["y_label"] = "Events"
			plot_config["fill_styles"] = [0]
			plot_config["colors"] = ["kBlack", "kRed", "kBlue", "kGreen", "kBlack"]
			plot_config["markers"] = ["P", "HIST", "HIST", "HIST", "P"]
			plot_config["y_subplot_lims"] = [0.95, 1.05]
		
		else:
			plot_config["files"] = [args.input_1, args.input_2]
			plot_config["folders"] = [args.folder_1, args.folder_2]
			plot_config["nicks"] = ["events1", "events2"]
			plot_config["x_expressions"] = [quantity_1, quantity_2]
			plot_config["weights"] = ["("+quantity_1+"> -990)", "("+quantity_2+"> -990)"]
			
			plot_config.setdefault("analysis_modules", []).append("Ratio")
			plot_config["ratio_numerator_nicks"] = plot_config["nicks"][0]
			plot_config["ratio_denominator_nicks"] = plot_config["nicks"][1]
			
			plot_config["labels"] = ["events in 1", "events in 2", ""]
			plot_config["legend_markers"] = ["LP", "F", ""]
			plot_config["legend"] = [0.7, 0.55, 0.9, 0.85]
			plot_config["y_label"] = "Events"
			plot_config["fill_styles"] = [0]
			plot_config["colors"] = ["kBlack", "kRed", "kBlack"]
			plot_config["markers"] = ["P", "HIST", "P"]
			plot_config["y_subplot_lims"] = [0.95, 1.05]
		
		plot_config["output_dir"] = os.path.expandvars(args.output_dir)
		plot_configs.append(plot_config)
			
	higgsplot.HiggsPlotter(list_of_config_dicts=plot_configs, list_of_args_strings=[args.args], n_processes=args.n_processes, n_plots=args.n_plots)
	
	if os.path.exists(event_matching_output) and not args.keep_eventmatching_output:
		os.remove(event_matching_output)

