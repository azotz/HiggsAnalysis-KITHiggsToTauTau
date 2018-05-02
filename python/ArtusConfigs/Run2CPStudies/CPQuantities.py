# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re

import HiggsAnalysis.KITHiggsToTauTau.ArtusConfigs.Run2Analysis.Run2Quantities as run2_quantities

import HiggsAnalysis.KITHiggsToTauTau.ArtusConfigs.Includes.IncludeQuantities as iq

class quantities(run2_quantities.quantities):

	def __init__(self):
		self["Quantities"]=[]
	def build_quantities(self, nickname, *args, **kwargs):
		
		self["Quantities"] += self.fourVectorQuantities()
		self["Quantities"] += self.syncQuantities()
		self["Quantities"] += self.weightQuantities()

		if re.search("Run2015", nickname):  					
			self["Quantities"] += self.recoPolarisationQuantities() 	
			
		elif re.search("(DY.?JetsToLL).*(?=(Spring16|Summer16|Summer17|Fall17))", nickname):
			self["Quantities"] += self.svfitSyncQuantities()
			if re.search("(Run2017|Summer17|Fall17)", nickname) == None:	 
				self["Quantities"] += self.splitJecUncertaintyQuantities()
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.genMatchedCPQuantities()
			self["Quantities"] += self.recoCPQuantities()
			self["Quantities"] += self.melaQuantities()
			self["Quantities"] += self.recoPolarisationQuantities()
			self["Quantities"] += self.recoPolarisationQuantitiesSvfit()
			if kwargs.get("channel", None) != "EM":
				self["Quantities"] += iq.SingleTauQuantities()	
			
		
		elif re.search("(HToTauTau|H2JetsToTauTau|Higgs).*(?=(Spring16|Summer16|Summer17|Fall17))", nickname):
			self["Quantities"] += self.svfitSyncQuantities()
			if re.search("(Run2017|Summer17|Fall17)", nickname) == None:	 
				self["Quantities"] += self.splitJecUncertaintyQuantities()
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.genHiggsQuantities()
			self["Quantities"] += self.genMatchedCPQuantities()
			self["Quantities"] += self.recoCPQuantities()
			self["Quantities"] += self.melaQuantities()
			
		elif re.search("^((?!(DY.?JetsToLL|HToTauTau|H2JetsToTauTau|Higgs)).)*Fall15", nickname):
			self["Quantities"] += self.recoPolarisationQuantities()
			
		elif re.search("(DY.?JetsToLL).*(?=Fall15)", nickname):
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.genMatchedCPQuantities()
			self["Quantities"] += self.recoPolarisationQuantities()

		elif re.search("(HToTauTau|H2JetsToTauTau|Higgs).*(?=Fall15)",nickname):   #almost the same as 2016 signal, no splitJecUncertaintyQuantities()
			self["Quantities"] += self.svfitSyncQuantities()
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.genHiggsQuantities()
			self["Quantities"] += self.genMatchedCPQuantities()
			self["Quantities"] += self.recoCPQuantities()
			self["Quantities"] += self.melaQuantities()

		elif re.search("Embedding2016", nickname):
			self["Quantities"] += self.splitJecUncertaintyQuantities()
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.recoPolarisationQuantities()
		
		elif re.search("(LFV).*(?=(Spring16|Summer16))", nickname):
			self["Quantities"] += self.splitJecUncertaintyQuantities()
			self["Quantities"] += self.genQuantities()
			self["Quantities"] += self.genQuantitiesLFV()
			if kwargs.get("channel", None) == "MT" or kwargs.get("channel", None) == "ET":
				self["Quantities"] += iq.SingleTauQuantities()	#until here
				self["Quantities"] += self.recoCPQuantities()
			elif kwargs.get("channel", None) == "EM":
				self["Quantities"] += self.recoCPQuantities()
		else:
			self["Quantities"] += self.svfitSyncQuantities()
			if re.search("(Run2017|Summer17|Fall17)", nickname) == None:	 
				self["Quantities"] += self.splitJecUncertaintyQuantities()
			self["Quantities"] += self.recoCPQuantities()
			self["Quantities"] += self.melaQuantities()
			self["Quantities"] += self.recoPolarisationQuantities()
			self["Quantities"] += self.recoPolarisationQuantitiesSvfit()


	def genCPQuantities(self, *args, **kwargs):    #TODO Is this really used, very similar to matchedcpquantities
		return [
			#"1genBosonDaughterSize",
			#"1genBoson1DaughterPt",
			#"1genBoson1DaughterPz",
			#"1genBoson1DaughterEta",
			#"1genBoson1DaughterPhi",
			#"1genBoson1DaughterMass",
			#"1genBoson1DaughterCharge",
			#"1genBoson1DaughterEnergy",
			#"1genBoson1DaughterPdgId",
			#"1genBoson1DaughterStatus",
			#"1genBoson2DaughterPt",
			#"1genBoson2DaughterPz",
			#"1genBoson2DaughterEta",
			#"1genBoson2DaughterPhi",
			#"1genBoson2DaughterMass",
			#"1genBoson2DaughterEnergy",
			#"1genBoson2DaughterPdgId",
			#"1genBoson2DaughterStatus",
			#"1genBoson1DaughterGranddaughterSize",
			#"1genBoson1Daughter1GranddaughterPt",
			#"1genBoson1Daughter1GranddaughterPz",
			#"1genBoson1Daughter1GranddaughterEta",
			#"1genBoson1Daughter1GranddaughterPhi",
			#"1genBoson1Daughter1GranddaughterMass",
			#"1genBoson1Daughter1GranddaughterEnergy",
			#"1genBoson1Daughter1GranddaughterPdgId",
			#"1genBoson1Daughter1GranddaughterStatus",
			#"1genBoson1Daughter2GranddaughterPt",
			#"1genBoson1Daughter2GranddaughterPz",
			#"1genBoson1Daughter2GranddaughterEta",
			#"1genBoson1Daughter2GranddaughterPhi",
			#"1genBoson1Daughter2GranddaughterMass",
			#"1genBoson1Daughter2GranddaughterEnergy",
			#"1genBoson1Daughter2GranddaughterPdgId",
			#"1genBoson1Daughter2GranddaughterStatus",
			#"1genBoson1Daughter3GranddaughterPt",
			#"1genBoson1Daughter3GranddaughterPz",
			#"1genBoson1Daughter3GranddaughterEta",
			#"1genBoson1Daughter3GranddaughterPhi",
			#"1genBoson1Daughter3GranddaughterMass",
			#"1genBoson1Daughter3GranddaughterEnergy",
			#"1genBoson1Daughter3GranddaughterPdgId",
			#"1genBoson1Daughter3GranddaughterStatus",
			#"1genBoson1Daughter4GranddaughterPt",
			#"1genBoson1Daughter4GranddaughterPz",
			#"1genBoson1Daughter4GranddaughterEta",
			#"1genBoson1Daughter4GranddaughterPhi",
			#"1genBoson1Daughter4GranddaughterMass",
			#"1genBoson1Daughter4GranddaughterEnergy",
			#"1genBoson1Daughter4GranddaughterPdgId",
			#"1genBoson1Daughter4GranddaughterStatus",
			#"1genBoson2DaughterGranddaughterSize",
			#"1genBoson2Daughter1GranddaughterPt",
			#"1genBoson2Daughter1GranddaughterPz",
			#"1genBoson2Daughter1GranddaughterEta",
			#"1genBoson2Daughter1GranddaughterPhi",
			#"1genBoson2Daughter1GranddaughterMass",
			#"1genBoson2Daughter1GranddaughterEnergy",
			#"1genBoson2Daughter1GranddaughterPdgId",
			#"1genBoson2Daughter1GranddaughterStatus",
			#"1genBoson2Daughter2GranddaughterPt",
			#"1genBoson2Daughter2GranddaughterPz",
			#"1genBoson2Daughter2GranddaughterEta",
			#"1genBoson2Daughter2GranddaughterPhi",
			#"1genBoson2Daughter2GranddaughterMass",
			#"1genBoson2Daughter2GranddaughterEnergy",
			#"1genBoson2Daughter2GranddaughterPdgId",
			#"1genBoson2Daughter2GranddaughterStatus",
			#"1genBoson2Daughter3GranddaughterPt",
			#"1genBoson2Daughter3GranddaughterPz",
			#"1genBoson2Daughter3GranddaughterEta",
			#"1genBoson2Daughter3GranddaughterPhi",
			#"1genBoson2Daughter3GranddaughterMass",
			#"1genBoson2Daughter3GranddaughterEnergy",
			#"1genBoson2Daughter3GranddaughterPdgId",
			#"1genBoson2Daughter3GranddaughterStatus",
			#"1genBoson2Daughter4GranddaughterPt",
			#"1genBoson2Daughter4GranddaughterPz",
			#"1genBoson2Daughter4GranddaughterEta",
			#"1genBoson2Daughter4GranddaughterPhi",
			#"1genBoson2Daughter4GranddaughterMass",
			#"1genBoson2Daughter4GranddaughterEnergy",
			#"1genBoson2Daughter4GranddaughterPdgId",
			#"1genBoson2Daughter4GranddaughterStatus",
			#"1genBoson1Daughter2GranddaughterGrandGranddaughterSize",
			#"1genBoson1Daughter2Granddaughter1GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter1GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter2GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter2GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter3GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter3GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter4GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter4GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter5GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter5GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter6GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter6GrandGranddaughterStatus",
			#"1genBoson2Daughter2GranddaughterGrandGranddaughterSize",
			"genPVx",
			"genPVy",
			"genPVz",
			"genPhiStarCP",
			"genPhiStar",
			"genOStarCP",
			"genPhiCP",
			"genPhi",
			"genOCP",
			"genPhiStarCPComb",
			"genPhiCPLab",

			"genIP1mag",
			"genIP1x",
			"genIP1y",
			"genIP1z",
		
			"genIP2mag",
			"genIP2x",
			"genIP2y",
			"genIP2z",
			"genCosPsiPlus",
			"genCosPsiMinus",
			"genPhiStarCP_rho",
			"genPhiCP_rho",
			"genPhiStar_rho",
			"genPhi_rho",
			"gen_yTau",
			"gen_posyTauL",
			"gen_negyTauL",
			"TauMProngEnergy",
			"TauPProngEnergy",
			"Tau1OneProngsSize",
			"Tau2OneProngsSize",
			"Tau1DecayMode",
			"Tau2DecayMode",
			"TauTree1DecayMode",
			"TauTree2DecayMode",
			"OneProngChargedPart1Pt",
			"OneProngChargedPart1Pz",
			"OneProngChargedPart1Eta",
			"OneProngChargedPart1Phi",
			"OneProngChargedPart1Mass",
			"OneProngChargedPart1Energy",
			"OneProngChargedPart1PdgId",
			"OneProngChargedPart2Pt",
			"OneProngChargedPart2Pz",
			"OneProngChargedPart2Eta",
			"OneProngChargedPart2Phi",
			"OneProngChargedPart2Mass",
			"OneProngChargedPart2Energy",
			"OneProngChargedPart2PdgId",
			"genZPlus",
			"genZMinus",
			"genZs"
		]

	def genHiggsQuantities(self, *args, **kwargs):
		return [
			"lheSignedDiJetDeltaPhi",
			"lheDiJetAbsDeltaEta",
			"lheDiJetMass",
			"lheNJets",
			"lheParticleIn1LV",
			"lheParticleIn2LV",
			"lheParticleOut1LV",
			"lheParticleOut2LV",
			"lheParticleBoson1LV",
			"lheParticleIn1PdgId",
			"lheParticleIn2PdgId",
			"lheParticleOut1PdgId",
			"lheParticleOut2PdgId",
			"lheParticleBoson1PdgId"
		]

	def genMatchedCPQuantities(self, *args, **kwargs):
		return [
			#"1genBosonDaughterSize",
			#"1genBoson1DaughterPt",
			#"1genBoson1DaughterPz",
			#"1genBoson1DaughterEta",
			#"1genBoson1DaughterPhi",
			#"1genBoson1DaughterMass",
			#"1genBoson1DaughterCharge",
			#"1genBoson1DaughterEnergy",
			#"1genBoson1DaughterPdgId",
			#"1genBoson1DaughterStatus",
			#"1genBoson2DaughterPt",
			#"1genBoson2DaughterPz",
			#"1genBoson2DaughterEta",
			#"1genBoson2DaughterPhi",
			#"1genBoson2DaughterMass",
			#"1genBoson2DaughterEnergy",
			#"1genBoson2DaughterPdgId",
			#"1genBoson2DaughterStatus",
			#"1genBoson1DaughterGranddaughterSize",
			#"1genBoson1Daughter1GranddaughterPt",
			#"1genBoson1Daughter1GranddaughterPz",
			#"1genBoson1Daughter1GranddaughterEta",
			#"1genBoson1Daughter1GranddaughterPhi",
			#"1genBoson1Daughter1GranddaughterMass",
			#"1genBoson1Daughter1GranddaughterEnergy",
			#"1genBoson1Daughter1GranddaughterPdgId",
			#"1genBoson1Daughter1GranddaughterStatus",
			#"1genBoson1Daughter2GranddaughterPt",
			#"1genBoson1Daughter2GranddaughterPz",
			#"1genBoson1Daughter2GranddaughterEta",
			#"1genBoson1Daughter2GranddaughterPhi",
			#"1genBoson1Daughter2GranddaughterMass",
			#"1genBoson1Daughter2GranddaughterEnergy",
			#"1genBoson1Daughter2GranddaughterPdgId",
			#"1genBoson1Daughter2GranddaughterStatus",
			#"1genBoson1Daughter3GranddaughterPt",
			#"1genBoson1Daughter3GranddaughterPz",
			#"1genBoson1Daughter3GranddaughterEta",
			#"1genBoson1Daughter3GranddaughterPhi",
			#"1genBoson1Daughter3GranddaughterMass",
			#"1genBoson1Daughter3GranddaughterEnergy",
			#"1genBoson1Daughter3GranddaughterPdgId",
			#"1genBoson1Daughter3GranddaughterStatus",
			#"1genBoson1Daughter4GranddaughterPt",
			#"1genBoson1Daughter4GranddaughterPz",
			#"1genBoson1Daughter4GranddaughterEta",
			#"1genBoson1Daughter4GranddaughterPhi",
			#"1genBoson1Daughter4GranddaughterMass",
			#"1genBoson1Daughter4GranddaughterEnergy",
			#"1genBoson1Daughter4GranddaughterPdgId",
			#"1genBoson1Daughter4GranddaughterStatus",
			#"1genBoson2DaughterGranddaughterSize",
			#"1genBoson2Daughter1GranddaughterPt",
			#"1genBoson2Daughter1GranddaughterPz",
			#"1genBoson2Daughter1GranddaughterEta",
			#"1genBoson2Daughter1GranddaughterPhi",
			#"1genBoson2Daughter1GranddaughterMass",
			#"1genBoson2Daughter1GranddaughterEnergy",
			#"1genBoson2Daughter1GranddaughterPdgId",
			#"1genBoson2Daughter1GranddaughterStatus",
			#"1genBoson2Daughter2GranddaughterPt",
			#"1genBoson2Daughter2GranddaughterPz",
			#"1genBoson2Daughter2GranddaughterEta",
			#"1genBoson2Daughter2GranddaughterPhi",
			#"1genBoson2Daughter2GranddaughterMass",
			#"1genBoson2Daughter2GranddaughterEnergy",
			#"1genBoson2Daughter2GranddaughterPdgId",
			#"1genBoson2Daughter2GranddaughterStatus",
			#"1genBoson2Daughter3GranddaughterPt",
			#"1genBoson2Daughter3GranddaughterPz",
			#"1genBoson2Daughter3GranddaughterEta",
			#"1genBoson2Daughter3GranddaughterPhi",
			#"1genBoson2Daughter3GranddaughterMass",
			#"1genBoson2Daughter3GranddaughterEnergy",
			#"1genBoson2Daughter3GranddaughterPdgId",
			#"1genBoson2Daughter3GranddaughterStatus",
			#"1genBoson2Daughter4GranddaughterPt",
			#"1genBoson2Daughter4GranddaughterPz",
			#"1genBoson2Daughter4GranddaughterEta",
			#"1genBoson2Daughter4GranddaughterPhi",
			#"1genBoson2Daughter4GranddaughterMass",
			#"1genBoson2Daughter4GranddaughterEnergy",
			#"1genBoson2Daughter4GranddaughterPdgId",
			#"1genBoson2Daughter4GranddaughterStatus",
			#"1genBoson1Daughter2GranddaughterGrandGranddaughterSize",
			#"1genBoson1Daughter2Granddaughter1GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter1GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter2GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter2GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter3GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter3GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter4GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter4GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter5GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter5GrandGranddaughterStatus",
			#"1genBoson1Daughter2Granddaughter6GrandGranddaughterPdgId",
			#"1genBoson1Daughter2Granddaughter6GrandGranddaughterStatus",
			#"1genBoson2Daughter2GranddaughterGrandGranddaughterSize",
			"genQ_1",
			"genQ_2",
			"genPVx",
			"genPVy",
			"genPVz",
			"genSV1x",
			"genSV1y",
			"genSV1z",
			"genSV2x",
			"genSV2y",
			"genSV2z",

			"genD01",
			"genD02",
		
			"genIP1mag",
			"genIP1x",
			"genIP1y",
			"genIP1z",
		
			"genIP2mag",
			"genIP2x",
			"genIP2y",
			"genIP2z",
			"genCosPsiPlus",
			"genCosPsiMinus",
			"genPhiStarCP",
			"genPhiStar",
			"genOStarCP",
			"genPhiStarCPComb",
			"genPhiStarCP_rho",
			"gen_posyTauL",
			"gen_negyTauL",
			"TauMProngEnergy",
			"TauPProngEnergy",
			"Tau1OneProngsSize",
			"Tau2OneProngsSize",
			"OneProngChargedPart1Pt",
			"OneProngChargedPart1Pz",
			"OneProngChargedPart1Eta",
			"OneProngChargedPart1Phi",
			"OneProngChargedPart1Mass",
			"OneProngChargedPart1Energy",
			"OneProngChargedPart1PdgId",
			"OneProngChargedPart2Pt",
			"OneProngChargedPart2Pz",
			"OneProngChargedPart2Eta",
			"OneProngChargedPart2Phi",
			"OneProngChargedPart2Mass",
			"OneProngChargedPart2Energy",
			"OneProngChargedPart2PdgId",
			"genZPlus",
			"genZMinus",
			"genZs",
			"d0s_area",
			"d0s_dist"
		]

	def genQuantities(self, *args, **kwargs):
		return [
			"genBosonLV",
			"genBosonParticleFound",
			"genBosonLVFound",
			"genBosonLep1LV",
			"genBosonTau1LV",
			"genBosonTau1VisibleLV",
			"genBosonTau1DecayMode",
			"genBosonTau1NProngs",
			"genBosonTau1NPi0s",
			"genBosonLep2LV",
			"genBosonTau2LV",
			"genBosonTau2VisibleLV",
			"genBosonTau2DecayMode",
			"genBosonTau2NProngs",
			"genBosonTau2NPi0s",
			"genDiLeptonDecayMode",
			"isZEE",
			"isZMM",
			"isZTT",
			"genTauTauDecayMode",
			"isZtt",
			"isZmt",
			"isZet",
			"isZem",
			"isZmm",
			"isZee",
			"npartons"
		]

	def genQuantitiesLFV(self, *args, **kwargs):
		return [
			"genBosonLV",
			"genBosonParticleFound",
			"genBosonLVFound",
			"genBosonLep1LV",
			"genBosonTau1LV",
			"genBosonTau1VisibleLV",
			"genBosonTau1DecayMode",
			"genBosonTau1NProngs",
			"genBosonTau1NPi0s",
			"genBosonLep2LV",
			"genBosonTau2LV",
			"genBosonTau2VisibleLV",
			"genBosonTau2DecayMode",
			"genBosonTau2NProngs",
			"genBosonTau2NPi0s",
			"genDiLeptonDecayMode",
			"isZEE",
			"isZMM",
			"isZTT",
			"genTauTauDecayMode",
			"isZtt",
			"isZmt",
			"isZet",
			"isZem",
			"isZmm",
			"isZee",
			"genDiLeptonDecayModeLFV",
			"isZET",
			"isZEM",
			"isZMT",
			"genTauDecayMode",
			"isZmt",
			"isZet",
			"isZem",
			"isZmm",
			"isZee",
			"lheDiLeptonDecayMode",
			"lheZtoEE",
			"lheZtoMM",
			"lheZtoTT",
			"lheZtoEM",
			"lheZtoET",
			"lheZtoMT",
			"LHE_p_1",
			"LHE_p_2"
		]

	def recoCPQuantities(self, *args, **kwargs):
		return [
			"thePVx",
			"thePVy",
			"thePVz",
			"thePVchi2",
			"thePVnDOF",
			"thePVnTracks",
			"thePVsigmaxx",
			"thePVsigmayy",
			"thePVsigmazz",
			"thePVsigmaxy",
			"thePVsigmaxz",
			"thePVsigmayz",

			"refitPVx",
			"refitPVy",
			"refitPVz",
			"refitPVchi2OverNdof",
			"refitPVnTracks",
			"refitPVsigmaxx",
			"refitPVsigmayy",
			"refitPVsigmazz",
			"refitPVsigmaxy",
			"refitPVsigmaxz",
			"refitPVsigmayz",

			"refitPVBSx",
			"refitPVBSy",
			"refitPVBSz",
			"refitPVBSchi2OverNdof",
			"refitPVBSnTracks",
			"refitPVBSsigmaxx",
			"refitPVBSsigmayy",
			"refitPVBSsigmazz",
			"refitPVBSsigmaxy",
			"refitPVBSsigmaxz",
			"refitPVBSsigmayz",

			"theBSx",
			"theBSy",
			"theBSz",
			"theBSsigmax",
			"theBSsigmay",
			"theBSsigmaz",

			"refP1x",
			"refP1y",
			"refP1z",
			"refP2x",
			"refP2y",
			"refP2z",
		
			"lep1TrackChi2OverNdof",
			"lep1TrackNInnerHits",
			"lep1TrackIsLooseQuality",
			"lep1TrackIsTightQuality",
			"lep1TrackIsHighPurityQuality",
		
			"lep2TrackChi2OverNdof",
			"lep2TrackNInnerHits",
			"lep2TrackIsLooseQuality",
			"lep2TrackIsTightQuality",
			"lep2TrackIsHighPurityQuality",

			"track1p4x",
			"track1p4y",
			"track1p4z",
			"track2p4x",
			"track2p4y",
			"track2p4z",

			"d3D_refitPV_1",
			"err3D_refitPV_1",
			"d2D_refitPV_1",
			"err2D_refitPV_1",
			"d3D_refitPV_2",
			"err3D_refitPV_2",
			"d2D_refitPV_2",
			"err2D_refitPV_2",

			"errD0_1",
			"errD0_1_newErr",
			"errD0_2",
			"errD0_2_newErr",

			"errDZ_1",
			"errDZ_1_newErr",
			"errDZ_2",
			"errDZ_2_newErr",

			"errIP_1",
			"errIP_2",

			"errD0_refitPV_1",
			"errD0_refitPV_2",

			"errDZ_refitPV_1",
			"errDZ_refitPV_2",

			"errIP_refitPV_1",
			"errIP_refitPV_2",

			"IP_1mag",
			"IP_1x",
			"IP_1y",
			"IP_1z",
			"IP_2mag",
			"IP_2x",
			"IP_2y",
			"IP_2z",

			"IP_refitPV_1mag",
			"IP_refitPV_1x",
			"IP_refitPV_1y",
			"IP_refitPV_1z",
			"IP_refitPV_2mag",
			"IP_refitPV_2x",
			"IP_refitPV_2y",
			"IP_refitPV_2z",

			"trackFromBS_1mag",
			"trackFromBS_1x",
			"trackFromBS_1y",
			"trackFromBS_1z",
			"trackFromBS_2mag",
			"trackFromBS_2x",
			"trackFromBS_2y",
			"trackFromBS_2z",

			"cosPsiPlus",
			"cosPsiMinus",

			"deltaEtaGenRecoIP1",
			"deltaEtaGenRecoIP2",
			"deltaPhiGenRecoIP1",
			"deltaPhiGenRecoIP2",
			"deltaRGenRecoIP1",
			"deltaRGenRecoIP2",
			"deltaGenRecoIP1",
			"deltaGenRecoIP2",

			"deltaEtaGenRecoIP1_refitPV",
			"deltaEtaGenRecoIP2_refitPV",
			"deltaPhiGenRecoIP1_refitPV",
			"deltaPhiGenRecoIP2_refitPV",
			"deltaRGenRecoIP1_refitPV",
			"deltaRGenRecoIP2_refitPV",
			"deltaGenRecoIP1_refitPV",
			"deltaGenRecoIP2_refitPV",

			#"recoPhiStarCP",
			#"recoPhiStarCPrPV2",
			#"recoPhiStarCPrPV_rho",
			#"recoPhiStarCPrPVbs",
			#"recoPhiStarCPrPVbs_rho",

			"recoPhiStarCP_rho",
			"recoPhiStarCP_rho_merged",
			"recoPhiStarCPrPV",
			"recoPhiStarCPComb",
			"recoPhiStarCPCombMerged",

			"recoPhiPlus_ipmeth",
			"recoPhiMinus_ipmeth",
			"recoPhiStarPlus_ipmeth",
			"recoPhiStarMinus_ipmeth",
			"recoPhiPlus_combmeth",
			"recoPhiMinus_combmeth",
			"recoPhiStarPlus_combmeth",
			"recoPhiStarMinus_combmeth",
			"recoPhiPlus_rhometh",
			"recoPhiMinus_rhometh",
			"recoPhiStarPlus_rhometh",
			"recoPhiStarMinus_rhometh",

			"recoPhiStar",
			"recoPhiStar_rho",
			"recoChargedHadron1HiggsFrameEnergy",
			"recoChargedHadron2HiggsFrameEnergy",

			"reco_posyTauL",
			"reco_negyTauL",

			"posLepSumChargedHadronsLV",
			"negLepSumChargedHadronsLV",
			"posLepSumNeutralHadronsLV",
			"negLepSumNeutralHadronsLV",

			"d0_refitPV_1",
			"d0_refitPVBS_1",
			"dZ_refitPV_1",
			"dZ_refitPVBS_1",
			"d0_refitPV_2",
			"d0_refitPVBS_2",
			"dZ_refitPV_2",
			"dZ_refitPVBS_2",
			#"recoImpactParameter1",
			#"recoImpactParameter2",

			"recoTrackRefError1",
			"recoTrackRefError2",

			"d0s_area",
			"d0s_dist"
		]

	def recoCPQuantitiesHiggs(self, *args, **kwargs):
		return [
			"madGraphLheParticle1LV",
			"madGraphLheParticle2LV",
			"madGraphLheParticle3LV",
			"madGraphLheParticle4LV",
			"madGraphLheParticle5LV",
			"madGraphLheParticle6LV",
			"madGraphLheParticle1PdgId",
			"madGraphLheParticle2PdgId",
			"madGraphLheParticle3PdgId",
			"madGraphLheParticle4PdgId",
			"madGraphLheParticle5PdgId",
			"madGraphLheParticle6PdgId",
			"subProcessCode",
			"lheParticleJetNumber"
		]

	def recoPolarisationQuantities(self, *args, **kwargs):
		return [
			"lep1SumChargedHadronsLV",
			"lep1SumNeutralHadronsLV",

			"genMatchedTau1LV",
			"genMatchedTau1Found",
			"genMatchedTau1VisibleLV",
			"genMatchedTau1DecayMode",
			"genMatchedTau1NProngs",
			"genMatchedTau1NPi0s",

			"lep2SumChargedHadronsLV",
			"lep2SumNeutralHadronsLV",

			"genMatchedTau2LV",
			"genMatchedTau2Found",
			"genMatchedTau2VisibleLV",
			"genMatchedTau2DecayMode",
			"genMatchedTau2NProngs",
			"genMatchedTau2NPi0s",
		
			"leadingTauLV",
			"trailingTauLV",

			#"hhKinFitTau1LV",
			#"hhKinFitTau2LV",

			"simpleFitAvailable",
			"simpleFitLV",
			"simpleFitTau1Available",
			"simpleFitTau1LV",
			"simpleFitTau2Available",
			"simpleFitTau2LV",

			"leadingTauDecayMode",
			"leadingTauSumChargedHadronsLV",
			"leadingTauSumNeutralHadronsLV",

			"trailingTauDecayMode",
			"trailingTauSumChargedHadronsLV",
			"trailingTauSumNeutralHadronsLV",

			#"a1OmegaHHKinFit_1",
			#"a1OmegaHHKinFit_2",
			#"a1OmegaSimpleFit_1",
			#"a1OmegaSimpleFit_2",
		
			#"rhoNeutralChargedAsymmetry_1",
			#"rhoNeutralChargedAsymmetry_2",

			#"visibleOverFullEnergyHHKinFit_1",
			#"visibleOverFullEnergyHHKinFit_2",
			#"visibleOverFullEnergySimpleFit_1",
			#"visibleOverFullEnergySimpleFit_2",
			#"visibleToFullAngleHHKinFit_1",
			#"visibleToFullAngleHHKinFit_2",
			#"visibleToFullAngleSimpleFit_1",
			#"visibleToFullAngleSimpleFit_2",

			#"tauPolarisationDiscriminatorHHKinFit",
			#"tauPolarisationDiscriminatorSimpleFit",
		
			"polarisationOmegaGenMatched_1",
			"polarisationOmegaGenMatched_2",
			"polarisationOmegaSimpleFit_1",
			"polarisationOmegaSimpleFit_2",
			#"polarisationOmegaHHKinFit_1",
			#"polarisationOmegaHHKinFit_2",
		
			"polarisationOmegaBarGenMatched_1",
			"polarisationOmegaBarGenMatched_2",
			"polarisationOmegaBarSimpleFit_1",
			"polarisationOmegaBarSimpleFit_2",
			#"polarisationOmegaBarHHKinFit_1",
			#"polarisationOmegaBarHHKinFit_2",
		
			"polarisationOmegaVisibleGenMatched_1",
			"polarisationOmegaVisibleGenMatched_2",
			"polarisationOmegaVisibleSimpleFit_1",
			"polarisationOmegaVisibleSimpleFit_2",
			#"polarisationOmegaVisibleHHKinFit_1",
			#"polarisationOmegaVisibleHHKinFit_2",
		
			"polarisationCombinedOmegaGenMatched",
			"polarisationCombinedOmegaSimpleFit",
			#"polarisationCombinedOmegaHHKinFit",
		
			"polarisationCombinedOmegaBarGenMatched",
			"polarisationCombinedOmegaBarSimpleFit",
			#"polarisationCombinedOmegaBarHHKinFit",
		
			"polarisationCombinedOmegaVisibleGenMatched",
			"polarisationCombinedOmegaVisibleSimpleFit",
			#"polarisationCombinedOmegaVisibleHHKinFit"
		]

	def recoPolarisationQuantitiesSvfit(self, *args, **kwargs):
		return [
			"polarisationOmegaSvfit_1",
			"polarisationOmegaSvfit_2",
			"polarisationOmegaBarSvfit_1",
			"polarisationOmegaBarSvfit_2",
			"polarisationOmegaVisibleSvfit_1",
			"polarisationOmegaVisibleSvfit_2",
			"polarisationCombinedOmegaSvfit",
			"polarisationCombinedOmegaBarSvfit",
			"polarisationCombinedOmegaVisibleSvfit",
		
			"polarisationOmegaSvfitM91_1",
			"polarisationOmegaSvfitM91_2",
			"polarisationOmegaBarSvfitM91_1",
			"polarisationOmegaBarSvfitM91_2",
			"polarisationOmegaVisibleSvfitM91_1",
			"polarisationOmegaVisibleSvfitM91_2",
			"polarisationCombinedOmegaSvfitM91",
			"polarisationCombinedOmegaBarSvfitM91",
			"polarisationCombinedOmegaVisibleSvfitM91"
		]

	def weightQuantities(self, *args, **kwargs):
		return [
			"hltWeight",
			"triggerWeight_1",
			"triggerWeight_2",
			"identificationWeight_1",
			"identificationWeight_2",
			"puWeight",
			"tauEnergyScaleWeight",
			"generatorWeight",
			"crossSectionPerEventWeight",
			"numberGeneratedEventsWeight",
			"embeddingWeight",
			"eventWeight",
			"sampleStitchingWeight",
			"tauSpinnerWeight",
			"tauSpinnerWeight000",
			"tauSpinnerWeight005",
			"tauSpinnerWeight010",
			"tauSpinnerWeight015",
			"tauSpinnerWeight020",
			"tauSpinnerWeight025",
			"tauSpinnerWeight030",
			"tauSpinnerWeight035",
			"tauSpinnerWeight040",
			"tauSpinnerWeight045",
			"tauSpinnerWeight050",
			"tauSpinnerWeight055",
			"tauSpinnerWeight060",
			"tauSpinnerWeight065",
			"tauSpinnerWeight070",
			"tauSpinnerWeight075",
			"tauSpinnerWeight080",
			"tauSpinnerWeight085",
			"tauSpinnerWeight090",
			"tauSpinnerWeight095",
			"tauSpinnerWeight100",
			"tauSpinnerWeightSample",
			"tauSpinnerWeightInvSample",
			"antiEVLooseSFWeight_1",
			"antiELooseSFWeight_1",
			"antiEMediumSFWeight_1",
			"antiETightSFWeight_1",
			"antiEVTightSFWeight_1",
			"antiEVLooseSFWeight_2",
			"antiELooseSFWeight_2",
			"antiEMediumSFWeight_2",
			"antiETightSFWeight_2",
			"antiEVTightSFWeight_2",
			"emuQcdWeightUp",
			"emuQcdWeightNom",
			"emuQcdWeightDown",
			"topPtReweightWeight",
			"topPtReweightWeightRun1",
			"topPtReweightWeightRun2",
			"zPtReweightWeight",
			"eleTauFakeRateWeight",
			"muTauFakeRateWeight",
			"madGraphWeight000",
			"madGraphWeight010",
			"madGraphWeight020",
			"madGraphWeight030",
			"madGraphWeight040",
			"madGraphWeight050",
			"madGraphWeight060",
			"madGraphWeight070",
			"madGraphWeight080",
			"madGraphWeight090",
			"madGraphWeight100",
			"madGraphWeightSample",
			"madGraphWeightInvSample"]

	def melaQuantities(self, *args, **kwargs):
		return [
			"melaProbCPEvenGGH",
			"melaProbCPOddGGH",
			"melaProbCPMixGGH",
			"melaDiscriminatorD0MinusGGH",
			"melaDiscriminatorDCPGGH",

			"melaProbCPEvenVBF",
			"melaProbCPOddVBF",
			"melaProbCPMixVBF",
			"melaDiscriminatorD0MinusVBF",
			"melaDiscriminatorDCPVBF",
		
			#"melaProbCPEvenWlepH",
			#"melaProbCPOddWlepH",
			#"melaProbCPMixWlepH",
			#"melaDiscriminatorD0MinusWlepH",
			#"melaDiscriminatorDCPWlepH",
		
			#"melaProbCPEvenWhadH",
			#"melaProbCPOddWhadH",
			#"melaProbCPMixWhadH",
			#"melaDiscriminatorD0MinusWhadH",
			#"melaDiscriminatorDCPWhadH",
		
			#"melaProbCPEvenZlepH",
			#"melaProbCPOddZlepH",
			#"melaProbCPMixZlepH",
			#"melaDiscriminatorD0MinusZlepH",
			#"melaDiscriminatorDCPZlepH",
		
			#"melaProbCPEvenZhadH",
			#"melaProbCPOddZhadH",
			#"melaProbCPMixZhadH",
			#"melaDiscriminatorD0MinusZhadH",
			#"melaDiscriminatorDCPZhadH",
		
			"melaM125ProbCPEvenGGH",
			"melaM125ProbCPOddGGH",
			"melaM125ProbCPMixGGH",
			"melaM125DiscriminatorD0MinusGGH",
			"melaM125DiscriminatorDCPGGH",

			"melaM125ProbCPEvenVBF",
			"melaM125ProbCPOddVBF",
			"melaM125ProbCPMixVBF",
			"melaM125DiscriminatorD0MinusVBF",
			"melaM125DiscriminatorDCPVBF",
		
			#"melaM125ProbCPEvenWlepH",
			#"melaM125ProbCPOddWlepH",
			#"melaM125ProbCPMixWlepH",
			#"melaM125DiscriminatorD0MinusWlepH",
			#"melaM125DiscriminatorDCPWlepH",
		
			#"melaM125ProbCPEvenWhadH",
			#"melaM125ProbCPOddWhadH",
			#"melaM125ProbCPMixWhadH",
			#"melaM125DiscriminatorD0MinusWhadH",
			#"melaM125DiscriminatorDCPWhadH",
		
			#"melaM125ProbCPEvenZlepH",
			#"melaM125ProbCPOddZlepH",
			#"melaM125ProbCPMixZlepH",
			#"melaM125DiscriminatorD0MinusZlepH",
			#"melaM125DiscriminatorDCPZlepH",
		
			#"melaM125ProbCPEvenZhadH",
			#"melaM125ProbCPOddZhadH",
			#"melaM125ProbCPMixZhadH",
			#"melaM125DiscriminatorD0MinusZhadH",
			#"melaM125DiscriminatorDCPZhadH"
		]



	
