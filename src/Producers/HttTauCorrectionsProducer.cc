
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/trim.hpp>

#include "DataFormats/TauReco/interface/PFTau.h"

#include "Artus/Utility/interface/SafeMap.h"
#include "Artus/Utility/interface/Utility.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/HttTauCorrectionsProducer.h"

#include "Artus/KappaAnalysis/interface/Utility/GeneratorInfo.h"

	
void HttTauCorrectionsProducer::Init(setting_type const& settings)
{
	TauCorrectionsProducer::Init(settings);
	
	tauEnergyCorrection = ToTauEnergyCorrection(boost::algorithm::to_lower_copy(boost::algorithm::trim_copy(static_cast<HttSettings const&>(settings).GetTauEnergyCorrection())));
}

void HttTauCorrectionsProducer::AdditionalCorrections(KTau* tau, event_type const& event,
                                                      product_type& product, setting_type const& settings) const
{
	TauCorrectionsProducer::AdditionalCorrections(tau, event, product, settings);
	
	double normalisationFactor = 1.0;
	
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorkingSummer2013#TauES_and_decay_mode_scale_facto
	if (tauEnergyCorrection == TauEnergyCorrection::SUMMER2013)
	{
		// http://cmslxr.fnal.gov/lxr/source/DataFormats/TauReco/interface/PFTau.h#035
		if (tau->decayMode == reco::PFTau::hadronicDecayMode::kOneProng0PiZero)
		{
			normalisationFactor = 0.88;
		}
		else if (tau->decayMode == reco::PFTau::hadronicDecayMode::kOneProng1PiZero || tau->decayMode == reco::PFTau::hadronicDecayMode::kOneProng2PiZero)
		{
			tau->p4 = tau->p4 * (1.012);
// 			tau->p4 = tau->p4 * (1.015 + 0.001 * std::min(std::max(tau->p4.Pt() - 45.0, 0.0), 10.0));
		}
		else if (tau->decayMode == reco::PFTau::hadronicDecayMode::kThreeProng0PiZero)
		{
			tau->p4 = tau->p4 * (1.012);
// 			tau->p4 = tau->p4 * (1.012 + 0.001 * std::min(std::max(tau->p4.Pt() - 32.0, 0.0), 18.0));
		}
	}
	else if (tauEnergyCorrection == TauEnergyCorrection::NEWTAUID)
	{
		tau->p4 = tau->p4 * (1.01);
	}
	else if (tauEnergyCorrection == TauEnergyCorrection::SMHTT2016)
	{
		if (tau->decayMode == 0)
		{
			tau->p4 = tau->p4 * static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionOneProng();
		}
		else if (tau->decayMode == 1 || tau->decayMode == 2)
		{
			tau->p4 = tau->p4 * static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionOneProngPiZeros();
		}
		else if (tau->decayMode == 10)
		{
			tau->p4 = tau->p4 * static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionThreeProng();
		}
	}
	else if (tauEnergyCorrection == TauEnergyCorrection::MSSMHTT2016)
	{
		KGenParticle* genParticle = GeneratorInfo::GetGenMatchedParticle(const_cast<KLepton*>(product.m_originalLeptons[tau]), product.m_genParticleMatchedLeptons, product.m_genTauMatchedLeptons);

		// correct e->tau fake energy scale
		if (genParticle && GeneratorInfo::GetGenMatchingCode(genParticle) == KappaEnumTypes::GenMatchingCode::IS_ELE_PROMPT)
		{
			if (tau->decayMode == 0)
			{
				tau->p4 = tau->p4 * static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionOneProng();
			}
			else if (tau->decayMode == 1 || tau->decayMode == 2)
			{
				tau->p4 = tau->p4 * static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionOneProngPiZeros();
			}
		}
	}
	else if (tauEnergyCorrection != TauEnergyCorrection::NONE)
	{
		LOG(FATAL) << "Tau energy correction of type " << Utility::ToUnderlyingValue(tauEnergyCorrection) << " not yet implemented!";
	}
	
	// tau energy scale shifts
	float tauEnergyCorrectionShift = static_cast<HttSettings const&>(settings).GetTauEnergyCorrectionShift();
	if (tauEnergyCorrectionShift != 1.0)
	{
		tau->p4 = tau->p4 * tauEnergyCorrectionShift;
		
		// settings for (cached) Svfit calculation
		(static_cast<HttProduct&>(product)).m_systematicShift = HttEnumTypes::SystematicShift::TAU_ES;
		(static_cast<HttProduct&>(product)).m_systematicShiftSigma = tauEnergyCorrectionShift;
	}
	
	// electron->tau fake energy scale shifts
	float tauElectronFakeEnergyCorrectionShift = static_cast<HttSettings const&>(settings).GetTauElectronFakeEnergyCorrection();
	if (tauElectronFakeEnergyCorrectionShift != 1.0)
	{
		KGenParticle* genParticle = GeneratorInfo::GetGenMatchedParticle(const_cast<KLepton*>(product.m_originalLeptons[tau]), product.m_genParticleMatchedLeptons, product.m_genTauMatchedLeptons);

		if (genParticle && GeneratorInfo::GetGenMatchingCode(genParticle) == KappaEnumTypes::GenMatchingCode::IS_ELE_PROMPT)
		{
			tau->p4 = tau->p4 * tauElectronFakeEnergyCorrectionShift;

			// settings for (cached) Svfit calculation
			(static_cast<HttProduct&>(product)).m_systematicShift = HttEnumTypes::SystematicShift::TAU_ELECTRON_FAKE_ES;
			(static_cast<HttProduct&>(product)).m_systematicShiftSigma = tauEnergyCorrectionShift;
		}
	}

	// muon->tau fake energy scale shifts
	float tauMuonFakeEnergyCorrectionShift = static_cast<HttSettings const&>(settings).GetTauMuonFakeEnergyCorrection();
	if (tauMuonFakeEnergyCorrectionShift != 1.0)
	{
		KGenParticle* genParticle = GeneratorInfo::GetGenMatchedParticle(const_cast<KLepton*>(product.m_originalLeptons[tau]), product.m_genParticleMatchedLeptons, product.m_genTauMatchedLeptons);

		if (genParticle && GeneratorInfo::GetGenMatchingCode(genParticle) == KappaEnumTypes::GenMatchingCode::IS_MUON_PROMPT)
		{
			tau->p4 = tau->p4 * tauMuonFakeEnergyCorrectionShift;

			// settings for (cached) Svfit calculation
			(static_cast<HttProduct&>(product)).m_systematicShift = HttEnumTypes::SystematicShift::TAU_MUON_FAKE_ES;
			(static_cast<HttProduct&>(product)).m_systematicShiftSigma = tauEnergyCorrectionShift;
		}
	}

	// jet->tau fake energy scale shifts
	float tauJetFakeEnergyCorrectionShift = static_cast<HttSettings const&>(settings).GetTauJetFakeEnergyCorrection();
	if (tauJetFakeEnergyCorrectionShift != 0.0)
	{
		KGenParticle* genParticle = GeneratorInfo::GetGenMatchedParticle(const_cast<KLepton*>(product.m_originalLeptons[tau]), product.m_genParticleMatchedLeptons, product.m_genTauMatchedLeptons);

		if ((genParticle && GeneratorInfo::GetGenMatchingCode(genParticle) == KappaEnumTypes::GenMatchingCode::IS_FAKE) || !genParticle)
		{
			// maximum shift of 40% for pt > 200 GeV
			double shift = tau->p4.Pt() < 200. ? 0.2 * tau->p4.Pt() / 100. : 0.4;

			tau->p4 = tau->p4 * (1 - tauJetFakeEnergyCorrectionShift * shift);

			// settings for (cached) Svfit calculation
			(static_cast<HttProduct&>(product)).m_systematicShift = HttEnumTypes::SystematicShift::TAU_JET_FAKE_ES;
			(static_cast<HttProduct&>(product)).m_systematicShiftSigma = tauJetFakeEnergyCorrectionShift;
		}
	}

	(static_cast<HttProduct&>(product)).m_tauEnergyScaleWeight[tau] = normalisationFactor;
}

