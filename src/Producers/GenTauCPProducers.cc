

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/GenTauCPProducers.h"

#include "Artus/Consumer/interface/LambdaNtupleConsumer.h"
#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/KappaAnalysis/interface/Utility/GenParticleDecayTree.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/CPQuantities.h"


void GenTauCPProducerBase::Init(setting_type const& settings)
{
	ProducerBase<HttTypes>::Init(settings);
	
	// add possible quantities for the lambda ntuples consumers
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStarCP", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStarCP;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiCP", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiCP;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStar", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStar;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhi", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhi;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("TauMProngEnergy", [](event_type const& event, product_type const& product)
	{
		return product.m_genChargedProngEnergies.first;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("TauPProngEnergy", [](event_type const& event, product_type const& product)
	{
		return product.m_genChargedProngEnergies.second;
	});
	// charged particles of a one-prong
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("Tau1OneProngsSize", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genBosonTree.m_daughters.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0))? product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("Tau2OneProngsSize", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0))? product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1PdgId", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->pdgId : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Pt", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Pt() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Pz", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Pz() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Eta", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Eta() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Phi", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Phi() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Mass", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.mass() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Energy", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.E() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2PdgId", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->pdgId : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Pt", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Pt() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Pz", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Pz() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Eta", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Eta() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Phi", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Phi() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Mass", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.mass() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Energy", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != 0) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.E() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genZPlus", [](event_type const& event, product_type const& product)
	{
		return product.m_genZPlus;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genZMinus", [](event_type const& event, product_type const& product)
	{
		return product.m_genZMinus;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genZs", [](event_type const& event, product_type const& product)
	{
		return product.m_genZs;
	});
}

void GenTauCPProducerBase::Produce(event_type const& event, product_type& product,
                                   setting_type const& settings) const
{
	// A generator level boson and its decay products must exist
	// The boson is searched for by a GenBosonProducer
	// and the decay tree is built by the GenTauDecayProducer
	assert(product.m_genBosonLVFound);
	assert(product.m_genBosonTree.m_daughters.size() > 1);
	
	GenParticleDecayTree* selectedTau1;
	GenParticleDecayTree* selectedTau2;
	if (product.m_genBosonTree.m_daughters[0].m_genParticle->charge() == +1){
		selectedTau1 = &(product.m_genBosonTree.m_daughters[0]);
		selectedTau2 = &(product.m_genBosonTree.m_daughters[1]);
	}
	else {
		selectedTau1 = &(product.m_genBosonTree.m_daughters[1]);
		selectedTau2 = &(product.m_genBosonTree.m_daughters[0]);
	}


	selectedTau1->CreateFinalStateProngs(selectedTau1);
	selectedTau2->CreateFinalStateProngs(selectedTau2);
	std::vector<GenParticleDecayTree*> selectedTau1OneProngs = selectedTau1->m_finalStateOneProngs;
	std::vector<GenParticleDecayTree*> selectedTau2OneProngs = selectedTau2->m_finalStateOneProngs;

	// Defining CPQuantities object to use variables and functions of this class
	CPQuantities cpq;
	
	//Selection of the right channel for phi, phi* and psi*CP
	if ((std::abs(selectedTau1->m_genParticle->pdgId) == DefaultValues::pdgIdTau) &&
	    (std::abs(selectedTau2->m_genParticle->pdgId) == DefaultValues::pdgIdTau) &&
	    (selectedTau1OneProngs.size() != 0) &&
	    (selectedTau2OneProngs.size() != 0))
	{
		//Initialization of charged particles
		KGenParticle* chargedPart1 = selectedTau1OneProngs[0]->m_genParticle;
		KGenParticle* chargedPart2 = selectedTau2OneProngs[0]->m_genParticle;
		for (unsigned int i = 0; i < selectedTau1OneProngs.size(); i++)
		{
			if (abs(selectedTau1OneProngs[i]->GetCharge()) == 1) chargedPart1 = selectedTau1OneProngs[i]->m_genParticle;
		}
		for (unsigned int i = 0; i < selectedTau2OneProngs.size(); i++)
		{
			if (abs(selectedTau2OneProngs[i]->GetCharge()) == 1) chargedPart2 = selectedTau2OneProngs[i]->m_genParticle;
		}
		// Saving the charged particles for  analysis
		product.m_genOneProngCharged1 = chargedPart1;
		product.m_genOneProngCharged2 = chargedPart2;
		// Saving Energies of charged particles in tau rest frames
		product.m_genChargedProngEnergies.first = cpq.CalculateChargedProngEnergy(selectedTau1->m_genParticle->p4, chargedPart1->p4);
		product.m_genChargedProngEnergies.second = cpq.CalculateChargedProngEnergy(selectedTau2->m_genParticle->p4, chargedPart2->p4);
		// Calculation of Phi* and Phi*CP itself
		double genPhiStarCP = cpq.CalculatePhiStarCP(selectedTau1->m_genParticle->p4, selectedTau2->m_genParticle->p4, chargedPart1->p4, chargedPart2->p4);
		product.m_genPhiStar = cpq.GetGenPhiStar();
		// Calculation of the angle Phi as angle betweeen normal vectors of Tau- -> Pi- and Tau+ -> Pi+ 
		// decay planes 
		double genPhiCP = cpq.CalculatePhiCP(product.m_genBosonLV, selectedTau1->m_genParticle->p4, selectedTau2->m_genParticle->p4, chargedPart1->p4, chargedPart2->p4);
		product.m_genPhi = cpq.GetGenPhi();

		//CPTransformation for semileptonic case
		if (settings.GetPhiTransform() == true && (((chargedPart1->pdgId == DefaultValues::pdgIdElectron || chargedPart1->pdgId == DefaultValues::pdgIdMuon) && (chargedPart2->pdgId == 211)) || ((chargedPart2->pdgId == -DefaultValues::pdgIdElectron || chargedPart2->pdgId == -DefaultValues::pdgIdMuon) && (chargedPart1->pdgId == -211))))
		{	
			product.m_genPhiStarCP = cpq.PhiTransform(genPhiStarCP);
			product.m_genPhiCP = cpq.PhiTransform(genPhiCP);
		}
		else
		{
			product.m_genPhiStarCP = genPhiStarCP;
			product.m_genPhiCP = genPhiCP;
		}
		//ZPlusMinus calculation
		product.m_genZPlus = cpq.CalculateZPlusMinus(product.m_genBosonLV, chargedPart1->p4);
		product.m_genZMinus = cpq.CalculateZPlusMinus(product.m_genBosonLV, chargedPart2->p4);
		product.m_genZs = cpq.CalculateZs(product.m_genZPlus, product.m_genZMinus);
	}
}

	
std::string GenTauCPProducer::GetProducerId() const
{
	return "GenTauCPProducer";
}

