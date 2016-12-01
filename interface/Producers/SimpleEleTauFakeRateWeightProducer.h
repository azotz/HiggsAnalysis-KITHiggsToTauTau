
#pragma once

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"

/**
   \brief SimpleEleTauFakeRateWeightProducer
   Config tags:
   - Fill me with something meaningful

*/

class SimpleEleTauFakeRateWeightProducer : public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;

	SimpleEleTauFakeRateWeightProducer();
	SimpleEleTauFakeRateWeightProducer(std::vector<float>& (setting_type::*GetSimpleEleTauFakeRateWeightVLoose)(void) const,
									  std::vector<float>& (setting_type::*GetSimpleEleTauFakeRateWeightTight)(void) const);

	std::string GetProducerId() const override;

	virtual void Init(setting_type const& settings) override;

	void Produce(event_type const& event, product_type& product,
				 setting_type const& settings) const override;
private:

	// the weights within each vector should be ordered by increasing |eta| in your json config
	// with lowest |eta| being the first entry and highest |eta| the last one
	std::vector<float>& (setting_type::*GetSimpleEleTauFakeRateWeightVLoose)(void) const;
	std::vector<float>& (setting_type::*GetSimpleEleTauFakeRateWeightTight)(void) const;

	std::vector<float> SimpleEleTauFakeRateWeightVLoose;
	std::vector<float> SimpleEleTauFakeRateWeightTight;
};
