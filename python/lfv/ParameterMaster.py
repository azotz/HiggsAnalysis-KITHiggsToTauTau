import os
import ConfigParser

###Enumeration classes for avaible parameter

class Parameter():
	m_vis = 0
	ptofsumdilep = 1
	mt_1 = 2
	mt_2 = 3
	number_jets = 4
	met = 5
	delta_phi = 6
	delta_phi_CM = 7
	delta_pt_jetdilep = 8
	pzeta = 9
	impact_1 = 10	
	impact_2 = 11
	sum_impact = 12
	limit = 13

class ParameterInfo():
	plot_info = 0
	label_info = 1
	cut_info = 2


##Class for storing information about the parameter for plotting and process all things about the parameter like reading out cut configs

class ParameterMaster(object):
	def __init__(self):
		self._Parameterinfo_libary = {
					ParameterInfo.plot_info:	self.__plotinfo__,
					ParameterInfo.label_info:	self.__labelinfo__,
					ParameterInfo.cut_info:		self.__cutinfo__
		}

	## Function saving information about the parameter

	def __plotinfo__(self):

		##Info saved as x_expression, x_bins, filename
		self._plotinfo = {
					Parameter.m_vis:		["m_vis", "100,0,170", "VisibleMass"],
					Parameter.ptofsumdilep:		["diLepLV.Pt()", "100,0,150", "PtOfMomentaSumDiLep"],
					Parameter.mt_1:			["mt_1", "100,0,200", "TransverseMass1"],
					Parameter.mt_2:			["mt_2", "100,0,200", "TransverseMass2"],
					Parameter.number_jets:		["njetspt30", "4,0,4", "NumberOfJets"], 
					Parameter.met:			["met", "100,0,140", "MissingTranverseEnergy"],
					Parameter.delta_phi:		["abs(abs(phi_1 - phi_2) - 3.14)", "100,0,3", "DeltaPhi"],
					Parameter.delta_phi_CM:		["abs(abs(lep1LV.BoostToCM().phi() - lep2LV.BoostToCM().phi()) - 3.14)", "100,0,3", "DeltaPhiCM"],
					Parameter.delta_pt_jetdilep:	["abs(diLepLV.Pt() -  leadingJetLV.Pt())", "100,0,150", "DeltaPtJetDilep"],
					Parameter.pzeta:		["pZetaMissVis", "100,-130,130", "PZeta"],
					Parameter.impact_1:		["abs(d0_1)", "100,0,0.02", "ImpactParameter1"],
					Parameter.impact_2:		["abs(d0_2)", "100,0,0.02", "ImpactParameter2"],
					Parameter.sum_impact:		["abs(d0_1 + d0_2)", "100,0,0.02", "SumOfImpactParameter"],
					Parameter.limit:		[["limit_exp:limit_exp-two_sigma_down:two_sigma_up-limit_exp", "limit_exp:limit_exp-one_sigma_down:one_sigma_up-limit_exp" , "limit_exp", "limit_obs"], "1,1,1", "limit"]
		}

	
		return self._plotinfo

	def __labelinfo__(self):
		self._labelinfo = {
					Parameter.m_vis:		"m_{vis}",
					Parameter.ptofsumdilep:		"(#sump^{#mu})_{T}",
					Parameter.mt_1:			"m_{T}",
					Parameter.mt_2:			"m_{T}",
					Parameter.number_jets:		"Number of jets",
					Parameter.met:			"#slash{E}_{T}",
					Parameter.delta_phi:		"||#Delta#phi| - #pi|",
					Parameter.delta_phi_CM:		"||#Delta#phi_{CM}| - #pi|",
					Parameter.delta_pt_jetdilep:	"|p_{T}(jet) - (#sump^{#mu})_{T}|",
					Parameter.pzeta:		"#left(p^{miss}_{#zeta} #minus 0.85 p^{vis}_{#zeta}#right)",
					Parameter.impact_1:		"|d_{0}|",
					Parameter.impact_2:		"|d_{0}|",
					Parameter.sum_impact:		"|#sum_{lepton} d_{0}_{lepton}|",
					Parameter.limit:		"95% CL Limit on BR(LFV)/BR(LFV)^{current}"
		}

		return self._labelinfo

	def __cutinfo__(self):
		self._cutinfo = {
					Parameter.ptofsumdilep:		"(diLepLV.Pt()<{cut})",
					Parameter.mt_1:			"(mt_1<{cut})",
					Parameter.mt_2:			"(mt_2<{cut})",
					Parameter.delta_phi:		"(abs(abs(phi_1 - phi_2) - 3.14)<{cut})",
					Parameter.met:			"(met<{cut})",
					Parameter.delta_phi_CM:		"(abs(abs(lep1LV.BoostToCM().phi() - lep2LV.BoostToCM().phi()) - 3.14)<{cut})",
					Parameter.delta_pt_jetdilep:	"(abs(diLepLV.Pt() -  leadingJetLV.Pt())<{cut})",
					Parameter.impact_1:		"(abs(d0_1)<{cut})",
					Parameter.impact_2:		"(abs(d0_2)<{cut})",
					Parameter.pzeta:		"(pZetaMissVis<{cut})"
		}

		return self._cutinfo


	##Returning wished parameter infomration

	def get_parameter_info(self, parameter, information):
		parameter_info = []

		##Fill info list checking if parameter/info are lists or integer 
		try:
			for info in information:
				try:
					for param in parameter:
						parameter_info.append(self._Parameterinfo_libary[info]()[param])

				except TypeError:
					parameter_info.append(self._Parameterinfo_libary[info]()[parameter])


		except TypeError:
			try:			
				for param in parameter:
					parameter_info.append(self._Parameterinfo_libary[information]()[param])
			
			except TypeError:
				parameter_info = self._Parameterinfo_libary[information]()[parameter]

		return parameter_info


	##Function writing and reading cut configs sectionwise

	def cutconfigwriter(self, path, filename, section, dictionary):
		if not os.path.exists(path):
			os.mkdir(path)
	
		ini_config = ConfigParser.ConfigParser()
		if os.path.exists(path + "/" + filename):
			ini_config.read(path + "/" + filename)
		ini_config.add_section(section)
	
		for (key, value) in dictionary.iteritems():
			ini_config.set(section, key, value)

		ini_file = open(path + "/" + filename, "w")
		ini_config.write(ini_file)
		ini_file.close()

		print "The cut information have been saved in " + filename + " under the section " + section + "."


	def cutconfigreader(self, filename, section):
		cut_config = ConfigParser.ConfigParser()
		cut_config.read(filename)

		cut_parameter = []
		cut_values = []

		for parameter, value in cut_config.items(section):
			cut_parameter.append(int(parameter))
			cut_values.append(value)
		
		return cut_parameter, cut_values

	
	##Sum weights of different parameter to get string using for harry plotter weight input

	def weightaddition(self, cut_strings, cut_values):
		weight = ""
		for index, (cut, value) in enumerate(zip(cut_strings, cut_values)):
			if index == 0:
				weight = cut.format(cut = value)

			else:
				weight = weight + "*" + cut.format(cut = value)

		return weight

	##Returns weight for harry plotter made from optimal cut parameters

	def weightmaster(self, filename):
		cut_parameter, cut_values = self.cutconfigreader(filename, "Iteration3")
		
		return self.weightaddition(self.get_parameter_info(cut_parameter,2), cut_values)




