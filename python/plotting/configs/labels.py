
#-*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import Artus.HarryPlotter.utility.labels as labels


class LabelsDict(labels.LabelsDict):
	def __init__(self, latex_version="latex", additional_labels=None):
		super(LabelsDict, self).__init__(latex_version=latex_version, additional_labels=additional_labels)

		if latex_version == "root":
			self.labels_dict["totalbkg"] = "Exp. unc."
			self.labels_dict["data"] = "Data"
			self.labels_dict["asimov"] = "Pseudodata"
			self.labels_dict["zll"] = "Z #rightarrow ll"
			self.labels_dict["zl"] = "Z #rightarrow ll (l #rightarrow #tau)"
			self.labels_dict["zj"] = "Z #rightarrow ll (jet/pu #rightarrow #tau)"
			self.labels_dict["zmm"] = "Z #rightarrow #mu#mu"
			self.labels_dict["zee"] = "Z #rightarrow ee"
			self.labels_dict["ztt"] = "Z #rightarrow #tau#tau"
			self.labels_dict["zttpospol"] = "Z #rightarrow #tau_{R}^{#minus}#tau_{L}^{#plus}"
			self.labels_dict["zttnegpol"] = "Z #rightarrow #tau_{L}^{#minus}#tau_{R}^{#plus}"
			self.labels_dict["zttposcp"] = "Z #rightarrow #tau#tau, #psi_{2} > #frac{#pi}{4}"
			self.labels_dict["zttnegcp"] = "Z #rightarrow #tau#tau, #psi_{2} < #frac{#pi}{4}"
			self.labels_dict["tt"] = "t#bar{t} + jets"
			self.labels_dict["tttautau"] = "t#bar{t} #rightarrow #tau#tau"
			self.labels_dict["ttjt"] = "t#bar{t} + jets (tau)"
			self.labels_dict["ttjl"] = "t#bar{t} + jets (lep)"
			self.labels_dict["ttt"] = "t#bar{t} + jets (tau)"
			self.labels_dict["zmt"] = "Z #rightarrow #mu#tau (LFV)"
			self.labels_dict["zet"] = "Z #rightarrow e#tau (LFV)"
			self.labels_dict["zem"] = "Z #rightarrow e#mu (LFV)"
			self.labels_dict["ttjj"] = "t#bar{t} + jets (jet)"
			self.labels_dict["wj"] = "W + jets"
			self.labels_dict["wj_mc_os"] = self.labels_dict["wj"]
			self.labels_dict["wj_mc_ss"] = self.labels_dict["wj"]
			self.labels_dict["wjt"] = "W + jets (tau)"
			self.labels_dict["wjl"] = "W + jets (lep)"
			self.labels_dict["vv"] = "Di-boson"
			self.labels_dict["vvt"] = "Di-boson (tau)"
			self.labels_dict["vvl"] = "Di-boson (lep)"
			self.labels_dict["vvj"] = "Di-boson (jet)"
			self.labels_dict["ewk"] = "Electroweak"
			self.labels_dict["qcd"] = "QCD"
			self.labels_dict["qcd_prefit"] = "QCD"
			self.labels_dict["htt"] = "H #rightarrow #tau#tau"
			self.labels_dict["ggh"] = "ggH"
			self.labels_dict["susy_ggh"] = "SUSY ggH"
			self.labels_dict["bbh"] = "bbH"
			self.labels_dict["susy"] = "SUSY"
			self.labels_dict["qqh"] = "qqH"
			self.labels_dict["vh"] = "VH"
			self.labels_dict["wh"] = "WH"
			self.labels_dict["zh"] = "ZH"
			self.labels_dict["hww"] = "H #rightarrow WW"
			self.labels_dict["hww125"] = "H(125) #rightarrow WW"
			self.labels_dict["ff"] = "Fake Factor"
			
			self.labels_dict["qqhsm125"] = "VBF 0^{#plus#plus}"
			self.labels_dict["qqhps125"] = "VBF 0^{#minus#plus}"
			self.labels_dict["qqhmm125"] = "VBF CPmix"			
			self.labels_dict["gghsm125"] = "GF 0^{#plus#plus}"
			self.labels_dict["gghps125"] = "GF 0^{#minus#plus}"
			self.labels_dict["gghmm125"] = "GF CPmix"		

			self.labels_dict["qqhjhusm125"] = "VBF 0^{#plus#plus}"
			self.labels_dict["qqhjhups125"] = "VBF 0^{#minus#plus}"
			self.labels_dict["qqhjhumm125"] = "VBF CPmix"			
			self.labels_dict["gghjhusm125"] = "GF 0^{#plus#plus}"
			self.labels_dict["gghjhups125"] = "GF 0^{#minus#plus}"
			self.labels_dict["gghjhumm125"] = "GF CPmix"	
			
			self.labels_dict["httcpeven"] = "CP-even"
			self.labels_dict["httcpmix"] = "CP-mix"
			self.labels_dict["httcpodd"] = "CP-odd"
			self.labels_dict["susycpodd"] = "CP-odd"
			self.labels_dict["susycpodd_alt"] = "CP-odd"
			self.labels_dict["cpeven"] = "CP-even"
			self.labels_dict["cpmix_alt"] = "CP-mix"
			self.labels_dict["cpodd_alt"] = "CP-odd"

			self.labels_dict["channel_tt"] = "#tau_{h}#tau_{h}"
			self.labels_dict["channel_mt"] = "#mu#tau_{h}"
			self.labels_dict["channel_et"] = "e#tau_{h}"
			self.labels_dict["channel_em"] = "e#mu"
			self.labels_dict["channel_mm"] = "#mu#mu"
			self.labels_dict["channel_zmumu_selection_for_embedding"] = "embedding #mu#mu-selection"
			self.labels_dict["channel_ee"] = "ee"
			self.labels_dict["channel_tt_btag"] = "#tau_{h}#tau_{h}, b-tag"
			self.labels_dict["channel_mt_btag"] = "#mu#tau_{h}, b-tag"
			self.labels_dict["channel_et_btag"] = "e#tau_{h}, b-tag"
			self.labels_dict["channel_em_btag"] = "e#mu, b-tag"
			self.labels_dict["channel_tt_nobtag"] = "#tau_{h}#tau_{h}, no b-tag"
			self.labels_dict["channel_mt_nobtag"] = "#mu#tau_{h}, no b-tag"
			self.labels_dict["channel_et_nobtag"] = "e#tau_{h}, no b-tag"
			self.labels_dict["channel_em_nobtag"] = "e#mu, no b-tag"
			
			self.labels_dict["channel_em_oneprong"] = self.labels_dict["channel_em"]
			self.labels_dict["channel_em_oneprong_1"] = self.labels_dict["channel_em"]
			self.labels_dict["channel_em_oneprong_2"] = self.labels_dict["channel_em"]
			self.labels_dict["channel_em_combined_oneprong_oneprong"] = self.labels_dict["channel_em"]
			
			self.labels_dict["channel_et_oneprong"] = "e#tau_{h}+#pie"
			self.labels_dict["channel_et_oneprong_1"] = "e#tau_{h}"
			self.labels_dict["channel_et_oneprong_2"] = "#pie"
			self.labels_dict["channel_et_rho"] = "e#tau_{h}+#rhoe"
			self.labels_dict["channel_et_rho_1"] = "e#tau_{h}"
			self.labels_dict["channel_et_rho_2"] = "#rhoe"
			self.labels_dict["channel_et_a1"] = "e#tau_{h}+a_{1}e"
			self.labels_dict["channel_et_a1_1"] = "e#tau_{h}"
			self.labels_dict["channel_et_a1_2"] = "a_{1}e"
			self.labels_dict["channel_et_combined_a1_oneprong"] = "ea_{1}"
			self.labels_dict["channel_et_combined_rho_oneprong"] = "e#rho"
			self.labels_dict["channel_et_combined_oneprong_oneprong"] = "e#pi"
			
			self.labels_dict["channel_mt_oneprong"] = "#mu#tau_{h}+#pi#mu"
			self.labels_dict["channel_mt_oneprong_1"] = "#mu#tau_{h}"
			self.labels_dict["channel_mt_oneprong_2"] = "#pi#mu"
			self.labels_dict["channel_mt_rho"] = "#mu#tau_{h}+#rho#mu"
			self.labels_dict["channel_mt_rho_1"] = "#mu#tau_{h}"
			self.labels_dict["channel_mt_rho_2"] = "#rho#mu"
			self.labels_dict["channel_mt_a1"] = "#mu#tau_{h}+a_{1}#mu"
			self.labels_dict["channel_mt_a1_1"] = "#mu#tau_{h}"
			self.labels_dict["channel_mt_a1_2"] = "a_{1}#mu"
			self.labels_dict["channel_mt_combined_a1_oneprong"] = "#mua_{1}"
			self.labels_dict["channel_mt_combined_rho_oneprong"] = "#mu#rho"
			self.labels_dict["channel_mt_combined_oneprong_oneprong"] = "#mu#pi"
			
			self.labels_dict["channel_tt_oneprong"] = "#pi#tau_{h}+#tau_{h}#pi"
			self.labels_dict["channel_tt_oneprong_1"] = "#pi#tau_{h}"
			self.labels_dict["channel_tt_oneprong_2"] = "#tau_{h}#pi"
			self.labels_dict["channel_tt_rho"] = "#rho#tau_{h}+#tau_{h}#rho"
			self.labels_dict["channel_tt_rho_1"] = "#rho#tau_{h}"
			self.labels_dict["channel_tt_rho_2"] = "#tau_{h}#rho"
			self.labels_dict["channel_tt_a1"] = "a_{1}#tau_{h}+#tau_{h}a_{1}"
			self.labels_dict["channel_tt_a1_1"] = "a_{1}#tau_{h}"
			self.labels_dict["channel_tt_a1_2"] = "#tau_{h}a_{1}"
			self.labels_dict["channel_tt_combined_a1_a1"] = "a_{1}a_{1}"
			self.labels_dict["channel_tt_combined_a1_rho"] = "a_{1}#rho+#rhoa_{1}"
			self.labels_dict["channel_tt_combined_a1_oneprong"] = "a_{1}#pi+#pia_{1}"
			self.labels_dict["channel_tt_combined_rho_rho"] = "#rho#rho"
			self.labels_dict["channel_tt_combined_rho_oneprong"] = "#rho#pi+#pi#rho"
			self.labels_dict["channel_tt_combined_oneprong_oneprong"] = "#pi#pi"
			
			self.labels_dict["cat_oneprong"] = "#pi^{#pm} / l^{#pm}"
			self.labels_dict["cat_rho"] = "#rho^{#pm} #rightarrow #pi^{#pm} #pi^{0}"
			self.labels_dict["cat_a1"] = "a_{1}^{#pm} #rightarrow #pi^{#pm} #pi^{#pm} #pi^{#mp}"
			
			# Z->tautau polarisation labels
			for channel in ["ee", "em", "et", "mm", "mt", "tt"]:
				self.labels_dict[channel+"_rhoNeutralChargedAsymmetry"] = "(E_{#pi^{#pm}} - E_{#pi^{0}}) / (E_{#pi^{#pm}} + E_{#pi^{0}})"
				self.labels_dict[channel+"_rhoNeutralChargedAsymmetry_1"] = "(E_{#pi^{#pm}} - E_{#pi^{0}}) / (E_{#pi^{#pm}} + E_{#pi^{0}})"
				self.labels_dict[channel+"_rhoNeutralChargedAsymmetry_2"] = "(E_{#pi^{#pm}} - E_{#pi^{0}}) / (E_{#pi^{#pm}} + E_{#pi^{0}})"
				self.labels_dict[channel+"_visibleOverFullEnergySvfit_1"] = "E_{vis} / E_{#tau}"
				self.labels_dict[channel+"_visibleOverFullEnergySvfit_2"] = "E_{vis} / E_{#tau}"
				self.labels_dict[channel+"_visibleOverFullEnergyHHKinFit_1"] = "E_{vis} / E_{#tau}"
				self.labels_dict[channel+"_visibleOverFullEnergyHHKinFit_2"] = "E_{vis} / E_{#tau}"
				self.labels_dict[channel+"_visibleOverFullEnergy"] = "E_{vis} / E_{#tau}"
				self.labels_dict[channel+"_visibleToFullAngleSvfit_1"] = "#angle(#tau_{vis}, #tau) / rad"
				self.labels_dict[channel+"_visibleToFullAngleSvfit_2"] = "#angle(#tau_{vis}, #tau) / rad"
				self.labels_dict[channel+"_visibleToFullAngleHHKinFit_1"] = "#angle(#tau_{vis}, #tau) / rad"
				self.labels_dict[channel+"_visibleToFullAngleHHKinFit_2"] = "#angle(#tau_{vis}, #tau) / rad"
				self.labels_dict[channel+"_tauPolarisationMva"] = "BDT Discriminator"
				self.labels_dict[channel+"_tauPolarisationDiscriminator"] = "Polarisation Discriminator"
				self.labels_dict[channel+"_lep1SumChargedHadronsLV.Pt()"] = "E_{#pi^{#pm}} / GeV"
				self.labels_dict[channel+"_lep2SumChargedHadronsLV.Pt()"] = "E_{#pi^{#pm}} / GeV"
				self.labels_dict[channel+"_lep1SumNeutralHadronsLV.Pt()"] = "E_{#pi^{0}} / GeV"
				self.labels_dict[channel+"_lep2SumNeutralHadronsLV.Pt()"] = "E_{#pi^{0}} / GeV"
				self.labels_dict["catZttPol13TeV_"+channel+"_index"] = ""
				
				for reco_fit in ["GenMatched", "Svfit", "SvfitM91", "SimpleFit", "HHKinFit"]:
					suffix = ""
					if "M91" in reco_fit:
						suffix = "_{m_{Z}}"
					elif "GenMatched" in reco_fit:
						suffix = "_{gen}"
					self.labels_dict[channel+"_polarisationCombinedOmega"+reco_fit] = "Combined Optimal Observable #Omega" + suffix
					self.labels_dict[channel+"_polarisationCombinedOmegaBar"+reco_fit] = "Combined Optimal Observable #bar{#Omega}" + suffix
					self.labels_dict[channel+"_polarisationCombinedOmegaVisible"+reco_fit] = "Combined Optimal Observable #Omega^{vis}" + suffix
					for lepton_index in ["1", "2"]:
						self.labels_dict[channel+"_polarisationOmega"+reco_fit+"_"+lepton_index] = "Optimal Observable #omega" + suffix
						self.labels_dict[channel+"_polarisationOmegaBar"+reco_fit+"_"+lepton_index] = "Optimal Observable #bar{#omega}" + suffix
						self.labels_dict[channel+"_polarisationOmegaVisible"+reco_fit+"_"+lepton_index] = "Optimal Observable #omega^{vis}" + suffix

			for channel in ["mt", "et", "tt", "em"]:
				self.labels_dict["testZttPol13TeV_"+channel+"_inclusive"] = "m_vis"

			for channel in ["em"]:
				for category in ["a1", "a1_1", "a1_2", "rho", "rho_1", "rho_2"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = "discriminator"
				for category in ["oneprong_1"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				for category in ["oneprong", "oneprong_2"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]
				for category in ["combined_oneprong_oneprong"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]

				for category in ["a1_a1", "a1_rho", "a1_oneprong", "rho_rho", "rho_oneprong"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_combined_"+category] = "discriminator"
				for category in ["oneprong_oneprong"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_combined_"+category] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]

			for channel in ["mt", "et"]:
				for category in ["a1", "a1_2"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]
				for category in ["rho", "rho_2"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]
				for category in ["oneprong", "oneprong_2"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]
				for category in ["a1_1", "rho_1"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = "discriminator"
				for category in ["oneprong_1"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_"+category] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]

				for category in ["a1_a1", "a1_rho", "rho_rho"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_combined_"+category] = "discriminator"
				for category in ["a1_oneprong", "rho_oneprong", "oneprong_oneprong"]:
					self.labels_dict["testZttPol13TeV_"+channel+"_combined_"+category] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]

			for channel in ["tt"]:
				self.labels_dict["testZttPol13TeV_"+channel+"_a1"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_a1_1"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_a1_2"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]

				self.labels_dict["testZttPol13TeV_"+channel+"_rho"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_rho_1"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_rho_2"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]

				self.labels_dict["testZttPol13TeV_"+channel+"_oneprong"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_oneprong_1"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_1"]
				self.labels_dict["testZttPol13TeV_"+channel+"_oneprong_2"] = self.labels_dict[channel+"_polarisationOmegaBarSvfit_2"]

				self.labels_dict["testZttPol13TeV_"+channel+"_combined_a1_a1"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]
				self.labels_dict["testZttPol13TeV_"+channel+"_combined_a1_rho"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]
				self.labels_dict["testZttPol13TeV_"+channel+"_combined_a1_oneprong"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]

				self.labels_dict["testZttPol13TeV_"+channel+"_combined_rho_rho"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]
				self.labels_dict["testZttPol13TeV_"+channel+"_combined_rho_oneprong"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]

				self.labels_dict["testZttPol13TeV_"+channel+"_combined_oneprong_oneprong"] = self.labels_dict[channel+"_polarisationCombinedOmegaBarSvfit"]
			
			for channel in ["ee", "em", "et", "mm", "mt", "tt"]:
				self.labels_dict["channel_"+channel+"_0jet_inclusive"] = self.labels_dict["channel_"+channel]+": 0-Jet-inclusive"
				self.labels_dict["channel_"+channel+"_0jet_low"] = self.labels_dict["channel_"+channel]+": 0-Jet-low"
				self.labels_dict["channel_"+channel+"_0jet_high"] = self.labels_dict["channel_"+channel]+": 0-Jet-high"

				self.labels_dict["channel_"+channel+"_1jet_inclusive"] = self.labels_dict["channel_"+channel]+": 1-Jet-inclusive"
				self.labels_dict["channel_"+channel+"_1jet_low"] = self.labels_dict["channel_"+channel]+": 1-Jet-low"
				self.labels_dict["channel_"+channel+"_1jet_high"] = self.labels_dict["channel_"+channel]+": 1-Jet-high"

				self.labels_dict["channel_"+channel+"_2jet_vbf"] = self.labels_dict["channel_"+channel]+": 2-Jet-VBF"
				self.labels_dict["channel_"+channel+"_2jet_inclusive"] = self.labels_dict["channel_"+channel]+": 2-Jet-inclusive"

				self.labels_dict["channel_"+channel+"_inclusive"] = self.labels_dict["channel_"+channel]+": inclusive"
				self.labels_dict["channel_"+channel+"_ztt_bkg"] = self.labels_dict["channel_"+channel]+": BDT-bkg"
				self.labels_dict["channel_"+channel+"_ztt_mid"] = self.labels_dict["channel_"+channel]+": BDT-middle"
				self.labels_dict["channel_"+channel+"_ztt_sig"] = self.labels_dict["channel_"+channel]+": BDT-signal"
				self.labels_dict[channel+"_lep1_centrality"] = "Centrality(l_{1})"
				self.labels_dict[channel+"_lep2_centrality"] = "Centrality(l_{2})"
				self.labels_dict[channel+"_delta_lep_centrality"] = "#Delta Centrality"
				self.labels_dict[channel+"_min_ll_jet_eta"] = "min(#eta_{ll}+#eta_{j1}, #eta_{ll}+#eta_{j2})"
				self.labels_dict[channel+"_pVecSum"] = "#cbar#vec{#slash{E}}+#vec{p(ll)}+#vec{p(jj)}#cbar / GeV"
				self.labels_dict[channel+"_H_mass"] = "m_{H}"
				self.labels_dict[channel+"_pScalSum"] = "#cbar#vec{#slash{E}}#cbar+#cbar#vec{p(ll)}#cbar+#cbar#vec{p(jj)}#cbar / GeV"
				self.labels_dict[channel+"_ptvis"] = "Visible Di-#tau p_{T} / GeV"
				self.labels_dict[channel+"_H_pt"] = "p_{T}(#vec{ll}+#vec{#slash{E}_{T}}) / GeV"
				self.labels_dict[channel+"_diLep_centrality"] = "Centrality(ll)"
				self.labels_dict[channel+"_diLep_diJet_deltaR"] = "#Delta R(ll,jj)"
				self.labels_dict[channel+"_disc_1"] = "BDT final discriminator"
				self.labels_dict[channel+"_ztt_1"] = "BDT Z#tau#tau"
				self.labels_dict[channel+"_ttj_1"] = "BDT t#bar{t} + jets"
				self.labels_dict[channel+"_vbf_1"] = "BDT VBF"
			self.labels_dict["diLepMass"] = "Visible di-#tau mass / GeV"
			self.labels_dict["svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["zmumu_selection_for_embedding_ZMass"] = "m(#mu#mu) [GeV]"
			self.labels_dict["zmumu_selection_for_embedding_integral"] = "Integral"

			self.labels_dict["tt_decayMode_1"] = "Leading Tau DM"
			self.labels_dict["tt_decayMode_2"] = "Trailing Tau DM"
			self.labels_dict["tt_eta_1"] = "Leading Tau #eta"
			self.labels_dict["tt_eta_2"] = "Trailing Tau #eta"
			self.labels_dict["tt_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["tt_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["tt_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["tt_integral"] = "Integral"
			self.labels_dict["tt_iso_1"] = "Leading Tau Isolation"
			self.labels_dict["tt_iso_2"] = "Trailing Tau Isolation"
			self.labels_dict["tt_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["tt_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["tt_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["tt_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["tt_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["tt_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["tt_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["tt_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["tt_m_1"] = "Leading Tau Mass / GeV"
			self.labels_dict["tt_m_2"] = "Trailing Tau Mass / GeV"
			self.labels_dict["tt_m_ll"] = "Visible di-#tau mass / GeV"
			self.labels_dict["tt_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["tt_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["tt_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["tt_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["tt_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["tt_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["tt_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["tt_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["tt_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["tt_mt_1"] = "Transverse Mass m_{T} (#tau, #slash{E}_{T}) / GeV"
			self.labels_dict["tt_mt_tot"] = "Total Transverse Mass m^{tot}_{T} / GeV"
			self.labels_dict["tt_mt_lep1met"] = "Transverse Mass m_{T} (#tau, #slash{E}_{T}) / GeV"
			self.labels_dict["tt_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["tt_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["tt_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["tt_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["tt_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["tt_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["tt_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["tt_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["tt_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["tt_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["tt_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["tt_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["tt_m_vis"] = "Visible di-#tau mass / GeV"
			self.labels_dict["tt_nJets30"] = "Number of Jets"
			self.labels_dict["tt_njetspt30"] = "Number of Jets"
			self.labels_dict["tt_njets"] = "Number of Jets"
			self.labels_dict["tt_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["tt_njetingap"] = "Number of central Jets"
			self.labels_dict["tt_npu"] = "NPU"
			self.labels_dict["tt_npv"] = "NPV"
			self.labels_dict["tt_phi_1"] = "Leading Tau #phi"
			self.labels_dict["tt_phi_2"] = "Trailing Tau #phi"
			self.labels_dict["tt_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["tt_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["tt_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["tt_pt_1"] = "Leading Tau p_{T} / GeV"
			self.labels_dict["tt_pt_2"] = "Trailing Tau p_{T} / GeV"
			self.labels_dict["tt_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["tt_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["tt_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["tt_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["tt_puweight"] = "PU Weight"
			self.labels_dict["tt_rho"] = "rho"
			self.labels_dict["tt_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["tt_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["tt_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["tt_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["tt_trigweight_1"] = "Leading Tau Trigger Weight"
			self.labels_dict["tt_trigweight_2"] = "Trailing Tau Trigger Weight"
			self.labels_dict["tt_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["tt_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["tt_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["tt_rhoNeutralChargedAsymmetry_1"] = "Leading Tau (E_{#pi^{#pm}} - E_{#pi^{0}}) / (E_{#pi^{#pm}} + E_{#pi^{0}})"
			self.labels_dict["tt_rhoNeutralChargedAsymmetry_2"] = "Trailing Tau (E_{#pi^{#pm}} - E_{#pi^{0}}) / (E_{#pi^{#pm}} + E_{#pi^{0}})"
			self.labels_dict["tt_visibleOverFullEnergy_1"] = "Leading Tau E_{vis}(#tau_{had}) / E_{#tau}"
			self.labels_dict["tt_visibleOverFullEnergy_2"] = "Trailing Tau E_{vis}(#tau_{had}) / E_{#tau}"
			
			self.labels_dict["mt_decayMode_2"] = "Tau DM"
			self.labels_dict["mt_eta_1"] = "Muon #eta"
			self.labels_dict["mt_eta_2"] = "Tau #eta"
			self.labels_dict["mt_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["mt_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["mt_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["mt_integral"] = "Integral"
			self.labels_dict["mt_iso_1"] = "Muon Isolation"
			self.labels_dict["mt_iso_2"] = "Tau Isolation"
			self.labels_dict["mt_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["mt_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["mt_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["mt_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["mt_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["mt_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["mt_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["mt_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["mt_m_1"] = "Muon Mass / GeV"
			self.labels_dict["mt_m_2"] = "Tau Mass / GeV"
			self.labels_dict["mt_m_ll"] = "Visible di-#tau mass / GeV"
			self.labels_dict["mt_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["mt_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["mt_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["mt_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mt_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mt_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mt_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mt_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["mt_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["mt_mt_1"] = "Transverse Mass m_{T} (#mu, #slash{E}_{T}) / GeV"
			self.labels_dict["mt_mt_2"] = "Transverse Mass m_{T} (#tau, #slash{E}_{T}) / GeV"
			self.labels_dict["mt_mt_tot"] = "Total Transverse Mass m^{tot}_{T} / GeV"
			self.labels_dict["mt_mt_lep1met"] = "Transverse Mass m_{T} (#mu, #slash{E}_{T}) / GeV"
			self.labels_dict["mt_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["mt_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["mt_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mt_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mt_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mt_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mt_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["mt_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mt_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mt_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mt_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mt_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["mt_m_vis"] = "Visible di-#tau mass / GeV"
			self.labels_dict["mt_nJets30"] = "Number of Jets"
			self.labels_dict["mt_njetspt30"] = "Number of Jets"
			self.labels_dict["mt_njets"] = "Number of Jets"
			self.labels_dict["mt_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["mt_njetingap"] = "Number of central Jets"
			self.labels_dict["mt_npu"] = "NPU"
			self.labels_dict["mt_npv"] = "NPV"
			self.labels_dict["mt_phi_1"] = "Muon #phi"
			self.labels_dict["mt_phi_2"] = "Tau #phi"
			self.labels_dict["mt_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["mt_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["mt_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["mt_pt_1"] = "Muon p_{T} / GeV"
			self.labels_dict["mt_pt_2"] = "Tau p_{T} / GeV"
			self.labels_dict["mt_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["mt_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["mt_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["mt_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["mt_puweight"] = "PU Weight"
			self.labels_dict["mt_rho"] = "rho"
			self.labels_dict["mt_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["mt_trigweight_1"] = "Muon Trigger Weight"
			self.labels_dict["mt_trigweight_2"] = "Tau Trigger Weight"
			self.labels_dict["mt_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["mt_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["mt_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["mt_pZetaMiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["mt_pZetaVis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["mt_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["mt_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["mt_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["mt_visibleOverFullEnergy_1"] = "E(#mu) / E_{#tau}"
			self.labels_dict["mt_visibleOverFullEnergy_2"] = "E(#tau_{had}) / E_{#tau}"
			
			self.labels_dict["et_decayMode_2"] = "Tau DM"
			self.labels_dict["et_eta_1"] = "Electron #eta"
			self.labels_dict["et_eta_2"] = "Tau #eta"
			self.labels_dict["et_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["et_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["et_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["et_integral"] = "Integral"
			self.labels_dict["et_iso_1"] = "Electron Isolation"
			self.labels_dict["et_iso_2"] = "Tau Isolation"
			self.labels_dict["et_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["et_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["et_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["et_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["et_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["et_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["et_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["et_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["et_m_1"] = "Electron Mass / GeV"
			self.labels_dict["et_m_2"] = "Tau Mass / GeV"
			self.labels_dict["et_m_ll"] = "Visible di-#tau mass / GeV"
			self.labels_dict["et_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["et_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["et_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["et_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["et_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["et_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["et_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["et_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["et_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["et_mt_1"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["et_mt_tot"] = "Total Transverse Mass m^{tot}_{T} / GeV"
			self.labels_dict["et_mt_lep1met"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["et_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["et_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["et_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["et_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["et_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["et_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["et_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["et_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["et_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["et_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["et_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["et_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["et_m_vis"] = "Visible di-#tau mass / GeV"
			self.labels_dict["et_nJets30"] = "Number of Jets"
			self.labels_dict["et_njetspt30"] = "Number of Jets"
			self.labels_dict["et_njets"] = "Number of Jets"
			self.labels_dict["et_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["et_njetingap"] = "Number of central Jets"
			self.labels_dict["et_npu"] = "NPU"#Delta R(ll,jj)
			self.labels_dict["et_npv"] = "NPV"
			self.labels_dict["et_phi_1"] = "Electron #phi"
			self.labels_dict["et_phi_2"] = "Tau #phi"
			self.labels_dict["et_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["et_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["et_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["et_pt_1"] = "Electron p_{T} / GeV"
			self.labels_dict["et_pt_2"] = "Tau p_{T} / GeV"
			self.labels_dict["et_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["et_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["et_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["et_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["et_puweight"] = "PU Weight"
			self.labels_dict["et_rho"] = "rho"
			self.labels_dict["et_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["et_trigweight_1"] = "Electron Trigger Weight"
			self.labels_dict["et_trigweight_2"] = "Tau Trigger Weight"
			self.labels_dict["et_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["et_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["et_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["et_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["et_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["et_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["et_visibleOverFullEnergy_1"] = "E(e) / E_{#tau}"
			self.labels_dict["et_visibleOverFullEnergy_2"] = "E(#tau_{had}) / E_{#tau}"
			
			self.labels_dict["em_eta_1"] = "Electron #eta"
			self.labels_dict["em_eta_2"] = "Muon #eta"
			self.labels_dict["em_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["em_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["em_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["em_integral"] = "Integral"
			self.labels_dict["em_iso_1"] = "Electron Isolation"
			self.labels_dict["em_iso_2"] = "Muon Isolation"
			self.labels_dict["em_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["em_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["em_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["em_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["em_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["em_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["em_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["em_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["em_m_1"] = "Electron Mass / GeV"
			self.labels_dict["em_m_2"] = "Muon Mass / GeV"
			self.labels_dict["em_m_ll"] = "Visible di-#tau mass / GeV"
			self.labels_dict["em_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["em_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["em_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["em_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["em_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["em_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["em_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["em_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["em_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["em_mt_1"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["em_mt_tot"] = "Total Transverse Mass m^{tot}_{T} / GeV"
			self.labels_dict["em_mt_lep1met"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["em_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["em_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["em_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["em_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["em_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["em_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["em_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["em_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["em_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["em_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["em_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["em_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["em_m_vis"] = "Visible di-#tau mass / GeV"
			self.labels_dict["em_nJets30"] = "Number of Jets"
			self.labels_dict["em_njetspt30"] = "Number of Jets"
			self.labels_dict["em_njets"] = "Number of Jets"
			self.labels_dict["em_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["em_njetingap"] = "Number of central Jets"
			self.labels_dict["em_npu"] = "NPU"
			self.labels_dict["em_npv"] = "NPV"
			self.labels_dict["em_phi_1"] = "Electron #phi"
			self.labels_dict["em_phi_2"] = "Muon #phi"
			self.labels_dict["em_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["em_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["em_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["em_pt_1"] = "Electron p_{T} / GeV"
			self.labels_dict["em_pt_2"] = "Muon p_{T} / GeV"
			self.labels_dict["em_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["em_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["em_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["em_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["em_puweight"] = "PU Weight"
			self.labels_dict["em_rho"] = "rho"
			self.labels_dict["em_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["em_trigweight_1"] = "Electron Trigger Weight"
			self.labels_dict["em_trigweight_2"] = "Muon Trigger Weight"
			self.labels_dict["em_pZetaMissVis"] = "#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right) / GeV"
			self.labels_dict["em_pzetamiss"] = "p^{miss}_{#zeta} / GeV"
			self.labels_dict["em_pzetavis"] = "p^{vis}_{#zeta} / GeV"
			self.labels_dict["em_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["em_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["em_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["em_visibleOverFullEnergy_1"] = "E(e) / E_{#tau}"
			self.labels_dict["em_visibleOverFullEnergy_2"] = "E(#mu) / E_{#tau}"
			
			self.labels_dict["mm_eta_1"] = "Leading Muon #eta"
			self.labels_dict["mm_eta_2"] = "Trailing Muon #eta"
			self.labels_dict["mm_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["mm_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["mm_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["mm_integral"] = "Integral"
			self.labels_dict["mm_iso_1"] = "Leading Muon Isolation"
			self.labels_dict["mm_iso_2"] = "Trailing Muon Isolation"
			self.labels_dict["mm_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["mm_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["mm_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["mm_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["mm_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["mm_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["mm_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["mm_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["mm_m_1"] = "Leading Muon Mass / GeV"
			self.labels_dict["mm_m_2"] = "Trailing Muon Mass / GeV"
			self.labels_dict["mm_m_ll"] = "Di-muon Mass m_{#mu#mu} / GeV"
			self.labels_dict["mm_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["mm_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["mm_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["mm_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mm_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mm_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mm_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mm_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["mm_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["mm_mt_1"] = "Transverse Mass m_{T} (#mu, #slash{E}_{T}) / GeV"
			self.labels_dict["mm_mt_lep1met"] = "Transverse Mass m_{T} (#mu, #slash{E}_{T}) / GeV"
			self.labels_dict["mm_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["mm_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["mm_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mm_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mm_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mm_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mm_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["mm_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["mm_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["mm_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["mm_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["mm_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["mm_m_vis"] = "Di-muon Mass m_{#mu#mu} / GeV"
			self.labels_dict["mm_nJets30"] = "Number of Jets"
			self.labels_dict["mm_njetspt30"] = "Number of Jets"
			self.labels_dict["mm_njets"] = "Number of Jets"
			self.labels_dict["mm_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["mm_njetingap"] = "Number of central Jets"
			self.labels_dict["mm_npu"] = "NPU"
			self.labels_dict["mm_npv"] = "NPV"
			self.labels_dict["mm_phi_1"] = "Leading Muon #phi"
			self.labels_dict["mm_phi_2"] = "Trailing Muon #phi"
			self.labels_dict["mm_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["mm_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["mm_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["mm_pt_1"] = "Leading Muon p_{T} / GeV"
			self.labels_dict["mm_pt_2"] = "Trailing Muon p_{T} / GeV"
			self.labels_dict["mm_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["mm_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["mm_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["mm_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["mm_puweight"] = "PU Weight"
			self.labels_dict["mm_rho"] = "rho"
			self.labels_dict["mm_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["mm_trigweight_1"] = "Leading Muon Trigger Weight"
			self.labels_dict["mm_trigweight_2"] = "Trailing Muon Trigger Weight"
			self.labels_dict["mm_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["mm_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["mm_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["mm_visibleOverFullEnergy_1"] = "Leading Muon E(#mu) / E_{#tau}"
			self.labels_dict["mm_visibleOverFullEnergy_2"] = "Trailing Muon E(#mu) / E_{#tau}"
			
			self.labels_dict["ee_eta_1"] = "Leading Electron #eta"
			self.labels_dict["ee_eta_2"] = "Trailing Electron #eta"
			self.labels_dict["ee_eta_ll"] = "#eta^{\\ell\\ell}"
			self.labels_dict["ee_eta_llmet"] = "#eta^{\\ell\\ell,MEt}"
			self.labels_dict["ee_eta_sv"] = "SVfit #eta(#tau#tau)"
			self.labels_dict["ee_integral"] = "Integral"
			self.labels_dict["ee_iso_1"] = "Leading Electron Isolation"
			self.labels_dict["ee_iso_2"] = "Trailing Electron Isolation"
			self.labels_dict["ee_jdeta"] = "#Delta#eta_{jj}"
			self.labels_dict["ee_jdphi"] = "#Delta#phi_{jj}"
			self.labels_dict["ee_jeta_1"] = "Leading Jet #eta"
			self.labels_dict["ee_jeta_2"] = "Trailing Jet #eta"
			self.labels_dict["ee_jphi_1"] = "Leading Jet #phi"
			self.labels_dict["ee_jphi_2"] = "Trailing Jet #phi"
			self.labels_dict["ee_jpt_1"] = "Leading Jet p_{T} / GeV"
			self.labels_dict["ee_jpt_2"] = "Trailing Jet p_{T} / GeV"
			self.labels_dict["ee_m_1"] = "Leading Electron Mass / GeV"
			self.labels_dict["ee_m_2"] = "Trailing Electron Mass / GeV"
			self.labels_dict["ee_m_ll"] = "Di-electron Mass m_{ee} / GeV"
			self.labels_dict["ee_m_llmet"] = "m_{\\ell\\ell,MEt} / GeV"
			self.labels_dict["ee_m_sv"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["ee_met"] = "PFlow #slash{E}_{T}"
			self.labels_dict["ee_metcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["ee_metcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["ee_metcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["ee_metcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["ee_metphi"] = "PFlow #slash{E}_{T} #phi"
			self.labels_dict["ee_mjj"] = "Di-jet Mass m_{jj} / GeV"
			self.labels_dict["ee_mt_1"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["ee_mt_lep1met"] = "Transverse Mass m_{T} (e, #slash{E}_{T}) / GeV"
			self.labels_dict["ee_mt_ll"] = "m_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["ee_mt_llmet"] = "m_{T}^{\\ell\\ell,MEt} / GeV"
			self.labels_dict["ee_mvacov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["ee_mvacov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["ee_mvacov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["ee_mvacov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["ee_mvamet"] = "#slash{E}_{T} / GeV"
			self.labels_dict["ee_mvametcov00"] = "Cov_{0,0}(#slash{E}_{T})"
			self.labels_dict["ee_mvametcov01"] = "Cov_{0,1}(#slash{E}_{T})"
			self.labels_dict["ee_mvametcov10"] = "Cov_{1,0}(#slash{E}_{T})"
			self.labels_dict["ee_mvametcov11"] = "Cov_{1,1}(#slash{E}_{T})"
			self.labels_dict["ee_mvametphi"] = "#phi(#slash{E}_{T})"
			self.labels_dict["ee_m_vis"] = "Di-electron Mass m_{e} / GeV"
			self.labels_dict["ee_nJets30"] = "Number of Jets"
			self.labels_dict["ee_njetspt30"] = "Number of Jets"
			self.labels_dict["ee_njets"] = "Number of Jets"
			self.labels_dict["ee_nbtag"] = "Number of b-tagged Jets"
			self.labels_dict["ee_njetingap"] = "Number of central Jets"
			self.labels_dict["ee_npu"] = "NPU"
			self.labels_dict["ee_npv"] = "NPV"
			self.labels_dict["ee_phi_1"] = "Leading Electron #phi"
			self.labels_dict["ee_phi_2"] = "Trailing Electron #phi"
			self.labels_dict["ee_phi_ll"] = "#phi^{\\ell\\ell}"
			self.labels_dict["ee_phi_llmet"] = "#phi^{\\ell\\ell,MEt}"
			self.labels_dict["ee_phi_sv"] = "SVfit #phi(#tau#tau)"
			self.labels_dict["ee_pt_1"] = "Leading Electron p_{T} / GeV"
			self.labels_dict["ee_pt_2"] = "Trailing Electron p_{T} / GeV"
			self.labels_dict["ee_pt_ll"] = "p_{T}^{\\ell\\ell} / GeV"
			self.labels_dict["ee_pt_llmet"] = "p_{T}^{\\ell\\ell,MEt}"
			self.labels_dict["ee_pt_sv"] = "SVfit p_{T}(#tau#tau) / GeV"
			self.labels_dict["ee_pt_tt"] = "p_{T}(#tau#tau) / GeV"
			self.labels_dict["ee_puweight"] = "PU Weight"
			self.labels_dict["ee_rho"] = "rho"
			self.labels_dict["ee_svfitMass"] = "Di-#tau Mass m_{#tau#tau} / GeV"
			self.labels_dict["ee_trigweight_1"] = "Leading Electron Trigger Weight"
			self.labels_dict["ee_trigweight_2"] = "Trailing Electron Trigger Weight"
			self.labels_dict["ee_metProjectionPar"] = "#nu_{#parallel} / GeV"
			self.labels_dict["ee_metProjectionPerp"] = "#nu_{#perp}  / GeV"
			self.labels_dict["ee_metProjectionPhi"] = "#nu_{#phi}"
			self.labels_dict["ee_visibleOverFullEnergy_1"] = "Leading Electron E(e) / E_{#tau}"
			self.labels_dict["ee_visibleOverFullEnergy_2"] = "Trailing Electron E(e) / E_{#tau}"
			
			for ch in ["ee_", "em_", "et_", "mm_", "mt_", "tt_"]:
				self.labels_dict[ch+"TrainingSelectionValue"] = "N-Fold Split Variable"
				self.labels_dict[ch+"all_vs_all"] = "BDT_{all}^{all}"
				self.labels_dict[ch+"all_vs_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{all}"
				self.labels_dict[ch+"all_vs_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{all}"
				self.labels_dict[ch+"ggh_vs_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{ggh}"
				self.labels_dict[ch+"ggh_vs_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{ggH}"
				self.labels_dict[ch+"glu_vs_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{ggh}"
				self.labels_dict[ch+"glu_vs_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{ggH}"
				self.labels_dict[ch+"vbf_vs_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{vbf}"
				self.labels_dict[ch+"vbf_vs_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{vbf}"
			self.labels_dict["BDT_all_all"] = "BDT_{all}^{all}"
			self.labels_dict["BDT_all_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{all}"
			self.labels_dict["BDT_all_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{all}"
			self.labels_dict["BDT_ggh_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{ggh}"
			self.labels_dict["BDT_ggh_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{ggH}"
			self.labels_dict["BDT_vbf_zll"] = "BDT_{Z#rightarrow \\ell\\ell}^{vbf}"
			self.labels_dict["BDT_vbf_ztt"] = "BDT_{Z#rightarrow#tau#tau}^{vbf}"
			
			for ch in ["em_", "et_", "mt_", "tt_"]:
				self.labels_dict[ch+"melaProbCPEvenGGH"] = "MELA Prob_{0^{#minus}}^{ggH}"
				self.labels_dict[ch+"melaProbCPOddGGH"] = "MELA Prob_{0^{#plus}}^{ggH}"
				self.labels_dict[ch+"melaProbCPMixGGH"] = "MELA Prob_{0^{#pm}}^{ggH}"
				self.labels_dict[ch+"melaProbCPEvenVBF"] = "MELA Prob_{0^{#minus}}^{VBF}"
				self.labels_dict[ch+"melaProbCPOddVBF"] = "MELA Prob_{0^{#plus}}^{VBF}"
				self.labels_dict[ch+"melaProbCPMixVBF"] = "MELA Prob_{0^{#pm}}^{VBF}"
			
				self.labels_dict[ch+"melaM125ProbCPEvenGGH"] = self.labels_dict[ch+"melaProbCPEvenGGH"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125ProbCPOddGGH"] = self.labels_dict[ch+"melaProbCPOddGGH"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125ProbCPMixGGH"] = self.labels_dict[ch+"melaProbCPMixGGH"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125ProbCPEvenVBF"] = self.labels_dict[ch+"melaProbCPEvenVBF"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125ProbCPOddVBF"] = self.labels_dict[ch+"melaProbCPOddVBF"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125ProbCPMixVBF"] = self.labels_dict[ch+"melaProbCPMixVBF"].replace("MELA", "MELA_{m_{H}}")
				
				self.labels_dict[ch+"melaDiscriminatorD0MinusGGH"] = "MELA D_{0^{#minus}}^{ggH}"
				self.labels_dict[ch+"melaDiscriminatorDCPGGH"] = "MELA D_{CP}^{ggH}"
				self.labels_dict[ch+"melaDiscriminatorD0MinusVBF"] = "MELA D_{0^{#minus}}^{VBF}"
				self.labels_dict[ch+"melaDiscriminatorDCPVBF"] = "MELA D_{CP}^{VBF}"
				self.labels_dict[ch+"melaDiscriminatorD0MinusGGH_signDCP"] = "MELA D_{0^{#minus}}^{ggH} #upoint sign #left(D_{CP}^{ggH}#right)"
				self.labels_dict[ch+"melaDiscriminatorD0MinusVBF_signDCP"] = "MELA D_{0^{#minus}}^{VBF} #upoint sign #left(D_{CP}^{VBF}#right)"
			
				self.labels_dict[ch+"melaM125DiscriminatorD0MinusGGH"] = self.labels_dict[ch+"melaDiscriminatorD0MinusGGH"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125DiscriminatorDCPGGH"] = self.labels_dict[ch+"melaDiscriminatorDCPGGH"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125DiscriminatorD0MinusVBF"] = self.labels_dict[ch+"melaDiscriminatorD0MinusVBF"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125DiscriminatorDCPVBF"] = self.labels_dict[ch+"melaDiscriminatorDCPVBF"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125DiscriminatorD0MinusGGH_signDCP"] = self.labels_dict[ch+"melaDiscriminatorD0MinusGGH_signDCP"].replace("MELA", "MELA_{m_{H}}")
				self.labels_dict[ch+"melaM125DiscriminatorD0MinusVBF_signDCP"] = self.labels_dict[ch+"melaDiscriminatorD0MinusVBF_signDCP"].replace("MELA", "MELA_{m_{H}}")
			
			for higgs_mass in xrange(90, 161, 5):
				self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy_ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy_ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["qqh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["qqh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["vh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["vh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["wh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["wh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["zh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["zh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpeven"]
				self.labels_dict["httcpmix{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpmix"]
				self.labels_dict["httcpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpodd"]
				self.labels_dict["susycpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd"]
				self.labels_dict["susycpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd_alt"]
				self.labels_dict["cpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpeven"]
				self.labels_dict["cpmix_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpmix_alt"]
				self.labels_dict["cpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpodd_alt"]

				for scale in [10, 25, 100, 250]:
					self.labels_dict["htt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["htt"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["ggh"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghsm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghsm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghmm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghmm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghps{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghps125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhusm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhusm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhumm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhumm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhups{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhups125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["susy_ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy_ggh"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["susy{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqh"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhsm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhsm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhmm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhmm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhps{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhps125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhusm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhusm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhumm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhumm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhups{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhups125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["vh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["vh"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["httcpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpeven"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["httcpmix{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpmix"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["httcpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpodd"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd_alt"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["cpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpeven"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["cpmix_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpmix_alt"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["cpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpodd_alt"]+" (#times {scale:d})".format(scale=scale)
					
			for higgs_mass in xrange(90, 3201, 10):
				self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy_ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy_ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["bbh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["bbh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpeven"]
				self.labels_dict["httcpmix{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpmix"]
				self.labels_dict["httcpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpodd"]
				self.labels_dict["susycpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd"]
				self.labels_dict["susycpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd_alt"]
				self.labels_dict["cpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpeven"]
				self.labels_dict["cpmix_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpmix_alt"]
				self.labels_dict["cpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["cpodd_alt"]
				for scale in [10, 25, 100, 250]:
					self.labels_dict["htt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susy_ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy_ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susy{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["bbh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["bbh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpeven"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpmix{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpmix"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd_alt"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["cpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpeven"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["cpmix_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpmix_alt"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["cpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["cpodd_alt"]+" (\\times {scale:d})".format(scale=scale)
			
			for alias, label in self.labels_dict.items():
				self.labels_dict[alias+"_large"] = "#scale[1.5]{"+label+"}"
		
		else:
			self.labels_dict["totalbkg"] = "$\\mathrm{Exp.} unc.$"
			self.labels_dict["data"] = "$\\mathrm{Data}$"
			self.labels_dict["asimov"] = "$\\mathrm{Pseudodata}$"
			self.labels_dict["zll"] = "$\\mathrm{Z}\\,\\rightarrow \\ell\\ell$"
			self.labels_dict["zmm"] = "$\\mathrm{Z}\\,\\rightarrow \\mu\\mu$"
			self.labels_dict["zee"] = "$\\mathrm{Z}\\,\\rightarrow \\mathrm{ee}$"
			self.labels_dict["ztt"] = "$\\mathrm{Z}\\,\\rightarrow \\tau\\tau$"
			self.labels_dict["tt"] = "$\\mathrm{t}\\bar{\\mathrm{t}} + \\mathrm{jets}$"
			self.labels_dict["wj"] = "$\\mathrm{W} + \\mathrm{jets}$"
			self.labels_dict["vv"] = "$\\mathrm{Di}-boson$"
			self.labels_dict["ewk"] = "$\\mathrm{Electroweak}$"
			self.labels_dict["qcd"] = "$\\mathrm{QCD}$"
			self.labels_dict["qcd_prefit"] = "$\\mathrm{QCD Prefit}$"
			self.labels_dict["htt"] = "$\\mathrm{H}\\,\\rightarrow \\tau\\tau$"
			self.labels_dict["ggh"] = "$\\mathrm{ggH}$"
			self.labels_dict["susy_ggh"] = "$\\mathrm{SUSY ggH}$"
			self.labels_dict["susy"] = "$\\mathrm{SUSY}$"
			self.labels_dict["qqh"] = "$\\mathrm{qqH}$"
			self.labels_dict["vh"] = "$\\mathrm{VH}$"
			self.labels_dict["wh"] = "$\\mathrm{WH}$"
			self.labels_dict["zh"] = "$\\mathrm{ZH}$"
			self.labels_dict["hww"] = "$\\mathrm{H}\\,\\rightarrow \\mathrm{WW}$"
			self.labels_dict["hww125"] = "$\\mathrm{H}(125) \\rightarrow \\mathrm{WW}$"
			self.labels_dict["httcpeven"] = "CP-even"
			self.labels_dict["httcpmix"] = "CP-mix"
			self.labels_dict["httcpodd"] = "CP-odd"
			self.labels_dict["susycpodd"] = "CP-odd"
			self.labels_dict["susycpodd_alt"] = "CP-odd"
			self.labels_dict["qqhsm125"] = "VBF 0^{#plus#plus}"
			self.labels_dict["qqhps125"] = "VBF 0^{#minus#plus}"
			self.labels_dict["qqhmm125"] = "VBF CPmix"			
			self.labels_dict["gghsm125"] = "GF 0^{#plus#plus}"
			self.labels_dict["gghps125"] = "GF 0^{#minus#plus}"
			self.labels_dict["gghmm125"] = "GF CPmix"		

			self.labels_dict["qqhjhusm125"] = "VBF 0^{#plus#plus}"
			self.labels_dict["qqhjhups125"] = "VBF 0^{#minus#plus}"
			self.labels_dict["qqhjhumm125"] = "VBF CPmix"			
			self.labels_dict["gghjhusm125"] = "GF 0^{#plus#plus}"
			self.labels_dict["gghjhups125"] = "GF 0^{#minus#plus}"
			self.labels_dict["gghjhumm125"] = "GF CPmix"			

			self.labels_dict["channel_tt"] = "$\\tau_{\\mathrm{h}}\\tau_{\\mathrm{h}}$"
			self.labels_dict["channel_mt"] = "$\\mu\\tau_{\\mathrm{h}}$"
			self.labels_dict["channel_et"] = "$\\mathrm{e}\\tau_{\\mathrm{h}}$"
			self.labels_dict["channel_em"] = "$\\mathrm{e}\\mu$"
			self.labels_dict["channel_mm"] = "$\\mu\\mu$"
			self.labels_dict["channel_ee"] = "$\\mathrm{ee}$"

			self.labels_dict["channel_tt_large"] = "$\\scale[1.5]{\\tau_{\\mathrm{h}}\\tau_{\\mathrm{h}}}$"
			self.labels_dict["channel_mt_large"] = "$\\scale[1.5]{\\mu\\tau_{\\mathrm{h}}}$"
			self.labels_dict["channel_et_large"] = "$\\scale[1.5]{\\mathrm{e}\\tau_{\\mathrm{h}}}$"
			self.labels_dict["channel_em_large"] = "$\\scale[1.5]{\\mathrm{e}\\mu}$"
			self.labels_dict["channel_mm_large"] = "$\\scale[1.5]{\\mu\\mu}$"
			self.labels_dict["channel_ee_large"] = "$\\scale[1.5]{\\mathrm{ee}}$"
			for channel in ["ee", "em", "et", "mm", "mt", "tt"]:
				self.labels_dict["channel_"+channel+"_0jet_inclusive"] = self.labels_dict["channel_"+channel]+": 0-Jet-inclusive$"
				self.labels_dict["channel_"+channel+"_0jet_low"] = self.labels_dict["channel_"+channel]+": 0-Jet-low$"
				self.labels_dict["channel_"+channel+"_0jet_high"] = self.labels_dict["channel_"+channel]+": 0-Jet-high$"

				self.labels_dict["channel_"+channel+"_1jet_inclusive"] = self.labels_dict["channel_"+channel]+": 1-Jet-inclusive$"
				self.labels_dict["channel_"+channel+"_1jet_low"] = self.labels_dict["channel_"+channel]+": 1-Jet-low$"
				self.labels_dict["channel_"+channel+"_1jet_high"] = self.labels_dict["channel_"+channel]+": 1-Jet-high$"

				self.labels_dict["channel_"+channel+"_2jet_vbf"] = self.labels_dict["channel_"+channel]+": 2-Jet-VBF$"
				self.labels_dict["channel_"+channel+"_2jet_inclusive"] = self.labels_dict["channel_"+channel]+": 2-Jet-inclusive$"

				self.labels_dict["channel_"+channel+"_inclusive"] = self.labels_dict["channel_"+channel]+": \\mathrm{inclusive}$"
				self.labels_dict["channel_"+channel+"_ztt_bkg"] = self.labels_dict["channel_"+channel]+": \\mathrm{BDT}-bkg$"
				self.labels_dict["channel_"+channel+"_ztt_mid"] = self.labels_dict["channel_"+channel]+": \\mathrm{BDT}-middle$"
				self.labels_dict["channel_"+channel+"_ztt_sig"] = self.labels_dict["channel_"+channel]+": \\mathrm{BDT}-signal$"
				self.labels_dict[channel+"_lep1_centrality"] = "$\\mathrm{Centrality}(l_{1})$"
				self.labels_dict[channel+"_lep2_centrality"] = "$\\mathrm{Centrality}(l_{2})$"
				self.labels_dict[channel+"_delta_lep_centrality"] = "$\\Delta \\mathrm{Centrality}$"
				self.labels_dict[channel+"_min_ll_jet_eta"] = "$\\mathrm{min}(\\eta_{\\ell\\ell}+\\eta_{\\mathrm{j}1}, \\eta_{\\ell\\ell}+\\eta_{\\mathrm{j}2})$"
				self.labels_dict[channel+"_pVecSum"] = "$|\\vec{\\slash{\\mathrm{E}}_{\\mathrm{T}}}+\\vec{\\mathrm{p}_{\\mathrm{T}}(ll)}+\\vec{\\mathrm{p}_{\\mathrm{T}}(jj)}|$"
			self.labels_dict["diLepMass"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"

			self.labels_dict["tt_decayMode_1"] = "$\\mathrm{Leading} Tau \\mathrm{DM}$"
			self.labels_dict["tt_decayMode_2"] = "$\\mathrm{Trailing} Tau \\mathrm{DM}$"
			self.labels_dict["tt_eta_1"] = "$\\mathrm{Leading} Tau \\eta$"
			self.labels_dict["tt_eta_2"] = "$\\mathrm{Trailing} Tau \\eta$"
			self.labels_dict["tt_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["tt_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["tt_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["tt_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["tt_iso_1"] = "$\\mathrm{Leading} Tau \\mathrm{Isolation}$"
			self.labels_dict["tt_iso_2"] = "$\\mathrm{Trailing} Tau \\mathrm{Isolation}$"
			self.labels_dict["tt_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["tt_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["tt_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["tt_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["tt_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["tt_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["tt_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["tt_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["tt_m_1"] = "$\\mathrm{Leading} Tau \\mathrm{Mass} / \\mathrm{GeV}$"
			self.labels_dict["tt_m_2"] = "$\\mathrm{Trailing} Tau \\mathrm{Mass} / \\mathrm{GeV}$"
			self.labels_dict["tt_m_ll"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["tt_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["tt_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["tt_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["tt_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["tt_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["tt_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\tau, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["tt_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\tau, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["tt_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["tt_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["tt_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["tt_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["tt_m_vis"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["tt_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["tt_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["tt_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["tt_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["tt_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["tt_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["tt_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["tt_phi_1"] = "$\\mathrm{Leading} Tau \\phi$"
			self.labels_dict["tt_phi_2"] = "$\\mathrm{Trailing} Tau \\phi$"
			self.labels_dict["tt_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["tt_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["tt_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["tt_pt_1"] = "$\\mathrm{Leading} Tau \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["tt_pt_2"] = "$\\mathrm{Trailing} Tau \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["tt_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["tt_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["tt_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["tt_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["tt_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["tt_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["tt_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["tt_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["tt_metProjectionPhi"] = "$\\nu_{\\phi}$"
			self.labels_dict["tt_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["tt_trigweight_1"] = "$\\mathrm{Leading} Tau \\mathrm{Trigger} Weight$"
			self.labels_dict["tt_trigweight_2"] = "$\\mathrm{Trailing} Tau \\mathrm{Trigger} Weight$"
			self.labels_dict["tt_pZetaMissVis"] = "$\\left(\\mathrm{p}^{\\mathrm{miss}}_{\\zeta}\\,\\minus 0.85 \\mathrm{p}^{\\mathrm{vis}}_{\\zeta}\\right) / \\mathrm{GeV}$"
			self.labels_dict["tt_pzetamiss"] = "$\\mathrm{p}^{\\mathrm{miss}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["tt_pzetavis"] = "$\\mathrm{p}^{\\mathrm{vis}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["mt_decayMode_2"] = "$\\mathrm{Tau} DM$"
			self.labels_dict["mt_eta_1"] = "$\\mathrm{Muon}\\,\\eta$"
			self.labels_dict["mt_eta_2"] = "$\\mathrm{Tau}\\,\\eta$"
			self.labels_dict["mt_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["mt_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mt_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["mt_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["mt_iso_1"] = "$\\mathrm{Muon}\\,\\mathrm{Isolation}$"
			self.labels_dict["mt_iso_2"] = "$\\mathrm{Tau}\\,\\mathrm{Isolation}$"
			self.labels_dict["mt_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["mt_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["mt_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["mt_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["mt_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["mt_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["mt_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mt_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mt_m_1"] = "$\\mathrm{Muon}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["mt_m_2"] = "$\\mathrm{Tau}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["mt_m_ll"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["mt_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["mt_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["mt_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["mt_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["mt_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["mt_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\mu, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["mt_mt_2"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\tau, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["mt_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\mu, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["mt_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["mt_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["mt_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mt_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mt_m_vis"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["mt_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mt_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mt_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mt_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["mt_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["mt_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["mt_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["mt_phi_1"] = "$\\mathrm{Muon}\\,\\phi$"
			self.labels_dict["mt_phi_2"] = "$\\mathrm{Tau}\\,\\phi$"
			self.labels_dict["mt_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["mt_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mt_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["mt_pt_1"] = "$\\mathrm{Muon} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mt_pt_2"] = "$\\mathrm{Tau} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mt_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["mt_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mt_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["mt_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["mt_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["mt_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["mt_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["mt_trigweight_1"] = "$\\mathrm{Muon} Trigger \\mathrm{Weight}$"
			self.labels_dict["mt_trigweight_2"] = "$\\mathrm{Tau} Trigger \\mathrm{Weight}$"
			self.labels_dict["mt_pZetaMissVis"] = "$\\left(\\mathrm{p}^{\\mathrm{miss}}_{\\zeta}\\,\\minus 0.85 \\mathrm{p}^{\\mathrm{vis}}_{\\zeta}\\right) / \\mathrm{GeV}$"
			self.labels_dict["mt_pzetamiss"] = "$\\mathrm{p}^{\\mathrm{miss}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["mt_pzetavis"] = "$\\mathrm{p}^{\\mathrm{vis}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["mt_pZetaMiss"] = "$\\mathrm{p}^{\\mathrm{miss}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["mt_pZetaVis"] = "$\\mathrm{p}^{\\mathrm{vis}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["mt_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["mt_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["mt_metProjectionPhi"] = "$\\nu_{\\phi}$"
			self.labels_dict["et_decayMode_2"] = "$\\mathrm{Tau} DM$"
			self.labels_dict["et_eta_1"] = "$\\mathrm{Electron}\\,\\eta$"
			self.labels_dict["et_eta_2"] = "$\\mathrm{Tau}\\,\\eta$"
			self.labels_dict["et_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["et_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["et_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["et_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["et_iso_1"] = "$\\mathrm{Electron}\\,\\mathrm{Isolation}$"
			self.labels_dict["et_iso_2"] = "$\\mathrm{Tau}\\,\\mathrm{Isolation}$"
			self.labels_dict["et_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["et_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["et_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["et_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["et_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["et_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["et_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["et_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["et_m_1"] = "$\\mathrm{Electron}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["et_m_2"] = "$\\mathrm{Tau}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["et_m_ll"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["et_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["et_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["et_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["et_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["et_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["et_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["et_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["et_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["et_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["et_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["et_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["et_m_vis"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["et_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["et_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["et_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["et_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["et_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["et_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["et_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["et_phi_1"] = "$\\mathrm{Electron}\\,\\phi$"
			self.labels_dict["et_phi_2"] = "$\\mathrm{Tau}\\,\\phi$"
			self.labels_dict["et_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["et_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["et_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["et_pt_1"] = "$\\mathrm{Electron} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["et_pt_2"] = "$\\mathrm{Tau} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["et_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["et_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["et_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["et_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["et_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["et_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["et_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["et_trigweight_1"] = "$\\mathrm{Electron} Trigger \\mathrm{Weight}$"
			self.labels_dict["et_trigweight_2"] = "$\\mathrm{Tau} Trigger \\mathrm{Weight}$"
			self.labels_dict["et_pZetaMissVis"] = "$\\left(\\mathrm{p}^{\\mathrm{miss}}_{\\zeta}\\,\\minus 0.85 \\mathrm{p}^{\\mathrm{vis}}_{\\zeta}\\right) / \\mathrm{GeV}$"
			self.labels_dict["et_pzetamiss"] = "$\\mathrm{p}^{\\mathrm{miss}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["et_pzetavis"] = "$\\mathrm{p}^{\\mathrm{vis}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["et_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["et_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["et_metProjectionPhi"] = "$\\nu_{\\phi}$"
			self.labels_dict["em_eta_1"] = "$\\mathrm{Electron}\\,\\eta$"
			self.labels_dict["em_eta_2"] = "$\\mathrm{Muon}\\,\\eta$"
			self.labels_dict["em_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["em_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["em_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["em_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["em_iso_1"] = "$\\mathrm{Electron}\\,\\mathrm{Isolation}$"
			self.labels_dict["em_iso_2"] = "$\\mathrm{Muon}\\,\\mathrm{Isolation}$"
			self.labels_dict["em_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["em_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["em_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["em_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["em_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["em_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["em_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["em_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["em_m_1"] = "$\\mathrm{Electron}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["em_m_2"] = "$\\mathrm{Muon}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["em_m_ll"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["em_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["em_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["em_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["em_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["em_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["em_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["em_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["em_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["em_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["em_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["em_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["em_m_vis"] = "$\\mathrm{Visible}\\, \\mathrm{di}-\\tau\\,\\mathrm{mass} / \\mathrm{GeV}$"
			self.labels_dict["em_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["em_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["em_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["em_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["em_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["em_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["em_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["em_phi_1"] = "$\\mathrm{Electron}\\,\\phi$"
			self.labels_dict["em_phi_2"] = "$\\mathrm{Muon}\\,\\phi$"
			self.labels_dict["em_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["em_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["em_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["em_pt_1"] = "$\\mathrm{Electron} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["em_pt_2"] = "$\\mathrm{Muon} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["em_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["em_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["em_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["em_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["em_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["em_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["em_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["em_trigweight_1"] = "$\\mathrm{Electron} Trigger \\mathrm{Weight}$"
			self.labels_dict["em_trigweight_2"] = "$\\mathrm{Muon} Trigger \\mathrm{Weight}$"
			self.labels_dict["em_pZetaMissVis"] = "$\\left(\\mathrm{p}^{\\mathrm{miss}}_{\\zeta}\\,\\minus 0.85 \\mathrm{p}^{\\mathrm{vis}}_{\\zeta}\\right) / \\mathrm{GeV}$"
			self.labels_dict["em_pzetamiss"] = "$\\mathrm{p}^{\\mathrm{miss}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["em_pzetavis"] = "$\\mathrm{p}^{\\mathrm{vis}}_{\\zeta} / \\mathrm{GeV}$"
			self.labels_dict["em_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["em_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["em_metProjectionPhi"] = "$\\nu_{\\phi}$"
			self.labels_dict["mm_eta_1"] = "$\\mathrm{Leading} Muon \\eta$"
			self.labels_dict["mm_eta_2"] = "$\\mathrm{Trailing} Muon \\eta$"
			self.labels_dict["mm_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["mm_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mm_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["mm_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["mm_iso_1"] = "$\\mathrm{Leading} Muon \\mathrm{Isolation}$"
			self.labels_dict["mm_iso_2"] = "$\\mathrm{Trailing} Muon \\mathrm{Isolation}$"
			self.labels_dict["mm_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["mm_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["mm_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["mm_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["mm_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["mm_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["mm_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mm_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mm_m_1"] = "$\\mathrm{Leading} Muon \\mathrm{Mass} / \\mathrm{GeV}$"
			self.labels_dict["mm_m_2"] = "$\\mathrm{Trailing} Muon \\mathrm{Mass} / \\mathrm{GeV}$"
			self.labels_dict["mm_m_ll"] = "$\\mathrm{Di}-muon \\mathrm{Mass} m_{\\mu\\mu} / \\mathrm{GeV}$"
			self.labels_dict["mm_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["mm_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["mm_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["mm_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["mm_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["mm_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\mu, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["mm_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (\\mu, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["mm_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["mm_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["mm_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mm_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["mm_m_vis"] = "$\\mathrm{Di}-muon \\mathrm{Mass} m_{\\mu\\mu} / \\mathrm{GeV}$"
			self.labels_dict["mm_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mm_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mm_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["mm_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["mm_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["mm_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["mm_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["mm_phi_1"] = "$\\mathrm{Leading} Muon \\phi$"
			self.labels_dict["mm_phi_2"] = "$\\mathrm{Trailing} Muon \\phi$"
			self.labels_dict["mm_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["mm_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mm_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["mm_pt_1"] = "$\\mathrm{Leading} Muon \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mm_pt_2"] = "$\\mathrm{Trailing} Muon \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["mm_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["mm_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["mm_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["mm_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["mm_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["mm_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["mm_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["mm_trigweight_1"] = "$\\mathrm{Leading} Muon \\mathrm{Trigger} Weight$"
			self.labels_dict["mm_trigweight_2"] = "$\\mathrm{Trailing} Muon \\mathrm{Trigger} Weight$"
			self.labels_dict["mm_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["mm_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["mm_metProjectionPhi"] = "$\\nu_{\\phi}$"
			self.labels_dict["ee_eta_1"] = "$\\mathrm{Electron}\\,\\eta$"
			self.labels_dict["ee_eta_2"] = "$\\mathrm{Muon}\\,\\eta$"
			self.labels_dict["ee_eta_ll"] = "$\\eta^{\\ell\\ell}$"
			self.labels_dict["ee_eta_llmet"] = "$\\eta^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["ee_eta_sv"] = "$\\mathrm{SVfit}\\,\\eta(\\tau\\tau)$"
			self.labels_dict["ee_integral"] = "$\\mathrm{Integral}$"
			self.labels_dict["ee_iso_1"] = "$\\mathrm{Electron}\\,\\mathrm{Isolation}$"
			self.labels_dict["ee_iso_2"] = "$\\mathrm{Muon}\\,\\mathrm{Isolation}$"
			self.labels_dict["ee_jdeta"] = "$\\Delta\\eta_{\\mathrm{jj}}$"
			self.labels_dict["ee_jdphi"] = "$\\Delta\\phi_{\\mathrm{jj}}$"
			self.labels_dict["ee_jeta_1"] = "$\\mathrm{Leading} Jet \\eta$"
			self.labels_dict["ee_jeta_2"] = "$\\mathrm{Trailing} Jet \\eta$"
			self.labels_dict["ee_jphi_1"] = "$\\mathrm{Leading} Jet \\phi$"
			self.labels_dict["ee_jphi_2"] = "$\\mathrm{Trailing} Jet \\phi$"
			self.labels_dict["ee_jpt_1"] = "$\\mathrm{Leading} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["ee_jpt_2"] = "$\\mathrm{Trailing} Jet \\mathrm{p}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["ee_m_1"] = "$\\mathrm{Electron}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["ee_m_2"] = "$\\mathrm{electron}\\,\\mathrm{Mass}\\,/ \\mathrm{GeV}$"
			self.labels_dict["ee_m_ll"] = "$\\mathrm{Di}-electron \\mathrm{Mass} m_{\\mathrm{ee}} / \\mathrm{GeV}$"
			self.labels_dict["ee_m_llmet"] = "$\\mathrm{m}_{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["ee_m_sv"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["ee_met"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}$"
			self.labels_dict["ee_metcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_metcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_metcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_metcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_metphi"] = "$\\mathrm{PFlow}\\,\\slash{\\mathrm{E}}_{\\mathrm{T}}\\,\\phi$"
			self.labels_dict["ee_mjj"] = "$\\mathrm{Di}-jet \\mathrm{Mass} m_{\\mathrm{jj}} / \\mathrm{GeV}$"
			self.labels_dict["ee_mt_1"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["ee_mt_lep1met"] = "$\\mathrm{Transverse}\\,\\mathrm{Mass}\\,\\mathrm{m}_{\\mathrm{T}} (e, \\slash{\\mathrm{E}}_{\\mathrm{T}}) / \\mathrm{GeV}$"
			self.labels_dict["ee_mt_ll"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["ee_mt_llmet"] = "$\\mathrm{m}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}} / \\mathrm{GeV}$"
			self.labels_dict["ee_mvacov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvacov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvacov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvacov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvamet"] = "$\\slash{\\mathrm{E}}_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["ee_mvametcov00"] = "$\\mathrm{Cov}_{0,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvametcov01"] = "$\\mathrm{Cov}_{0,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvametcov10"] = "$\\mathrm{Cov}_{1,0}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvametcov11"] = "$\\mathrm{Cov}_{1,1}(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_mvametphi"] = "$\\phi(\\slash{\\mathrm{E}}_{\\mathrm{T}})$"
			self.labels_dict["ee_m_vis"] = "$\\mathrm{Di}-electron \\mathrm{Mass} m_{\\mathrm{e}} / \\mathrm{GeV}$"
			self.labels_dict["ee_nJets30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["ee_njetspt30"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["ee_njets"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{Jets}$"
			self.labels_dict["ee_nbtag"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{b}-\\mathrm{tagged}\\,\\mathrm{Jets}$"
			self.labels_dict["ee_njetingap"] = "$\\mathrm{Number}\\,\\mathrm{of}\\,\\mathrm{central}\\,\\mathrm{Jets}$"
			self.labels_dict["ee_npu"] = "$\\mathrm{NPU}$"
			self.labels_dict["ee_npv"] = "$\\mathrm{NPV}$"
			self.labels_dict["ee_phi_1"] = "$\\mathrm{Electron}\\,\\phi$"
			self.labels_dict["ee_phi_2"] = "$\\mathrm{Muon}\\,\\phi$"
			self.labels_dict["ee_phi_ll"] = "$\\phi^{\\ell\\ell}$"
			self.labels_dict["ee_phi_llmet"] = "$\\phi^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["ee_phi_sv"] = "$\\mathrm{SVfit}\\,\\phi(\\tau\\tau)$"
			self.labels_dict["ee_pt_1"] = "$\\mathrm{Electron} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["ee_pt_2"] = "$\\mathrm{Muon} p_{\\mathrm{T}} / \\mathrm{GeV}$"
			self.labels_dict["ee_pt_ll"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell} / \\mathrm{GeV}$"
			self.labels_dict["ee_pt_llmet"] = "$\\mathrm{p}_{\\mathrm{T}}^{\\ell\\ell,\\mathrm{MEt}}$"
			self.labels_dict["ee_pt_sv"] = "$\\mathrm{SVfit} p_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["ee_pt_tt"] = "$\\mathrm{p}_{\\mathrm{T}}(\\tau\\tau) / \\mathrm{GeV}$"
			self.labels_dict["ee_puweight"] = "$\\mathrm{PU} Weight$"
			self.labels_dict["ee_rho"] = "$\\mathrm{rho}$"
			self.labels_dict["ee_svfitMass"] = "$\\mathrm{Di}-\\tau \\mathrm{Mass} m_{\\tau\\tau} / \\mathrm{GeV}$"
			self.labels_dict["ee_trigweight_1"] = "$\\mathrm{Electron} Trigger \\mathrm{Weight}$"
			self.labels_dict["ee_trigweight_2"] = "$\\mathrm{Muon} Trigger \\mathrm{Weight}$"
			self.labels_dict["ee_metProjectionPar"] = "$\\nu_{\\parallel} / \\mathrm{GeV}$"
			self.labels_dict["ee_metProjectionPerp"] = "$\\nu_{\\perp}  / \\mathrm{GeV}$"
			self.labels_dict["ee_metProjectionPhi"] = "$\\nu_{\\phi}$"
			for ch in ["ee_", "em_", "et_", "mm_", "mt_", "tt_"]:
				self.labels_dict[ch+"TrainingSelectionValue"] = "N-Fold Split Variable"
				self.labels_dict[ch+"all_vs_all"] = "$\\mathrm{BDT}_{\\mathrm{all}}^{\\mathrm{all}}$"
				self.labels_dict[ch+"all_vs_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{all}}$"
				self.labels_dict[ch+"all_vs_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{all}}$"
				self.labels_dict[ch+"ggh_vs_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{ggh}}$"
				self.labels_dict[ch+"ggh_vs_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{ggH}}$"
				self.labels_dict[ch+"glu_vs_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{ggh}}$"
				self.labels_dict[ch+"glu_vs_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{ggH}}$"
				self.labels_dict[ch+"vbf_vs_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{vbf}}$"
				self.labels_dict[ch+"vbf_vs_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{vbf}}$"
			self.labels_dict["BDT_all_all"] = "$\\mathrm{BDT}_{\\mathrm{all}}^{\\mathrm{all}}$"
			self.labels_dict["BDT_all_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{all}}$"
			self.labels_dict["BDT_all_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{all}}$"
			self.labels_dict["BDT_ggh_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{ggh}}$"
			self.labels_dict["BDT_ggh_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{ggH}}$"
			self.labels_dict["BDT_vbf_zll"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow \\ell\\ell}^{\\mathrm{vbf}}$"
			self.labels_dict["BDT_vbf_ztt"] = "$\\mathrm{BDT}_{\\mathrm{Z}\\rightarrow\\tau\\tau}^{\\mathrm{vbf}}$"
			for higgs_mass in xrange(90, 161, 5):
				self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy_ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy_ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["qqh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["qqh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["vh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["vh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["wh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["wh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["zh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["zh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpeven"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpmix{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpmix"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpodd"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susycpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susycpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd_alt"].replace("H", "H({mass:d})".format(mass=higgs_mass))

				for scale in [10, 25, 100, 250]:
					self.labels_dict["htt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["htt"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["ggh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["gghsm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghsm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghmm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghmm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghps{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghps125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhusm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhusm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhumm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhumm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["gghjhups{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["gghjhups125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["susy_ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy_ggh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susy{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["qqh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["qqhsm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhsm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhmm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhmm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhps{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhps125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhusm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhusm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhumm{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhumm125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["qqhjhups{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqhjhups125"]+" (#times {scale:d})".format(scale=scale)
					self.labels_dict["vh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["vh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpeven"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpmix{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpmix"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd_alt"]+" (\\times {scale:d})".format(scale=scale)
					
			for higgs_mass in xrange(90, 3201, 10):
				self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy_ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy_ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susy{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susy"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpeven{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpeven"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpmix{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpmix"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["httcpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["httcpodd"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susycpodd{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				self.labels_dict["susycpodd_alt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["susycpodd_alt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
				for scale in [10, 25, 100, 250]:
					self.labels_dict["htt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["htt"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["ggh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susy_ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy_ggh"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susy{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susy"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpeven{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpeven"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpmix{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpmix"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["httcpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["httcpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd"]+" (\\times {scale:d})".format(scale=scale)
					self.labels_dict["susycpodd_alt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["susycpodd_alt"]+" (\\times {scale:d})".format(scale=scale)

		self.labels_dict["data_obs"] = "Observed"
		self.labels_dict["ttj"] = self.labels_dict["tt"]
		self.labels_dict["ttbar"] = self.labels_dict["tt"]
		self.labels_dict["wjets"]  = self.labels_dict["wj"]
		self.labels_dict["w"]  = self.labels_dict["wj"]
		self.labels_dict["dibosons"]  = self.labels_dict["vv"]
		self.labels_dict["fakes"] = self.labels_dict["qcd"]
		self.labels_dict["qcdwj"] = self.labels_dict["qcd"]
		self.labels_dict["totalsig"] = self.labels_dict["htt"]

		#for higgs_mass in xrange(90, 161, 5):
			#self.labels_dict["htt{mass:d}".format(mass=higgs_mass)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			#self.labels_dict["ggh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			#self.labels_dict["qqh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["qqh"].replace("H", "H({mass:d})".format(mass=higgs_mass))
			#self.labels_dict["vh{mass:d}".format(mass=higgs_mass)] = self.labels_dict["vh"].replace("H", "H({mass:d})".format(mass=higgs_mass))

			#for scale in [10, 25, 100, 250]:
				#self.labels_dict["htt{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["htt"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
				#self.labels_dict["ggh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["ggh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
				#self.labels_dict["qqh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["qqh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
				#self.labels_dict["vh{mass:d}_{scale:d}".format(mass=higgs_mass, scale=scale)] = self.labels_dict["vh"].replace("H", "H({mass:d})".format(mass=higgs_mass))+" (\\times {scale:d})".format(scale=scale)