void GenTauCPProducer::Init(setting_type const& settings)
{
	GenTauCPProducerBase::Init(settings);
}

void GenTauCPProducer::Produce(event_type const& event, product_type& product,
                               setting_type const& settings) const
{
	GenTauCPProducerBase::Produce(event, product, settings);
}


std::string GenMatchedTauCPProducer::GetProducerId() const
{
	return "GenMatchedTauCPProducer";
}

void GenMatchedTauCPProducer::Init(setting_type const& settings)
{
	GenTauCPProducerBase::Init(settings);
}

void GenMatchedTauCPProducer::Produce(event_type const& event, product_type& product,
                                      setting_type const& settings) const
{
	// A generator level boson and its decay products must exist
	// The boson is searched for by a GenBosonProducer
	// and the decay tree is built by the GenTauDecayProducer
	assert(product.m_genBosonLVFound);
	assert(product.m_genBosonTree.m_daughters.size() > 1);
	
	// find the correct gen taus (i.e. the genBoson daughters)
	if (product.m_genBosonTree.m_daughters[0].m_genParticle->status() != 2|| product.m_genBosonTree.m_daughters[1].m_genParticle->status() != 2){
		FindGenTau(product);
	}

	// get the taus: the tau1 is always the positevely charged tau
	GenParticleDecayTree* selectedTau1;
	GenParticleDecayTree* selectedTau2;
	if (product.m_genBosonTree.m_daughters[0].m_genParticle->charge() == +1){
		selectedTau1 = &(product.m_genBosonTree.m_daughters[0]);
		selectedTau2 = &(product.m_genBosonTree.m_daughters[1]);
	}
	else {
		selectedTau1 = &(product.m_genBosonTree.m_daughters[1]);
		selectedTau2 = &(product.m_genBosonTree.m_daughters[0]);
	}

	// find the match between the gen tau (or its daughters)
	// and the leptons saved in the GenLeptons collections
	// (that are gen particles matched with the reco particles)
	std::vector<GenParticleDecayTree> tau1Daughters = selectedTau1->m_daughters;
	std::vector<GenParticleDecayTree> tau2Daughters = selectedTau2->m_daughters;
	std::vector<KGenParticle*> matchedLep = product.m_chargeOrderedGenLeptons;
	bool tau1Match = false;
	bool tau2Match = false;
	bool match0 = false; // boolean to check the match with matchedLep[0]
	bool match1 = false; // boolean to check the match with matchedLep[1]

	// search for a match only if the matched (gen-reco) collection exists and has non-null components
	if (matchedLep[0] && matchedLep[1]){
		// if the selectedTau decays leptonically,
		// search for the match between selectedTau daughters and matchedLep
		if ((int)selectedTau1->m_decayMode == 1 || (int)selectedTau1->m_decayMode == 2){
			for (std::vector<GenParticleDecayTree>::const_iterator Part = tau1Daughters.begin(); Part != tau1Daughters.end(); ++Part){
				if ( ROOT::Math::VectorUtil::DeltaR( (*Part).m_genParticle->p4,  matchedLep[0]->p4 ) < 0.001 ){
					match0 = true;
					tau1Match = true;
				}
				if ( ROOT::Math::VectorUtil::DeltaR( (*Part).m_genParticle->p4,  matchedLep[1]->p4 ) < 0.001 ){
					match1 = true;
					tau1Match = true;
				}
			}
		}
		// if the selectedTau decays hadronically,
		// search for the match between selectedTau and matchedLep
		else {
			if ( ROOT::Math::VectorUtil::DeltaR( selectedTau1->m_genParticle->p4,  matchedLep[0]->p4 ) < 0.001 ){
				match0 = true;
				tau1Match = true;
			}
			if ( ROOT::Math::VectorUtil::DeltaR( selectedTau1->m_genParticle->p4,  matchedLep[1]->p4 ) < 0.001 ){
				match1 = true;
				tau1Match = true;
			}
		}

		if ((int)selectedTau2->m_decayMode == 1 || (int)selectedTau2->m_decayMode == 2){
			for (std::vector<GenParticleDecayTree>::const_iterator Part = tau2Daughters.begin(); Part != tau2Daughters.end(); ++Part){
				if ( !match0 && ROOT::Math::VectorUtil::DeltaR( (*Part).m_genParticle->p4,  matchedLep[0]->p4 ) < 0.001 ){
					match0 = true;
					tau2Match = true;
				}
				if ( !match1 && ROOT::Math::VectorUtil::DeltaR( (*Part).m_genParticle->p4,  matchedLep[1]->p4 ) < 0.001 ){
					match1 = true;
					tau2Match = true;
				}
			}
		}
		else {
			if ( !match0 && ROOT::Math::VectorUtil::DeltaR( selectedTau2->m_genParticle->p4,  matchedLep[0]->p4 ) < 0.001 ){
				match0 = true;
				tau2Match = true;
			}
			if ( !match1 && ROOT::Math::VectorUtil::DeltaR( selectedTau2->m_genParticle->p4,  matchedLep[1]->p4 ) < 0.001 ){
				match1 = true;
				tau2Match = true;
			}
		}
	} // if matchedLep[0] && matchedLep[1]

	// Calculate the CP observables only if matchedLep components are non-null
	// and the match between selectedTaus and matchedLeptons was found
	if ( matchedLep[0] && matchedLep[1] && tau1Match && tau2Match ){
		selectedTau1->CreateFinalStateProngs(selectedTau1);
		selectedTau2->CreateFinalStateProngs(selectedTau2);
		std::vector<GenParticleDecayTree*> selectedTau1OneProngs = selectedTau1->m_finalStateOneProngs;
		std::vector<GenParticleDecayTree*> selectedTau2OneProngs = selectedTau2->m_finalStateOneProngs;

		// Defining CPQuantities object to use variables and functions of this class
		CPQuantities cpq;

		// Selection of the right channel for phi, phi* and psi*CP
		if ((std::abs(selectedTau1->m_genParticle->pdgId) == DefaultValues::pdgIdTau) &&
		    (std::abs(selectedTau2->m_genParticle->pdgId) == DefaultValues::pdgIdTau) &&
		    (selectedTau1OneProngs.size() != 0) &&
		    (selectedTau2OneProngs.size() != 0))
		{
			//Initialization of charged particles
			KGenParticle* chargedPart1 = selectedTau1OneProngs[0]->m_genParticle;
			KGenParticle* chargedPart2 = selectedTau2OneProngs[0]->m_genParticle;

			for (unsigned int i = 0; i < selectedTau1OneProngs.size(); i++)
			{
				if (abs(selectedTau1OneProngs[i]->GetCharge()) == 1) chargedPart1 = selectedTau1OneProngs[i]->m_genParticle;
			}
			for (unsigned int i = 0; i < selectedTau2OneProngs.size(); i++)
			{
				if (abs(selectedTau2OneProngs[i]->GetCharge()) == 1) chargedPart2 = selectedTau2OneProngs[i]->m_genParticle;
			}

			// Saving the charged particles for analysis
			product.m_genOneProngCharged1 = chargedPart1;
			product.m_genOneProngCharged2 = chargedPart2;

			// Saving energies of charged particles in tau rest frames
			product.m_genChargedProngEnergies.first = cpq.CalculateChargedProngEnergy(selectedTau1->m_genParticle->p4, chargedPart1->p4);
			product.m_genChargedProngEnergies.second = cpq.CalculateChargedProngEnergy(selectedTau2->m_genParticle->p4, chargedPart2->p4);

			// Calculation of Phi* and Phi*CP
			double genPhiStarCP = cpq.CalculatePhiStarCP(selectedTau1->m_genParticle->p4, selectedTau2->m_genParticle->p4, chargedPart1->p4, chargedPart2->p4);
			product.m_genPhiStar = cpq.GetGenPhiStar();

			// Calculation of Phi and PhiCP
			double genPhiCP = cpq.CalculatePhiCP(product.m_genBosonLV, selectedTau1->m_genParticle->p4, selectedTau2->m_genParticle->p4, chargedPart1->p4, chargedPart2->p4);
			product.m_genPhi = cpq.GetGenPhi();
	
			//CPTransformation for semileptonic case
			if (settings.GetPhiTransform() == true && (((chargedPart1->pdgId == DefaultValues::pdgIdElectron || chargedPart1->pdgId == DefaultValues::pdgIdMuon) && (chargedPart2->pdgId == 211)) || ((chargedPart2->pdgId == -DefaultValues::pdgIdElectron || chargedPart2->pdgId == -DefaultValues::pdgIdMuon) && (chargedPart1->pdgId == -211))))
			{	
				product.m_genPhiStarCP = cpq.PhiTransform(genPhiStarCP);
				product.m_genPhiCP = cpq.PhiTransform(genPhiCP);
			}
			else
			{
				product.m_genPhiStarCP = genPhiStarCP;
				product.m_genPhiCP = genPhiCP;
			}

			//ZPlusMinus calculation
			product.m_genZPlus = cpq.CalculateZPlusMinus(product.m_genBosonLV, chargedPart1->p4);
			product.m_genZMinus = cpq.CalculateZPlusMinus(product.m_genBosonLV, chargedPart2->p4);
			product.m_genZs = cpq.CalculateZs(product.m_genZPlus, product.m_genZMinus);
		} // if (selection of the right channel)

	} // if matchedLep is non-null and match was found
}

