
#pragma once

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"
#include "Artus/KappaAnalysis/interface/KappaProducerBase.h"
#include "HTTutilities/Jet2TauFakes/interface/FakeFactor.h"
#include <boost/regex.hpp>


#if ROOT_VERSION_CODE < ROOT_VERSION(6,0,0)
#include <TROOT.h>
#endif

/**
   \brief JetToTauFakesProducer
   Config tags:
   
    Run this producer after the Run2DecayModeProducer

*/

class JetToTauFakesProducer : public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;
	
	virtual ~JetToTauFakesProducer();
	
	virtual std::string GetProducerId() const override;

	virtual void Init(setting_type const& settings) override;

	void Produce(event_type const& event, product_type& product,
                 setting_type const& settings) const override;
private:

	std::map<std::string,std::shared_ptr<FakeFactor>> m_ffComb;
	bool m_applyFakeFactors;
	bool m_isET;
	bool m_isMT;
	bool m_isTT;
};
