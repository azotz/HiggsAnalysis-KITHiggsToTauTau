# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import CombineHarvester.CombineTools.ch as ch

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards


class TauEsDatacards(datacards.Datacards):
	def __init__(self, shifts=[], decaymodes=[], pt_bins=[], year="", cb=None):
		super(TauEsDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category+"_"+decaymode+"_ptbin"+pt_bin for category in ["inclusive"] for decaymode in decaymodes for pt_bin in pt_bins],
					bkg_processes=["ZLL", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTT"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=shifts
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZTT", "ZLL", "TT", "VV"]).AddSyst(self.cb, *self.muon_efficiency_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficiency_corr_syst_args)
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, "CMS_eff_t_mt_13TeV", "lnN", ch.SystMap()(1.10))
			else:
				self.cb.cp().channel(["mt"]).process(["ZTT", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)

			# extrapolation uncertainty
			#self.cb.cp().channel(["mt"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# mu->tau fake ES
			self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.muFakeTau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# b-tag efficiency and mistag
			self.cb.cp().channel(["mt"]).process(["ZTT", "ZLL", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.btag_efficiency_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTT", "ZLL", "TT", "VV", "W", "QCD"]).AddSyst(self.cb, *self.btag_mistag_syst_args)

			# ======================================================================
			# All channels
			#self.cb.cp().process(["ZTT"]).AddSyst(self.cb, "ZTT_uniform_2", "lnU", ch.SystMap()(2.0))
		
			# lumi
			# (hopefully) temporary fix
			if year == "2016":
				self.cb.cp().channel(["mt"]).process(["ZTT", "ZLL", "TT", "VV"]).AddSyst(self.cb, "lumi_13TeV", "lnN", ch.SystMap()(1.062))
			else:
				self.cb.cp().process(["ZTT", "ZLL", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)

			# cross section
			self.cb.cp().process(["ZLL"]).AddSyst(self.cb, *self.zll_cross_section_syst_args)
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			#self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# signal acceptance/efficiency
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTT"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)

			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_inclusive_args)
			
			# transform B-Tagging shape to lnN
			self.cb.cp().syst_name(['CMS_eff_b_13TeV']).ForEachSyst(lambda x: x.set_type("lnN"))
			self.cb.cp().syst_name(['CMS_mistag_b_13TeV']).ForEachSyst(lambda x: x.set_type("lnN"))
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()