// This function is meant to find the gen taus (daughter of the genBoson) that have status=2
// Indeed, status!=2 means that the tau does not decay into leptons/hadrons, but emits a gamma.
// With this function, the decay tree of the tau is followed up, until the tau with status=2 is found
// Once found, the DetermineDecayMode function is called, in order to set the product member m_decayMode correctly
void GenMatchedTauCPProducer::FindGenTau(product_type& product) const
{

	GenParticleDecayTree newtau0 = nullptr;
	GenParticleDecayTree newtau1 = nullptr;

	if (product.m_genBosonTree.m_daughters[0].m_genParticle->status() != 2
		&& product.m_genBosonTree.m_daughters[0].m_daughters.size() != 0){
		for (std::vector<GenParticleDecayTree>::const_iterator Part = product.m_genBosonTree.m_daughters[0].m_daughters.begin();
		Part != product.m_genBosonTree.m_daughters[0].m_daughters.end(); ++Part){
			if ((*Part).m_genParticle->pdgId == product.m_genBosonTree.m_daughters[0].m_genParticle->pdgId){
				newtau0 = *Part;
			}
		}
		newtau0.DetermineDecayMode(&newtau0);
		product.m_genBosonTree.m_daughters[0] = newtau0;
	}

	if (product.m_genBosonTree.m_daughters[1].m_genParticle->status() != 2
		&& product.m_genBosonTree.m_daughters[1].m_daughters.size() != 0){
		for (std::vector<GenParticleDecayTree>::const_iterator Part = product.m_genBosonTree.m_daughters[1].m_daughters.begin();
		Part != product.m_genBosonTree.m_daughters[1].m_daughters.end(); ++Part){
			if ((*Part).m_genParticle->pdgId == product.m_genBosonTree.m_daughters[1].m_genParticle->pdgId){
				newtau1 = *Part;
			}
		}
		newtau1.DetermineDecayMode(&newtau1);
		product.m_genBosonTree.m_daughters[1] = newtau1;
	}

	if (product.m_genBosonTree.m_daughters[0].m_genParticle->status() == 2
		&& product.m_genBosonTree.m_daughters[1].m_genParticle->status() == 2){
	}
	else if (product.m_genBosonTree.m_daughters[0].m_daughters.size() != 0
		|| product.m_genBosonTree.m_daughters[1].m_daughters.size() != 0){
		FindGenTau(product);
	}
}


