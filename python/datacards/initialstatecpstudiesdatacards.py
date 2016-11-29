# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import HiggsAnalysis.KITHiggsToTauTau.plotting.configs.categories as Categories
import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards
import HiggsAnalysis.KITHiggsToTauTau.datacards.smhttdatacards as smhttdatacards
import CombineHarvester.CombineTools.ch as ch

class InitialStateCPStudiesDatacards(smhttdatacards.SMHttDatacards):
	def __init__(self, higgs_masses=["125"], useRateParam=False, year="", cb=None, signal_processes=[ "qqH", "WH", "ZH","ggHsm","ggHmm","ggHps"]):
		super(InitialStateCPStudiesDatacards, self).__init__(higgs_masses,useRateParam,year,cb, signal_processes=["qqH", "WH", "ZH","ggHsm","ggHmm","ggHps"])
		
		self.cb.cp().signals().ForEachProc(lambda process: process.set_signal(False if process.process() in ["qqH", "WH", "ZH"] else True) )
		self.cb.cp().process(["qqH", "WH", "ZH"]).ForEachSyst(lambda systematic: systematic.set_signal(False) )
		self.cb.cp().backgrounds().ForEachProc(lambda process: process.set_mass("*"))
		self.cb.cp().backgrounds().ForEachSyst(lambda systematic: systematic.set_mass("*"))
		#self.cb.cp().signals().ForEachProc(lambda process: process.set_process("ggHps_alt","ggHps")
		#self.cb.PrintAll()
