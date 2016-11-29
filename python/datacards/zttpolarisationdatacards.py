# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import CombineHarvester.CombineTools.ch as ch

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards


class ZttPolarisationDatacards(datacards.Datacards):
	def __init__(self, cb=None):
		super(ZttPolarisationDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["x_a1", "x_rho", "x_oneprong"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTTPOSPOL", "ZTTNEGPOL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["0"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.muon_efficiency_syst_args)
			
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_corr_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)
			#self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)
			
			# from Yuta
			self.cb.cp().channel(["mt"]).process(["ZL", "ZJ", "W"]).AddSyst(self.cb, *self.boson_scale_met_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL", "ZJ", "W"]).AddSyst(self.cb, *self.boson_resolution_met_syst_args)
			self.cb.cp().channel(["mt"]).process(["TT", "VV"]).AddSyst(self.cb, *self.ewk_top_scale_met_syst_args)
			self.cb.cp().channel(["mt"]).process(["TT", "VV"]).AddSyst(self.cb, *self.ewk_top_resolution_met_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_extrapol_syst_args)
			self.cb.cp().channel(["mt"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Tau ES
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZJ"]).AddSyst(self.cb, *self.zjFakeTau_syst_args)
			
			# Top pT reweight
			#self.cb.cp().channel(["mt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)
		
			# ======================================================================
			# ET channel
			self.add_processes(
					channel="et",
					categories=["et_"+category for category in ["x_a1", "x_rho", "x_oneprong"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTTPOSPOL", "ZTTNEGPOL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["0"]
			)
		
			# efficiencies
			self.cb.cp().channel(["et"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.electron_efficiency_syst_args)
			
			self.cb.cp().channel(["et"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_corr_syst_args)
			self.cb.cp().channel(["et"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)
			#self.cb.cp().channel(["et"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_extrapol_syst_args)
			self.cb.cp().channel(["et"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Tau ES
			self.cb.cp().channel(["et"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_tight_syst_args)
			self.cb.cp().channel(["et"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			self.cb.cp().channel(["et"]).process(["ZJ"]).AddSyst(self.cb, *self.zjFakeTau_syst_args)
			
			# Top pT reweight
			#self.cb.cp().channel(["et"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)
		
			# ======================================================================
			# TT channel
			self.add_processes(
					channel="tt",
					categories=["tt_"+category for category in ["a1_x", "rho_x", "oneprong_x", "x_a1", "x_rho"]],
					bkg_processes=["ZL", "ZJ", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTTPOSPOL", "ZTTNEGPOL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["0"]
			)
		
			# efficiencies
			self.cb.cp().channel(["tt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_corr_syst_args)
			self.cb.cp().channel(["tt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)
			#self.cb.cp().channel(["tt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_efficiency_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_extrapol_syst_args)
			self.cb.cp().channel(["tt"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# Tau ES
			self.cb.cp().channel(["tt"]).process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.tau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["tt"]).process(["ZL"]).AddSyst(self.cb, *self.eFakeTau_tight_syst_args)
			self.cb.cp().channel(["tt"]).process(["ZL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)
			self.cb.cp().channel(["tt"]).process(["ZJ"]).AddSyst(self.cb, *self.zjFakeTau_syst_args)
			
			# Top pT reweight
			#self.cb.cp().channel(["tt"]).process(["TT"]).AddSyst(self.cb, *self.ttj_syst_args)

			# ======================================================================
			# All channels
			#self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, "ZTTPOSPOL_uniform_2", "ZTTNEGPOL_uniform_2", "lnU", ch.SystMap()(2.0))
		
			# lumi
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL", "ZL", "ZJ", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)
		
			# cross section
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL", "ZL", "ZJ"]).AddSyst(self.cb, *self.zll_cross_section_syst_args)
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# signal acceptance/efficiency
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)

			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_inclusive_args)
			
			# ======================================================================
			# Groups of systematics
			self.cb.SetGroup("syst", [".*"])
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()

