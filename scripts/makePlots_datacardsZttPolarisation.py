#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import copy
import os
import sys

import Artus.Utility.tools as tools
import Artus.Utility.jsonTools as jsonTools
import Artus.HarryPlotter.utility.plotconfigs as plotconfigs

import HiggsAnalysis.KITHiggsToTauTau.plotting.higgsplot as higgsplot
import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.samples_run2_2015 as samples
import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.binnings as binnings
import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.systematics_run2 as systematics
import HiggsAnalysis.KITHiggsToTauTau.datacards.zttpolarisationdatacards as zttpolarisationdatacards



def _call_command(command):
	log.debug(command)
	logger.subprocessCall(command, shell=True)


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Create ROOT inputs and datacards for ZTT polarisation analysis.",
	                                 parents=[logger.loggingParser])

	parser.add_argument("-i", "--input-dir", required=True,
	                    help="Input directory.")
	parser.add_argument("-c", "--channel", action = "append",
	                    default=["mt", "et", "tt", "em"],
	                    help="Channel. This agument can be set multiple times. [Default: %(default)s]")
	parser.add_argument("--categories", action="append", nargs="+",
	                    default=[["all"]] * len(parser.get_default("channel")),
	                    help="Categories per channel. This agument needs to be set as often as --channels. [Default: %(default)s]")
	parser.add_argument("-m", "--higgs-masses", nargs="+", default=["125"],
	                    help="Higgs masses. [Default: %(default)s]")
	parser.add_argument("--add-bbb-uncs", action="store_true", default=False,
	                    help="Add bin-by-bin uncertainties. [Default: %(default)s]")
	parser.add_argument("--auto-rebin", action="store_true", default=False,
	                    help="Do auto rebinning [Default: %(default)s]")
	parser.add_argument("--lumi", type=float, default=samples.default_lumi/1000.0,
	                    help="Luminosity for the given data in fb^(-1). [Default: %(default)s]")
	parser.add_argument("-w", "--weight", default="1.0",
	                    help="Additional weight (cut) expression. [Default: %(default)s]")
	parser.add_argument("--analysis-modules", default=[], nargs="+",
	                    help="Additional analysis Modules. [Default: %(default)s]")
	parser.add_argument("-r", "--ratio", default=False, action="store_true",
	                    help="Add ratio subplot. [Default: %(default)s]")
	parser.add_argument("-a", "--args", default="",
	                    help="Additional Arguments for HarryPlotter. [Default: %(default)s]")
	#parser.add_argument("--qcd-subtract-shapes", action="store_false", default=True, help="subtract shapes for QCD estimation [Default:%(default)s]")
	parser.add_argument("-n", "--n-processes", type=int, default=1,
	                    help="Number of (parallel) processes. [Default: %(default)s]")
	parser.add_argument("-f", "--n-plots", type=int, nargs=2, default=[None, None],
	                    help="Number of plots for datacard inputs (1st arg) and for postfit plots (2nd arg). [Default: all]")
	parser.add_argument("-o", "--output-dir",
	                    default="$CMSSW_BASE/src/plots/ztt_polarisation_datacards/",
	                    help="Output directory. [Default: %(default)s]")
	parser.add_argument("--clear-output-dir", action="store_true", default=False,
	                    help="Delete/clear output directory before running this script. [Default: %(default)s]")
	parser.add_argument("--scale-lumi", default=False,
                        help="Scale datacard to luminosity specified. [Default: %(default)s]")
	parser.add_argument("--use-asimov-dataset", action="store_true", default=False,
						help="Use s+b expectation as observation instead of real data. [Default: %(default)s]")
	#parser.add_argument("--use-rate-parameter", action="store_true", default=False,
	#					help="Use rate parameter to estimate ZTT normalization from ZMM. [Default: %(default)s]")
	parser.add_argument("--era", default="2015",
	                    help="Era of samples to be used. [Default: %(default)s]")
	parser.add_argument("--www", nargs="?", default=None, const="datacards",
	                    help="Publish plots. [Default: %(default)s]")
	
	args = parser.parse_args()
	logger.initLogger(args)
	
	args.n_plots = [n_plots if n_plots >= 0 else None for n_plots in args.n_plots]
	
	if (args.era == "2015") or (args.era == "2015new"):
		import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.samples_run2_2015 as samples
	elif args.era == "2016":
		import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.samples_run2_2016 as samples
		if args.lumi == parser.get_default("lumi"):
			args.lumi = samples.default_lumi/1000.0
	else:
		log.critical("Invalid era string selected: " + args.era)
		sys.exit(1)
	
	args.output_dir = os.path.abspath(os.path.expandvars(args.output_dir))
	if args.clear_output_dir and os.path.exists(args.output_dir):
		logger.subprocessCall("rm -r " + args.output_dir, shell=True)
	
	# initialisations for plotting
	sample_settings = samples.Samples()
	binnings_settings = binnings.BinningsDict()
	systematics_factory = systematics.SystematicsFactory()
	
	plot_configs = []
	output_files = []
	merged_output_files = []
	hadd_commands = []
	
	datacards = zttpolarisationdatacards.ZttPolarisationDatacards() # useRateParam=args.use_rate_parameter
	
	# initialise datacards
	tmp_input_root_filename_template = "input/${ANALYSIS}_${CHANNEL}_${BIN}_${SYSTEMATIC}_${ERA}.root"
	input_root_filename_template = "input/${ANALYSIS}_${CHANNEL}_${BIN}_${ERA}.root"
	bkg_histogram_name_template = "${BIN}/${PROCESS}"
	sig_histogram_name_template = "${BIN}/${PROCESS}"
	bkg_syst_histogram_name_template = "${BIN}/${PROCESS}_${SYSTEMATIC}"
	sig_syst_histogram_name_template = "${BIN}/${PROCESS}_${SYSTEMATIC}"
	datacard_filename_templates = [
		"datacards/individual/${CHANNEL}/${BINID}/${ANALYSIS}_${CHANNEL}_${BINID}_${ERA}.txt",
		"datacards/channel/${CHANNEL}/${ANALYSIS}_${CHANNEL}_${ERA}.txt",
		"datacards/category/${BINID}/${ANALYSIS}_${BINID}_${ERA}.txt",
		"datacards/combined/${ANALYSIS}_${ERA}.txt",
	]
	output_root_filename_template = "datacards/common/${ANALYSIS}.input_${ERA}.root"
	
	if args.channel != parser.get_default("channel"):
		args.channel = args.channel[len(parser.get_default("channel")):]
	
	if args.categories != parser.get_default("categories"):
		args.categories = args.categories[len(parser.get_default("categories")):]
	args.categories = (args.categories * len(args.channel))[:len(args.channel)]
	
	# restrict CombineHarvester to configured channels
	datacards.cb.channel(args.channel)

	for index, (channel, categories) in enumerate(zip(args.channel, args.categories)):
		
		# prepare category settings based on args and datacards
		if (len(categories) == 1) and (categories[0] == "all"):
			categories = datacards.cb.cp().channel([channel]).bin_set()
		else:
			categories = list(set(categories).intersection(set(datacards.cb.cp().channel([channel]).bin_set())))
		args.categories[index] = categories
		
		# restrict CombineHarvester to configured categories:
		datacards.cb.FilterAll(lambda obj : (obj.channel() == channel) and (obj.bin() not in categories))
		
		for category in categories:
			datacards_per_channel_category = zttpolarisationdatacards.ZttPolarisationDatacards(cb=datacards.cb.cp().channel([channel]).bin([category]))
			
			higgs_masses = [mass for mass in datacards_per_channel_category.cb.mass_set() if mass != "*"]
			
			output_file = os.path.join(args.output_dir, input_root_filename_template.replace("$", "").format(
					ANALYSIS="ztt",
					CHANNEL=channel,
					BIN=category,
					ERA="13TeV"
			))
			output_files.append(output_file)
			tmp_output_files = []
			
			for shape_systematic, list_of_samples in datacards_per_channel_category.get_samples_per_shape_systematic().iteritems():
				nominal = (shape_systematic == "nominal")
				list_of_samples = (["data"] if nominal else []) + [datacards.configs.process2sample(process) for process in list_of_samples]
				
				for shift_up in ([True] if nominal else [True, False]):
					systematic = "nominal" if nominal else (shape_systematic + ("Up" if shift_up else "Down"))
					
					log.debug("Create inputs for (samples, systematic) = ([\"{samples}\"], {systematic}), (channel, category) = ({channel}, {category}).".format(
							samples="\", \"".join(list_of_samples),
							channel=channel,
							category=category,
							systematic=systematic
					))
					
					# prepare plotting configs for retrieving the input histograms
					config = sample_settings.get_config(
							samples=[getattr(samples.Samples, sample) for sample in list_of_samples],
							channel=channel,
							category="catZttPol13TeV_"+category,
							weight=args.weight,
							lumi = args.lumi * 1000,
							higgs_masses=higgs_masses,
							estimationMethod="new",
							polarisation_bias_correction=True,
							cut_type="baseline_low_mvis"
					)
					
					systematics_settings = systematics_factory.get(shape_systematic)(config)
					# TODO: evaluate shift from datacards_per_channel_category.cb
					config = systematics_settings.get_config(shift=(0.0 if nominal else (1.0 if shift_up else -1.0)))
					
					#config["qcd_subtract_shape"] =[args.qcd_subtract_shapes]
					
					config["x_expressions"] = [("0" if "_gen" in nick else "testZttPol13TeV_"+category) for nick in config["nicks"]]

					binnings_key = "binningZttPol13TeV_"+category
					if binnings_key in binnings_settings.binnings_dict:
						config["x_bins"] = [("1,-1,1" if "_gen" in nick else binnings_key) for nick in config["nicks"]]
						
					config["directories"] = [args.input_dir]
					
					histogram_name_template = bkg_histogram_name_template if nominal else bkg_syst_histogram_name_template
					config["labels"] = [histogram_name_template.replace("$", "").format(
							PROCESS=datacards.configs.sample2process(sample),
							BIN=category,
							SYSTEMATIC=systematic
					) for sample in config["labels"]]
					
					tmp_output_file = os.path.join(args.output_dir, tmp_input_root_filename_template.replace("$", "").format(
							ANALYSIS="ztt",
							CHANNEL=channel,
							BIN=category,
							SYSTEMATIC=systematic,
							ERA="13TeV"
					))
					tmp_output_files.append(tmp_output_file)
					config["output_dir"] = os.path.dirname(tmp_output_file)
					config["filename"] = os.path.splitext(os.path.basename(tmp_output_file))[0]
				
					config["plot_modules"] = ["ExportRoot"]
					config["file_mode"] = "UPDATE"
			
					if "legend_markers" in config:
						config.pop("legend_markers")
					
					plot_configs.append(config)
			
			hadd_commands.append("hadd -f {DST} {SRC} && rm {SRC}".format(
					DST=output_file,
					SRC=" ".join(tmp_output_files)
			))
	
	if log.isEnabledFor(logging.DEBUG):
		import pprint
		pprint.pprint(plot_configs)
	
	# delete existing output files
	tmp_output_files = list(set([os.path.join(config["output_dir"], config["filename"]+".root") for config in plot_configs[:args.n_plots[0]]]))
	for output_file in tmp_output_files:
		if os.path.exists(output_file):
			os.remove(output_file)
			log.debug("Removed file \""+output_file+"\" before it is recreated again.")
	output_files = list(set(output_files))
	
	# create input histograms with HarryPlotter
	higgsplot.HiggsPlotter(list_of_config_dicts=plot_configs, list_of_args_strings=[args.args], n_processes=args.n_processes, n_plots=args.n_plots[0])
	if args.n_plots[0] != 0:
		tools.parallelize(_call_command, hadd_commands, n_processes=args.n_processes)
	
	debug_plot_configs = []
	for output_file in (output_files):
		debug_plot_configs.extend(plotconfigs.PlotConfigs().all_histograms(output_file, plot_config_template={"markers":["E"], "colors":["#FF0000"]}))
	if args.www:
		for debug_plot_config in debug_plot_configs:
			debug_plot_config["www"] = debug_plot_config["output_dir"].replace(args.output_dir, args.www)
	higgsplot.HiggsPlotter(list_of_config_dicts=debug_plot_configs, list_of_args_strings=[args.args], n_processes=args.n_processes, n_plots=args.n_plots[0])
	
	# update CombineHarvester with the yields and shapes
	datacards.extract_shapes(
			os.path.join(args.output_dir, input_root_filename_template.replace("$", "")),
			bkg_histogram_name_template, sig_histogram_name_template,
			bkg_syst_histogram_name_template, sig_syst_histogram_name_template,
			update_systematics=True
	)
	
	# add bin-by-bin uncertainties
	if args.add_bbb_uncs:
		datacards.add_bin_by_bin_uncertainties(
				processes=datacards.cb.cp().backgrounds().process_set(),
				add_threshold=0.1, merge_threshold=0.5, fix_norm=True
		)
	

	# scale
	if(args.scale_lumi):
		datacards.scale_expectation( float(args.scale_lumi) / args.lumi)
		
	# use asimov dataset for s+b
	asimov_options = ""
	if args.use_asimov_dataset:
		#asimov_options = "--expectSignal 1.0 -t -1 --setPhysicsModelParameters \"pol=-0.159,r=1\""
		
		pospol_signals = datacards.cb.cp().signals()
		pospol_signals.FilterAll(lambda obj : ("pospol" not in obj.process().lower()))
		pospol_signals.ForEachProc(lambda process: process.set_rate(process.no_norm_rate() * (1.0 - 0.159)))
		
		negpol_signals = datacards.cb.cp().signals()
		negpol_signals.FilterAll(lambda obj : ("negpol" not in obj.process().lower()))
		negpol_signals.ForEachProc(lambda process: process.set_rate(process.no_norm_rate() * (1.0 + 0.159)))
		
		datacards.replace_observation_by_asimov_dataset()
		
		pospol_signals.ForEachProc(lambda process: process.set_rate(process.no_norm_rate() / (1.0 - 0.159)))
		negpol_signals.ForEachProc(lambda process: process.set_rate(process.no_norm_rate() / (1.0 + 0.159)))

	if args.auto_rebin:
		datacards.auto_rebin(bin_threshold = 1.0, rebin_mode = 0)

	# write datacards and call text2workspace
	datacards_cbs = {}
	for datacard_filename_template in datacard_filename_templates:
		datacards_cbs.update(datacards.write_datacards(
				datacard_filename_template.replace("{", "").replace("}", ""),
				output_root_filename_template.replace("{", "").replace("}", ""),
				args.output_dir
		))
	
	datacards_workspaces = datacards.text2workspace(
			datacards_cbs,
			args.n_processes,
			"-P {MODEL} {MODEL_PARAMETERS}".format(
					MODEL="HiggsAnalysis.KITHiggsToTauTau.datacards.zttmodels:ztt_pol",
					MODEL_PARAMETERS=""
			)
	)
	
	# Max. likelihood fit and postfit plots
	datacards.combine(
			datacards_cbs,
			datacards_workspaces,
			None,
			args.n_processes,
			"-M MaxLikelihoodFit --saveWorkspace --redefineSignalPOIs pol "+(asimov_options if args.use_asimov_dataset else "")+" "+datacards.stable_options+" -n \"\"",
			split_stat_syst_uncs=False # MaxLikelihoodFit does not support the splitting of uncertainties
	)
	
	datacards_postfit_shapes = datacards.postfit_shapes_fromworkspace(
			datacards_cbs,
			datacards_workspaces,
			False,
			args.n_processes,
			"--sampling" + (" --print" if args.n_processes <= 1 else "")
	)
	
	datacards.prefit_postfit_plots(
			datacards_cbs,
			datacards_postfit_shapes,
			plotting_args={"ratio" : args.ratio, "args" : args.args, "lumi" : args.lumi, "x_expressions" : "tauPolarisationDiscriminator", "era" : "2015", "www" : args.www},
			n_processes=args.n_processes,
			signal_stacked_on_bkg=True
	)
	
	datacards.print_pulls(datacards_cbs, args.n_processes, "-A -p {POI}".format(POI="pol"))
	datacards.pull_plots(
			datacards_postfit_shapes,
			s_fit_only=True,
			plotting_args={"fit_poi" : ["pol"], "formats" : ["pdf", "png"], "args" : args.args, "www" : args.www},
			n_processes=args.n_processes
	)
	#datacards.nuisance_impacts(datacards_cbs, datacards_workspaces, args.n_processes)
	
	# split uncertainties
	datacards.combine(
			datacards_cbs,
			datacards_workspaces,
			None,
			args.n_processes,
			"-M MultiDimFit --algo singles -P pol --floatOtherPOIs 1 "+(asimov_options if args.use_asimov_dataset else "")+" "+datacards.stable_options+" -n ",
			split_stat_syst_uncs=True,
	)
	
	annotation_replacements = {channel : index for (index, channel) in enumerate(["combined"] + args.channel)}
	annotation_replacements.update({binid : index+1 for (index, binid) in enumerate(sorted(list(set([datacards.configs.category2binid(category, channel=category[:2]) for category in tools.flattenList(args.categories)]))))})
	values_tree_files = {}
	datacards.annotate_trees(
			datacards_workspaces,
			"higgsCombine*.*.mH*.root",
			[
					[os.path.join(os.path.dirname(template.replace("${CHANNEL}", "(.*)").replace("${MASS}", "\d*")), ".*.root") for template in datacard_filename_templates if "channel" in template][0],
					[os.path.join(os.path.dirname(template.replace("${BINID}", "(\d*)").replace("${MASS}", "\d*")), ".*.root") for template in datacard_filename_templates if "category" in template][0],
			],
			annotation_replacements,
			args.n_processes,
			values_tree_files,
			"-t limit -b channel category"
	)
	datacards.annotate_trees(
			datacards_workspaces,
			"higgsCombine*.*.mH*.root",
			[
					[os.path.join(os.path.dirname(template.replace("combined", "(combined)").replace("${MASS}", "\d*")), ".*.root") for template in datacard_filename_templates if "combined" in template][0],
			]*2,
			annotation_replacements,
			args.n_processes,
			values_tree_files,
			"-t limit -b channel category"
	)
	
	# plot best fit values of parameter pol from physics model
	plot_configs = []
	for template in ["$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/plots/configs/combine/best_fit_pol_over_channel.json",
	                 "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/plots/configs/combine/best_fit_pol_over_channel_tot_stat_unc.json",
	                 "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/plots/configs/combine/best_fit_weinberg_angle_over_channel.json",
	                 "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/plots/configs/combine/best_fit_weinberg_angle_over_channel_tot_stat_unc.json"]:
		
		x_values = sorted([values[0] for values in values_tree_files.keys() if values[0] > -990.0])
		config = jsonTools.JsonDict(os.path.expandvars(template))
		config["directories"] = [" ".join(set([os.path.dirname(root_file) for root_file in sorted(tools.flattenList(values_tree_files.values()))]))]
		config["x_ticks"] = x_values
		inv_annotation_replacements = {value : key for key, value in annotation_replacements.iteritems() if (type(key) != int) or (key < 1000)}
		config["x_tick_labels"] = [str(inv_annotation_replacements.get(int(value), value)) for value in x_values]
		#config["x_tick_labels"] = ["#scale[1.5]{" + ("" if label == "combined" else "channel_") + label + "}" for label in config["x_tick_labels"]]
		config["x_tick_labels"] = ["" + ("" if label == "combined" else "channel_") + label + "" for label in config["x_tick_labels"]]
		config["x_lims"] = [min(x_values) - 0.5, max(x_values) + 0.5]
		config["output_dir"] = os.path.join(args.output_dir, "datacards/combined/plots")
		if args.www:
			config["www"] = os.path.join(args.www, "combined/plots")
		
		plot_configs.append(config)
	
	higgsplot.HiggsPlotter(list_of_config_dicts=plot_configs, list_of_args_strings=[args.args], n_processes=args.n_processes, n_plots=args.n_plots[1])

