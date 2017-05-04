

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/GenTauCPProducers.h"

#include "Artus/Consumer/interface/LambdaNtupleConsumer.h"
#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/KappaAnalysis/interface/Utility/GenParticleDecayTree.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/CPQuantities.h"


void GenTauCPProducerBase::Init(setting_type const& settings)
{
	ProducerBase<HttTypes>::Init(settings);

	// add possible quantities for the lambda ntuples consumers

	// MC-truth PV coordinates
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPVx", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genPV != nullptr) ? (product.m_genPV)->x() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPVy", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genPV != nullptr) ? (product.m_genPV)->y() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPVz", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genPV != nullptr) ? (product.m_genPV)->z() : DefaultValues::UndefinedFloat);
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStarCP", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStarCP;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStarCP_rho", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStarCP_rho;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiCP", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiCP;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiCP_rho", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiCP_rho;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStar", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStar;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhiStar_rho", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhiStar_rho;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhi", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhi;
	});

	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genPhi_rho", [](event_type const& event, product_type const& product)
	{
		return product.m_genPhi_rho;
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
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->pdgId : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Pt", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Pt() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Pz", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Pz() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Eta", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Eta() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Phi", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.Phi() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Mass", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.mass() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart1Energy", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged1 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged1->p4.E() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2PdgId", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->pdgId : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Pt", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Pt() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Pz", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Pz() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Eta", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Eta() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Phi", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.Phi() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Mass", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.mass() : DefaultValues::UndefinedDouble;
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("OneProngChargedPart2Energy", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genOneProngCharged2 != nullptr) && ((product.m_genBosonTree.m_daughters.size() > 1) && (product.m_genBosonTree.m_daughters[1].m_finalStateOneProngs.size() > 0) && (product.m_genBosonTree.m_daughters[0].m_finalStateOneProngs.size() > 0)))? product.m_genOneProngCharged2->p4.E() : DefaultValues::UndefinedDouble;
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
	if (product.m_genBosonLVFound && (product.m_genBosonTree.m_daughters.size() > 1))
	{

		// save MC-truth PV
		for (unsigned int i=0; i<event.m_genParticles->size(); ++i){
			if (event.m_genParticles->at(i).pdgId == 23 || event.m_genParticles->at(i).pdgId == 25 || event.m_genParticles->at(i).pdgId == 36){
				product.m_genPV = &event.m_genParticles->at(i).vertex;
			}
		}
	
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
			//KGenParticle* neutralPart1 = selectedTau1OneProngs[0]->m_genParticle;
			//KGenParticle* neutralPart2 = selectedTau2OneProngs[0]->m_genParticle;
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

			// rho method
			if (product.m_genBosonLVFound && product.m_genLeptonsFromBosonDecay.size() > 1 &&
				(std::abs(product.m_genLeptonsFromBosonDecay.at(0)->pdgId) == DefaultValues::pdgIdTau) &&
			(std::abs(product.m_genLeptonsFromBosonDecay.at(1)->pdgId) == DefaultValues::pdgIdTau))
			{
				//generate the Taus from the Boson decay
				KGenTau* genTau1 = SafeMap::GetWithDefault(product.m_validGenTausMap, product.m_genLeptonsFromBosonDecay.at(0), static_cast<KGenTau*>(nullptr));
				KGenTau* genTau2 = SafeMap::GetWithDefault(product.m_validGenTausMap, product.m_genLeptonsFromBosonDecay.at(1), static_cast<KGenTau*>(nullptr));

				//std::cout << "Tau1 Decay mode " << genTau1->genDecayMode()  << std::endl;
				//std::cout << "Tau2 Decay mode " << genTau2->genDecayMode()  << std::endl;

				//selected the taus decaying into a rho
				if (genTau1->genDecayMode() == 1 && genTau2->genDecayMode() == 1)
				{
					//std::cout << "Number of Pions 1 " << selectedTau1OneProngs.size() << std::endl;
					//std::cout << "Number of Pions 2 " << selectedTau2OneProngs.size() << std::endl;
					//std::cout << "PdgId " << chargedPart1->pdgId << std::endl;
					//std::cout << "PdgId " << chargedPart2->pdgId << std::endl;

					cpq.CalculatePhiStarCP_rho(chargedPart1->p4, chargedPart2->p4,chargedPart1->p4, chargedPart2->p4);
				}
			}




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

	// add possible quantities for the lambda ntuples consumers

	// MC-truth SV vertex, obtained by tau daughter 1
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV1x", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV1 != nullptr) ? (product.m_genSV1)->x() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV1y", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV1 != nullptr) ? (product.m_genSV1)->y() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV1z", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV1 != nullptr) ? (product.m_genSV1)->z() : DefaultValues::UndefinedFloat);
	});

	// MC-truth SV vertex, obtained by tau daughter 2
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV2x", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV2 != nullptr) ? (product.m_genSV2)->x() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV2y", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV2 != nullptr) ? (product.m_genSV2)->y() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genSV2z", [](event_type const& event, product_type const& product)
	{
		return ((product.m_genSV2 != nullptr) ? (product.m_genSV2)->z() : DefaultValues::UndefinedFloat);
	});

	// MC-truth IP vectors
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP1x", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP1 != nullptr) ? (product.m_genIP1).x() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP1y", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP1 != nullptr) ? (product.m_genIP1).y() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP1z", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP1 != nullptr) ? (product.m_genIP1).z() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP2x", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP2 != nullptr) ? (product.m_genIP2).x() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP2y", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP2 != nullptr) ? (product.m_genIP2).y() : DefaultValues::UndefinedFloat);
	});
	LambdaNtupleConsumer<HttTypes>::AddFloatQuantity("genIP2z", [](event_type const& event, product_type const& product)
	{
		return ((&product.m_genIP2 != nullptr) ? (product.m_genIP2).z() : DefaultValues::UndefinedFloat);
	});


}

