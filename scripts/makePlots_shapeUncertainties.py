#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import os

import ROOT

import Artus.HarryPlotter.utility.roottools as roottools
import Artus.Utility.tfilecontextmanager as tfilecontextmanager

import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot



if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description="Plot shape uncertainties.",
	                                 parents=[logger.loggingParser])
	
	parser.add_argument("files", nargs="+",
	                    help="Limit input ROOT files.")
	parser.add_argument("-a", "--args", default="--plot-modules PlotRootHtt",
	                    help="Additional Arguments for HarryPlotter. [Default: %(default)s]")
	parser.add_argument("-r", "--ratio", default=False, action="store_true",
	                    help="Add ratio subplot. [Default: %(default)s]")
	parser.add_argument("-n", "--n-processes", type=int, default=1,
	                    help="Number of (parallel) processes. [Default: %(default)s]")
	parser.add_argument("-f", "--n-plots", type=int,
	                    help="Number of plots. [Default: all]")
	parser.add_argument("-o", "--output-dir", default=None,
	                    help="Output directory. [Default: relative to datacards]")
	
	args = parser.parse_args()
	logger.initLogger(args)
	
	plot_configs = []
	for input_file in args.files:
		root_file_content = []
		with tfilecontextmanager.TFileContextManager(input_file, "READ") as root_file:
			root_file_content = roottools.RootTools.walk_root_directory(root_file)
		
		parsed_root_file_content = {}
		for key, path in root_file_content:
			folder = os.path.dirname(path)
			histogram = os.path.basename(path)
			histogram_parts = histogram.split("_")
			process = histogram_parts[0]
			uncertainty = "_".join(histogram_parts[1:])
			index = None
			shift_up = uncertainty.endswith("Up")
			if shift_up:
				uncertainty = uncertainty[:-2]
				index = 1
			shift_down = uncertainty.endswith("Down")
			if shift_down:
				uncertainty = uncertainty[:-4]
				index = 0
			if shift_up or shift_down:
				parsed_root_file_content.setdefault(folder, {}).setdefault((process, uncertainty), [None, None])[index] = histogram
		
		for folder, folder_content in parsed_root_file_content.iteritems():
			for (process, uncertainty), histograms in folder_content.iteritems():
				
				config = {}
				config["files"] = [input_file]
				config["folders"] = [folder]
				config["x_expressions"] = ([process]+histograms)[::-1]
				config["nicks"] = ([process]+histograms)[::-1]
				
				config["colors"] = ["#FF0000", "#0000FF", "#000000"]
				config["markers"] = ["LINE E", "LINE E", "E"]
				config["marker_styles"] = [0, 0, 20]
				config["legend_markers"] = ["L", "L", "ELP"]
				config["labels"] = ["#plus 1#sigma shift", "#minus 1#sigma shift", "nominal"]
				
				uncString = uncertainty
				if "_qcd_" in uncertainty and "syst" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from QCD syst." 
				if "_qcd_" in uncertainty and "stat" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from QCD stat." 
				if "_w_" in uncertainty and "syst" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from W+Jets syst." 
				if "_w_" in uncertainty and "stat" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from W+Jets stat." 
				if "_tt_" in uncertainty and "syst" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from TT+Jets syst." 
				if "_tt_" in uncertainty and "stat" in uncertainty:
					uncString = "Jet #rightarrow #tau Fakes Shape from TT+Jets stat." 
				if "ttbarShape" in uncertainty:
					uncString = "Top p_T Reweighting Shape Uncertainty"
				if "dyShape" in uncertainty:
					uncString = "Z Reweighting Shape Uncertainty"
				if "scale_t" in uncertainty:
					uncString = "#tau Energy Scale Shape Uncertainty"

				config["legend"] = [0.65, 0.7, 0.9, 0.88]
				config["title"] = uncString+" ("+process+")"
				config["x_label"] = "Visible di-tau Mass / GeV"
				
				if args.ratio:
					if not "Ratio" in config.get("analysis_modules", []):
						config.setdefault("analysis_modules", []).append("Ratio")
					config.setdefault("ratio_numerator_nicks", []).extend(histograms[::-1])
					config.setdefault("ratio_denominator_nicks", []).extend([process] * 2)
					config.setdefault("ratio_result_nicks", []).extend(["ratio_up", "ratio_down"])
					
					config["colors"].extend(config["colors"][:2])
					#config["markers"].extend(config["markers"][:2])
					config["markers"] = ["LINE E", "LINE E", "E", "LINE", "LINE"]
					config["marker_styles"].extend(config["marker_styles"][:2])
					config["legend_markers"].extend(config["legend_markers"][:2])
					config["labels"].extend([""] * 2)					

					config["legend"] = [0.65, 0.65, 0.95, 0.85]
					config["y_subplot_lims"] = [0.8, 1.2]
					if "stat" in uncertainty:
						config["y_subplot_lims"] = [0.9, 1.1]
					if "_w_" in uncertainty:
						config["y_subplot_lims"] = [0.95, 1.05]
					if "_tt_" in uncertainty:
						config["y_subplot_lims"] = [0.98, 1.02]
				
				output_dir = args.output_dir
				if output_dir is None:
					output_dir = os.path.join(os.path.splitext(input_file)[0], folder, uncertainty)
				config["output_dir"] = output_dir
				config["filename"] = uncertainty+"_"+process
				
				plot_configs.append(config)
	
	if log.isEnabledFor(logging.DEBUG):
		import pprint
		pprint.pprint(configs)
	
	higgs_plotter = higgsplot.HiggsPlotter(list_of_config_dicts=plot_configs, list_of_args_strings=[args.args], n_processes=args.n_processes, n_plots=args.n_plots)

