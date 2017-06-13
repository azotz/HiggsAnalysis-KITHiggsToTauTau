# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.categories as Categories
import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards
import CombineHarvester.CombineTools.ch as ch

class SMHttDatacards(datacards.Datacards):
	def __init__(self, higgs_masses=["125"], useRateParam=False, year="", cb=None):
		super(SMHttDatacards, self).__init__(cb)

		if cb is None:
			signal_processes = ["ggH", "qqH", "WH", "ZH"]
			
			background_processes_mt = ["ZTT", "ZL", "ZJ", "TTT", "TTJJ", "VVT", "VVJ", "W", "QCD"]
			background_processes_et = ["ZTT", "ZL", "ZJ", "TTT", "TTJJ", "VVT", "VVJ", "W", "QCD"]
			background_processes_tt = ["ZTT", "ZL", "ZJ", "TTT", "TTJJ", "VVT", "VVJ", "W", "QCD"]
			background_processes_em = ["ZTT", "ZLL", "TT", "VV", "hww_gg125", "hww_qq125", "W", "QCD"]
			background_processes_mm = ["ZLL", "TT", "VV", "W"]
			
			all_mc_bkgs = ["ZTT", "ZL", "ZJ", "TT", "TTT", "TTJJ", "VV", "VVT", "VVJ", "W", "hww_gg125", "hww_qq125"]
			all_mc_bkgs_no_W = ["ZTT", "ZL", "ZJ", "TT", "TTT", "TTJJ", "VV", "VVT", "VVJ", "hww_gg125", "hww_qq125"]
			all_mc_bkgs_no_TTJ = ["ZTT", "ZL", "ZJ", "TT", "TTT", "VV", "VVT", "VVJ", "W", "hww_gg125", "hww_qq125"]
			
			# list of JEC uncertainties
			jecUncertNames = [
				"AbsoluteFlavMap",
				"AbsoluteMPFBias",
				"AbsoluteScale",
				"AbsoluteStat",
				"FlavorQCD",
				"Fragmentation",
				"PileUpDataMC",
				"PileUpPtBB",
				"PileUpPtEC1",
				"PileUpPtEC2",
				"PileUpPtHF",
				"PileUpPtRef",
				"RelativeBal",
				"RelativeFSR",
				"RelativeJEREC1",
				"RelativeJEREC2",
				"RelativeJERHF",
				"RelativePtBB",
				"RelativePtEC1",
				"RelativePtEC2",
				"RelativePtHF",
				"RelativeStatEC",
				"RelativeStatFSR",
				"RelativeStatHF",
				"SinglePionECAL",
				"SinglePionHCAL",
				"TimePtEta"
			]

			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=Categories.CategoriesDict().getCategories(["mt"])["mt"],
					bkg_processes=background_processes_mt,
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# efficiencies
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["mt"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.trigger_efficiency2016_syst_args)
				self.cb.cp().channel(["mt"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.muon_efficiency2016_syst_args)
				self.cb.cp().channel(["mt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.tau_efficiency2016_syst_args)
			else:
				self.cb.cp().channel(["mt"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.muon_efficiency_syst_args)
				self.cb.cp().channel(["mt"]).process(signal_processes+["ZTT", "TTT", "VVT"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)

			# mu->tau fake ES
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, "CMS_ZLShape_mt_1prong_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, "CMS_ZLShape_mt_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))

			# mu->tau fake rate
			if year == "2016":
				self.cb.cp().channel(["mt"]).process(["ZL"]).bin(["mt_ZeroJet2D", "mt_Boosted2D", "mt_Vbf2D"]).AddSyst(self.cb, "CMS_mFakeTau_1prong_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["mt"]).process(["ZL"]).bin(["mt_ZeroJet2D", "mt_Boosted2D", "mt_Vbf2D"]).AddSyst(self.cb, "CMS_mFakeTau_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))
			else:
				self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			
			# decay mode reweighting
			self.cb.cp().channel(["mt"]).process(["ZTT"]).bin(["mt_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_1prong_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["mt"]).process(["ZTT"]).bin(["mt_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["mt"]).process(["ZTT"]).bin(["mt_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_3prong_13TeV", "shape", ch.SystMap()(1.0))
			
			if useRateParam:
				for category in Categories.CategoriesDict().getCategories(["mt"], False)["mt"]:
					self.cb.cp().channel(["mt"]).bin(["mt_"+category]).process(["ZTT"]).AddSyst(self.cb, "n_zll_"+category+"_norm", "rateParam", ch.SystMap()(1.0))

			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=Categories.CategoriesDict().getCategories(["et"])["et"],
					bkg_processes=background_processes_et,
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# efficiencies
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.trigger_efficiency2016_syst_args)
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.electron_efficiency2016_syst_args)
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.tau_efficiency2016_syst_args)
			else:
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.electron_efficiency_syst_args)
				self.cb.cp().channel(["et"]).process(signal_processes+["ZTT", "TTT", "VVT"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)

			# e->tau fake ES
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, "CMS_ZLShape_et_1prong_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, "CMS_ZLShape_et_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))

			# e->tau fake rate
			if year == "2016":
				self.cb.cp().channel(["et"]).process(["ZL"]).bin(["et_ZeroJet2D", "et_Boosted2D", "et_Vbf2D"]).AddSyst(self.cb, "CMS_eFakeTau_1prong_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["et"]).process(["ZL"]).bin(["et_ZeroJet2D", "et_Boosted2D", "et_Vbf2D"]).AddSyst(self.cb, "CMS_eFakeTau_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))
			else:
				self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_tight_syst_args)
			
			# decay mode reweighting
			self.cb.cp().channel(["et"]).process(["ZTT"]).bin(["et_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_1prong_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et"]).process(["ZTT"]).bin(["et_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et"]).process(["ZTT"]).bin(["et_ZeroJet2D"]).AddSyst(self.cb, "CMS_tauDMReco_3prong_13TeV", "shape", ch.SystMap()(1.0))
			
			if useRateParam:
				for category in Categories.CategoriesDict().getCategories(["et"], False)["et"]:
					self.cb.cp().channel(["et"]).bin(["et_"+category]).process(["ZTT"]).AddSyst(self.cb, "n_zll_"+category+"_norm", "rateParam", ch.SystMap()(1.0))

			# ======================================================================
			# EM channel
			self.add_processes(
					channel="em",
					categories=Categories.CategoriesDict().getCategories(["em"])["em"],
					bkg_processes=background_processes_em,
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# efficiencies
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.trigger_efficiency2016_em_syst_args)
				self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.electron_efficiency2016_syst_args)
				self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.muon_efficiency2016_syst_args)
			else:
				self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.electron_efficiency_syst_args)
				self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.muon_efficiency_syst_args)

			# B-Tag
			if year == "2016":
				self.cb.cp().channel(["em"]).process(["TT", "VV"]).bin(["em_ZeroJet2D", "em_Boosted2D", "em_Vbf2D"]).AddSyst(self.cb, *self.btag_efficiency2016_syst_args)
			
			# electron ES
			self.cb.cp().channel(["em"]).process(signal_processes+all_mc_bkgs+["QCD"]).AddSyst(self.cb, *self.ele_es_syst_args)
			
			if useRateParam:
				for category in Categories.CategoriesDict().getCategories(["em"], False)["em"]:
					self.cb.cp().channel(["em"]).bin(["em_"+category]).process(["ZTT"]).AddSyst(self.cb, "n_zll_"+category+"_norm", "rateParam", ch.SystMap()(1.0))

			# ======================================================================
			# TT channel
			self.add_processes(
					channel="tt",
					categories=Categories.CategoriesDict().getCategories(["tt"])["tt"],
					bkg_processes=background_processes_tt,
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# efficiencies
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.trigger_efficiency2016_syst_args)
				self.cb.cp().channel(["tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.tau_efficiency2016_tt_syst_args)
			else:
				self.cb.cp().channel(["tt"]).process(signal_processes+["ZTT", "TTT", "VVT"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)
			
			if useRateParam:
				for category in Categories.CategoriesDict().getCategories(["tt"], False)["tt"]:
					self.cb.cp().channel(["tt"]).bin(["tt_"+category]).process(["ZTT"]).AddSyst(self.cb, "n_zll_"+category+"_norm", "rateParam", ch.SystMap()(1.0))
			
			# ======================================================================
			# MM channel
			self.add_processes(
					channel="mm",
					categories=Categories.CategoriesDict().getCategories(["mm"])["mm"],
					bkg_processes=background_processes_mm,
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)
			
			# efficiencies
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["mm"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.muon_efficiency2016_syst_args)
			else:
				self.cb.cp().channel(["mm"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.muon_efficiency_syst_args)
			
			if useRateParam:
				for category in Categories.CategoriesDict().getCategories(["mm"], False)["mm"]:
					self.cb.cp().channel(["mm"]).bin(["mm_"+category]).process(["ZLL"]).AddSyst(self.cb, "n_zll_"+category+"_norm", "rateParam", ch.SystMap()(1.0))

			# ======================================================================
			# All channels

			# lumi
			# (hopefully) temporary fix
			# TODO: update processes once MM and TT fits are implemented
			if year == "2016":
				self.cb.cp().process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.lumi2016_syst_args)
				self.cb.cp().process(["W"]).channel(["em", "tt", "mm"]).AddSyst(self.cb, *self.lumi2016_syst_args) # automatically in other channels determined
			else:
				self.cb.cp().process(signal_processes+all_mc_bkgs_no_W).AddSyst(self.cb, *self.lumi_syst_args)
				self.cb.cp().process(["W"]).channel(["em", "tt", "mm"]).AddSyst(self.cb, *self.lumi_syst_args) # automatically in other channels determined
			
			# cross section
			self.cb.cp().process(["ZTT", "ZL", "ZJ", "ZLL"]).AddSyst(self.cb, *self.ztt_cross_section_syst_args)
			self.cb.cp().process(["TT", "TTT", "TTJJ"]).channel(["mt", "et", "em", "tt"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args) # automatically in other channels determined
			if year == "2016":
				self.cb.cp().process(["VV", "VVT", "VVJ"]).AddSyst(self.cb, *self.vv_cross_section2016_syst_args)
			else:
				self.cb.cp().process(["VV", "VVT", "VVJ"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["W"]).channel(["em"]).AddSyst(self.cb, "CMS_htt_jetFakeLep_13TeV", "lnN", ch.SystMap()(1.20)) # automatically in other channels determined
			self.cb.cp().process(["W"]).channel(["tt", "mm"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# tau efficiency
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["mt", "et"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.tau_efficiency2016_corr_syst_args)
				self.cb.cp().channel(["tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, *self.tau_efficiency2016_tt_corr_syst_args)
			else:
				self.cb.cp().channel(["mt", "et", "tt"]).process(signal_processes+["ZTT", "TTT", "VVT"]).AddSyst(self.cb, *self.tau_efficiency_corr_syst_args)

			# tau ES
			self.cb.cp().channel(["mt", "et", "tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, "CMS_scale_t_1prong_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["mt", "et", "tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, "CMS_scale_t_1prong1pizero_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["mt", "et", "tt"]).process(signal_processes+all_mc_bkgs).AddSyst(self.cb, "CMS_scale_t_3prong_13TeV", "shape", ch.SystMap()(1.0))

			# jet ES
			# TODO: use mix of lnN/shape systematics as done in official analysis?
			for jecUncert in jecUncertNames:
				self.cb.cp().process(signal_processes+all_mc_bkgs+["QCD"]).bin([channel+"_"+category for channel in ["et", "mt", "tt", "em"] for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "CMS_scale_j_"+jecUncert+"_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["mt"]).process(signal_processes+all_mc_bkgs).bin(["mt_ZeroJet2D_WJCR", "mt_Boosted2D_WJCR", "mt_ZeroJet2D_QCDCR", "mt_Boosted2D_QCDCR"]).AddSyst(self.cb, "CMS_scale_j_"+jecUncert+"_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs).bin(["et_ZeroJet2D_WJCR", "et_Boosted2D_WJCR", "et_Boosted2D_QCDCR"]).AddSyst(self.cb, "CMS_scale_j_"+jecUncert+"_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["et"]).process(signal_processes+all_mc_bkgs_no_TTJ).bin(["et_ZeroJet2D_QCDCR"]).AddSyst(self.cb, "CMS_scale_j_"+jecUncert+"_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["tt"]).process(signal_processes+all_mc_bkgs).bin(["tt_ZeroJet2D_QCDCR", "tt_Boosted2D_QCDCR", "tt_Vbf2D_QCDCR"]).AddSyst(self.cb, "CMS_scale_j_"+jecUncert+"_13TeV", "shape", ch.SystMap()(1.0))
			
			# jet->tau fake ES
			if year == "2016":
				self.cb.cp().channel(["et", "mt", "tt"]).process(["ZJ", "TTJJ", "VVJ"]).AddSyst(self.cb, "CMS_htt_jetToTauFake_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["et", "mt", "tt"]).process(["W"]).bin([channel+"_"+category for channel in ["et", "mt", "tt"] for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "CMS_htt_jetToTauFake_13TeV", "shape", ch.SystMap()(1.0))
				self.cb.cp().channel(["et", "mt"]).process(["W"]).bin([channel+"_"+category for channel in ["et", "mt"] for category in ["ZeroJet2D_QCDCR", "Boosted2D_QCDCR"]]).AddSyst(self.cb, "CMS_htt_jetToTauFake_13TeV", "shape", ch.SystMap()(1.0))
			else:
				self.cb.cp().channel(["et", "mt", "tt"]).process(["ZJ", "W", "TTJJ", "VVJ"]).AddSyst(self.cb, *self.jetFakeTau_syst_args)
			
			# MET ES
			self.cb.cp().channel(["et", "mt", "tt", "em"]).process(signal_processes+all_mc_bkgs).bin([channel+"_"+category for channel in ["et", "mt", "tt", "em"] for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "CMS_scale_met_clustered_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et", "mt", "tt", "em"]).process(signal_processes+all_mc_bkgs).bin([channel+"_"+category for channel in ["et", "mt", "tt", "em"] for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "CMS_scale_met_unclustered_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et", "mt"]).process(all_mc_bkgs).bin([channel+"_"+category for channel in ["et", "mt"] for category in ["ZeroJet2D_WJCR", "ZeroJet2D_QCDCR", "Boosted2D_WJCR", "Boosted2D_QCDCR"]]).AddSyst(self.cb, "CMS_scale_met_clustered_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et", "mt"]).process(all_mc_bkgs).bin([channel+"_"+category for channel in ["et", "mt"] for category in ["ZeroJet2D_WJCR", "ZeroJet2D_QCDCR", "Boosted2D_WJCR", "Boosted2D_QCDCR"]]).AddSyst(self.cb, "CMS_scale_met_unclustered_13TeV", "shape", ch.SystMap()(1.0))
			
			# QCD normalization from https://github.com/cms-analysis/CombineHarvester/blob/SM2016-dev/HTTSM2016/src/HttSystematics_SMRun2.cc#L1393-L1415
			self.cb.cp().channel(["em"]).process(["QCD"]).bin(["em_ZeroJet2D"]).AddSyst(self.cb, "CMS_htt_QCD_0jet_em_13TeV", "lnN", ch.SystMap()(1.10))
			self.cb.cp().channel(["em"]).process(["QCD"]).bin(["em_Boosted2D"]).AddSyst(self.cb, "CMS_htt_QCD_boosted_em_13TeV", "lnN", ch.SystMap()(1.10))
			self.cb.cp().channel(["em"]).process(["QCD"]).bin(["em_Vbf2D"]).AddSyst(self.cb, "CMS_htt_QCD_VBF_em_13TeV", "lnN", ch.SystMap()(1.20))
			
			self.cb.cp().channel(["tt"]).process(["QCD"]).bin(["tt_ZeroJet2D"]).AddSyst(self.cb, "CMS_htt_QCD_0jet_tt_13TeV", "lnN", ch.SystMap()(1.027))
			self.cb.cp().channel(["tt"]).process(["QCD"]).bin(["tt_Boosted2D"]).AddSyst(self.cb, "CMS_htt_QCD_boosted_tt_13TeV", "lnN", ch.SystMap()(1.027))
			self.cb.cp().channel(["tt"]).process(["QCD"]).bin(["tt_Vbf2D"]).AddSyst(self.cb, "CMS_htt_QCD_VBF_tt_13TeV", "lnN", ch.SystMap()(1.15))
			
			self.cb.cp().channel(["mt"]).process(["QCD"]).bin(["mt_"+category for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "QCD_Extrap_Iso_nonIso_mt_13TeV", "lnN", ch.SystMap()(1.20))
			self.cb.cp().channel(["et"]).process(["QCD"]).bin(["et_"+category for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "QCD_Extrap_Iso_nonIso_et_13TeV", "lnN", ch.SystMap()(1.20))
			
			self.cb.cp().channel(["et", "mt"]).process(["QCD"]).bin([channel+"_ZeroJet2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WSFUncert_$CHANNEL_0jet_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et", "mt"]).process(["QCD"]).bin([channel+"_Boosted2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WSFUncert_$CHANNEL_boosted_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().channel(["et", "mt"]).process(["QCD"]).bin([channel+"_Vbf2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WSFUncert_$CHANNEL_vbf_13TeV", "shape", ch.SystMap()(1.0))
			
			self.cb.cp().channel(["et", "mt"]).process(["W"]).bin([channel+"_ZeroJet2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WHighMTtoLowMT_0jet_13TeV", "lnN", ch.SystMap()(1.10))
			self.cb.cp().channel(["et", "mt"]).process(["W"]).bin([channel+"_Boosted2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WHighMTtoLowMT_boosted_13TeV", "lnN", ch.SystMap()(1.05))
			self.cb.cp().channel(["et", "mt"]).process(["W"]).bin([channel+"_Vbf2D" for channel in ["et", "mt"]]).AddSyst(self.cb, "WHighMTtoLowMT_vbf_13TeV", "lnN", ch.SystMap()(1.10))
			
			# ttbar shape
			self.cb.cp().channel(["et", "mt", "em", "tt"]).process(["TTT", "TTJJ"]).AddSyst(self.cb, *self.ttj_syst_args)
			self.cb.cp().channel(["em"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)
			
			# dy shape
			self.cb.cp().channel(["et", "mt", "tt"]).process(["ZTT", "ZL", "ZJ"]).AddSyst(self.cb, *self.dy_shape_syst_args)
			self.cb.cp().channel(["em"]).process(["ZTT", "ZLL"]).AddSyst(self.cb, *self.dy_shape_syst_args)
			
			# ======================================================================
			# Theory uncertainties
			self.cb.cp().channel(["mt", "et", "tt", "em"]).process(["ggH"]).bin([channel+"_"+category for channel in ["et", "mt", "em", "tt"] for category in ["ZeroJet2D", "Boosted2D", "Vbf2D"]]).AddSyst(self.cb, "CMS_scale_gg_13TeV", "shape", ch.SystMap()(1.0))
			self.cb.cp().process(["qqH"]).AddSyst(self.cb, *self.htt_qcd_scale_qqh_syst_args)
			self.cb.cp().process(["ggH", "qqH"]).AddSyst(self.cb, *self.htt_pdf_scale_smhtt_syst_args)
			self.cb.cp().process(["ggH", "qqH"]).AddSyst(self.cb, *self.htt_ueps_smhtt_syst_args)
			
			# Uncertainty on BR of HTT @ 125 GeV
			self.cb.cp().signals().AddSyst(self.cb, "BR_htt_THU", "lnN", ch.SystMap()(1.017))
			self.cb.cp().signals().AddSyst(self.cb, "BR_htt_PU_mq", "lnN", ch.SystMap()(1.0099))
			self.cb.cp().signals().AddSyst(self.cb, "BR_htt_PU_alphas", "lnN", ch.SystMap()(1.0062))
			
			# Uncertainty on BR of HWW @ 125 GeV
			self.cb.cp().process(["hww_gg125", "hww_qq125"]).AddSyst(self.cb, "BR_hww_THU", "lnN", ch.SystMap()(1.0099))
			self.cb.cp().process(["hww_gg125", "hww_qq125"]).AddSyst(self.cb, "BR_hww_PU_mq", "lnN", ch.SystMap()(1.0099))
			self.cb.cp().process(["hww_gg125", "hww_qq125"]).AddSyst(self.cb, "BR_hww_PU_alphas", "lnN", ch.SystMap()(1.0066))
			
			self.cb.cp().process(["ggH", "hww_gg125"]).AddSyst(self.cb, "QCDScale_ggH", "lnN", ch.SystMap()(1.039))
			self.cb.cp().process(["qqH", "hww_qq125"]).AddSyst(self.cb, "QCDScale_qqH", "lnN", ch.SystMap()(1.004))
			self.cb.cp().process(["WH"]).AddSyst(self.cb, "QCDScale_VH", "lnN", ch.SystMap()(1.007))
			self.cb.cp().process(["ZH"]).AddSyst(self.cb, "QCDScale_VH", "lnN", ch.SystMap()(1.038))
			
			self.cb.cp().process(["ggH", "hww_gg125"]).AddSyst(self.cb, "pdf_Higgs_gg", "lnN", ch.SystMap()(1.032))
			self.cb.cp().process(["qqH", "hww_qq125"]).AddSyst(self.cb, "pdf_Higgs_qq", "lnN", ch.SystMap()(1.021))
			self.cb.cp().process(["WH"]).AddSyst(self.cb, "pdf_Higgs_VH", "lnN", ch.SystMap()(1.019))
			self.cb.cp().process(["ZH"]).AddSyst(self.cb, "pdf_Higgs_VH", "lnN", ch.SystMap()(1.016))
			
			# ======================================================================

			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()


# simplified version just for the purpose of datacard synchronization (no systematics)
class SMHttDatacardsForSync(datacards.Datacards):
	def __init__(self, higgs_masses=["125"], cb=None):
		super(SMHttDatacardsForSync, self).__init__(cb)

		if cb is None:
			signal_processes = []

			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["inclusivemt40"]],
					bkg_processes=["ZTT", "ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=["et_"+category for category in ["inclusivemt40"]],
					bkg_processes=["ZTT", "ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# ======================================================================
			# EM channel
			self.add_processes(
					channel="em",
					categories=["em_"+category for category in []],
					bkg_processes=["ZTT", "ZLL", "TT", "VV", "W", "QCD"],
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			# ======================================================================
			# TT channel
			self.add_processes(
					channel="tt",
					categories=["tt_"+category for category in []],
					bkg_processes=["ZTT", "ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=signal_processes,
					analysis=["htt"],
					era=["13TeV"],
					mass=higgs_masses
			)

			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()
