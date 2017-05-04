
#pragma once

#include "Artus/KappaAnalysis/interface/Producers/TauCorrectionsProducer.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"


/**
   \brief Producer for tau energy scale corrections (Htt version).
   
   Required config tags
   - TauEnergyCorrection (possible value: summer2013)
*/
class HttTauCorrectionsProducer: public TauCorrectionsProducer
{

public:

	typedef KappaEvent event_type;
	typedef KappaProduct product_type;
	typedef KappaSettings setting_type;
	typedef typename HttTypes::event_type spec_event_type;
	typedef typename HttTypes::product_type spec_product_type;
	typedef typename HttTypes::setting_type spec_setting_type;

	enum class TauEnergyCorrection : int
	{
		NONE  = -1,
		SUMMER2013 = 0,
		NEWTAUID = 1,
		SMHTT2016,
		MSSMHTT2016,
	};
	static TauEnergyCorrection ToTauEnergyCorrection(std::string const& tauEnergyCorrection)
	{
		if (tauEnergyCorrection == "summer2013") return TauEnergyCorrection::SUMMER2013;
		else if (tauEnergyCorrection == "newtauid") return TauEnergyCorrection::NEWTAUID;
		else if (tauEnergyCorrection == "smhtt2016") return TauEnergyCorrection::SMHTT2016;
		else if (tauEnergyCorrection == "mssmhtt2016") return TauEnergyCorrection::MSSMHTT2016;
		else return TauEnergyCorrection::NONE;
	}
	
	virtual void Init(setting_type const& settings) override;


protected:

	// Htt type tau energy corrections
	virtual void AdditionalCorrections(KTau* tau, event_type const& event,
	                                   product_type& product, setting_type const& settings) const override;


private:
	TauEnergyCorrection tauEnergyCorrection;

};