void GenMatchedTauCPProducer::Produce(event_type const& event, product_type& product,
                                      setting_type const& settings) const
{

	if(product.m_genBosonLVFound && product.m_genBosonTree.m_daughters.size() > 1){

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
	
		// initialization of TVector3 objects
		product.m_genIP1.SetXYZ(-999,-999,-999);
		product.m_genIP2.SetXYZ(-999,-999,-999);
	
	
		if (product.m_chargeOrderedGenLeptons.at(0) and product.m_chargeOrderedGenLeptons.at(1)){
			
			//KGenParticle* genParticle1 = product.m_chargeOrderedGenLeptons.at(0);
			//KGenParticle* genParticle2 = product.m_chargeOrderedGenLeptons.at(1);
			KGenParticle* genParticle1 = product.m_flavourOrderedGenLeptons.at(0);
			KGenParticle* genParticle2 = product.m_flavourOrderedGenLeptons.at(1);
			TVector3 genIP1(-999,-999,-999);
			TVector3 genIP2(-999,-999,-999);
	
			// Defining CPQuantities object to use variables and functions of this class
			CPQuantities cpq;
	
			// if the GenLepton is a hadronic tau, we want to take its hadronic daughter
			// for the calculation of the IP vector
			if (std::abs(genParticle1->pdgId) == DefaultValues::pdgIdTau){
	
				selectedTau1->CreateFinalStateProngs(selectedTau1);
				std::vector<GenParticleDecayTree*> prongs = selectedTau1->m_finalStates;
	
				selectedTau1->DetermineDecayMode(selectedTau1);
				int decaymode = (int)selectedTau1->m_decayMode;
	
				if (decaymode == 4 or decaymode == 7){
					for (unsigned int i=0; i<prongs.size(); ++i){
						if (std::abs(prongs.at(i)->GetCharge()) == 1){
							genParticle1 = prongs.at(i)->m_genParticle;
							break;
						}
					} // loop over the prongs
				} // if decaymode = 1-prong
	
				// if (decaymode == 10) {}    // need a definition in case of 3-prongs
	
			} // if genParticle1 == tau
	
	
			if (std::abs(genParticle2->pdgId) == DefaultValues::pdgIdTau){
	
				selectedTau2->CreateFinalStateProngs(selectedTau2);
				std::vector<GenParticleDecayTree*> prongs = selectedTau2->m_finalStates;
	
				selectedTau2->DetermineDecayMode(selectedTau2);
				int decaymode = (int)selectedTau2->m_decayMode;
	
				if (decaymode == 4 or decaymode == 7){
					for (unsigned int i=0; i<prongs.size(); ++i){
						if (std::abs(prongs.at(i)->GetCharge()) == 1){
							genParticle2 = prongs.at(i)->m_genParticle;
							break;
						}
					} // loop over the prongs
				} // if decaymode = 1-prong
	
				// if (decaymode == 10) {}    // need a definition in case of 3-prongs
	
			} // if genParticle2 == tau
	
			product.m_genSV1 = &genParticle1->vertex;
			product.m_genSV2 = &genParticle2->vertex;
	
			if (product.m_genPV != nullptr){
				genIP1 = cpq.CalculateIPVector(genParticle1, product.m_genPV);
				genIP2 = cpq.CalculateIPVector(genParticle2, product.m_genPV);
				
				product.m_genIP1 = genIP1;
				product.m_genIP2 = genIP2;
				
			}
			// need to add the calculation of phi*CP
	
	
		} // if chargeOrderedGenLeptons is a non-empty vector


	} // if product.m_genBosonLVFound && product.m_genBosonTree.m_daughters.size() > 1

}
