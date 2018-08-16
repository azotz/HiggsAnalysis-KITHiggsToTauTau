# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re


class TauES(dict):
	def __init__(self, nickname):
		if re.search("(Spring16|Summer16)",nickname):
			self["TauEnergyCorrection"] = "smhtt2016"
			self["TauEnergyCorrectionOneProng"] = 0.982
			self["TauEnergyCorrectionOneProngPiZeros"] = 1.01
			self["TauEnergyCorrectionThreeProng"] = 1.004
		elif re.search("(Summer17|Fall17)",nickname):
			#https://indico.cern.ch/event/738043/contributions/3048471/attachments/1674773/2688351/TauId_26062018.pdf 
			self["TauEnergyCorrection"] = "smhtt2016"
			self["TauEnergyCorrectionOneProng"] = 0.970 #+-3%  
			self["TauEnergyCorrectionOneProngPiZeros"] = 0.98 #+-3%
			self["TauEnergyCorrectionThreeProng"] = 0.99 #+-3%
			self["TauElectronFakeEnergyCorrectionOneProng"] = 1.0
			self["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.0
		else:
			self["TauEnergyCorrection"] = "none"
		
			self["TauEnergyCorrectionOneProng"] = 0.982
			self["TauEnergyCorrectionOneProngPiZeros"] = 1.01
			self["TauEnergyCorrectionThreeProng"] = 1.004
			
		if re.search("(DY.?JetsToLL|EWKZ2Jets|LFV).*(?=(Spring16|Summer16))", nickname):
			self["TauElectronFakeEnergyCorrectionOneProng"] = 1.0
			self["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.095
			self["TauElectronFakeEnergyCorrectionThreeProng"] = 1.0
			self["TauMuonFakeEnergyCorrectionOneProng"] = 0.998
			self["TauMuonFakeEnergyCorrectionOneProngPiZeros"] = 1.015
			self["TauMuonFakeEnergyCorrectionThreeProng"] = 1.0

