
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/SvfitTools.h"

#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/Utility/interface/CutRange.h"
#include "Artus/Utility/interface/Utility.h"

#include "Kappa/DataFormats/interface/Hash.h"


TauSVfitQuantity::TauSVfitQuantity(size_t tauIndex) :	
	svFitStandalone::SVfitQuantity(),
	m_tauIndex(tauIndex),
	m_tauLabel("Tau"+std::to_string(tauIndex+1))
{
}

TauESVfitQuantity::TauESVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauESVfitQuantity::CreateHistogram(std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return svFitStandalone::makeHistogram(std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"E").c_str(), measuredTauLeptons.at(m_tauIndex).E()/1.025, TMath::Max(1.e+3, 1.e+1*measuredTauLeptons.at(m_tauIndex).E()/1.025), 1.025);
}
double TauESVfitQuantity::FitFunction(std::vector<svFitStandalone::LorentzVector> const& fittedTauLeptons, std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return fittedTauLeptons.at(m_tauIndex).E();
}

TauPtSVfitQuantity::TauPtSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauPtSVfitQuantity::CreateHistogram(std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return svFitStandalone::makeHistogram(std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"Pt").c_str(), 1., 1.e+3, 1.025);
}
double TauPtSVfitQuantity::FitFunction(std::vector<svFitStandalone::LorentzVector> const& fittedTauLeptons, std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return fittedTauLeptons.at(m_tauIndex).pt();
}

TauEtaSVfitQuantity::TauEtaSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauEtaSVfitQuantity::CreateHistogram(std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return new TH1D(std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"Eta").c_str(), std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"Eta").c_str(), 198, -9.9, +9.9);
}
double TauEtaSVfitQuantity::FitFunction(std::vector<svFitStandalone::LorentzVector> const& fittedTauLeptons, std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return fittedTauLeptons.at(m_tauIndex).eta();
}

TauPhiSVfitQuantity::TauPhiSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauPhiSVfitQuantity::CreateHistogram(std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return new TH1D(std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"Phi").c_str(), std::string("SVfitStandaloneAlgorithm_histogram"+m_tauLabel+"Phi").c_str(), 180, -TMath::Pi(), +TMath::Pi());
}
double TauPhiSVfitQuantity::FitFunction(std::vector<svFitStandalone::LorentzVector> const& fittedTauLeptons, std::vector<svFitStandalone::LorentzVector> const& measuredTauLeptons, svFitStandalone::Vector const& measuredMET) const
{
	return fittedTauLeptons.at(m_tauIndex).phi();
}

MCTauTauQuantitiesAdapter::MCTauTauQuantitiesAdapter() : MCPtEtaPhiMassAdapter()
{
	quantities_.push_back(new TauESVfitQuantity(0));
	quantities_.push_back(new TauPtSVfitQuantity(0));
	quantities_.push_back(new TauEtaSVfitQuantity(0));
	quantities_.push_back(new TauPhiSVfitQuantity(0));
	quantities_.push_back(new TauESVfitQuantity(1));
	quantities_.push_back(new TauPtSVfitQuantity(1));
	quantities_.push_back(new TauEtaSVfitQuantity(1));
	quantities_.push_back(new TauPhiSVfitQuantity(1));
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedHiggsLV() const
{
	RMFLV momentum;
	momentum.SetPt(getPt());
	momentum.SetEta(getEta());
	momentum.SetPhi(getPhi());
	momentum.SetM(getMass());
	return momentum;
}

float MCTauTauQuantitiesAdapter::GetFittedTau1E() const
{
	return ExtractValue(5);
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedTau1LV() const
{
	RMFLV momentum;
	momentum.SetPt(ExtractValue(6));
	momentum.SetEta(ExtractValue(7));
	momentum.SetPhi(ExtractValue(8));
	momentum.SetM(DefaultValues::TauMassGeV);
	return momentum;
}

float MCTauTauQuantitiesAdapter::GetFittedTau2E() const
{
	return ExtractValue(9);
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedTau2LV() const
{
	RMFLV momentum;
	momentum.SetPt(ExtractValue(10));
	momentum.SetEta(ExtractValue(11));
	momentum.SetPhi(ExtractValue(12));
	momentum.SetM(DefaultValues::TauMassGeV);
	return momentum;
}


SvfitEventKey::SvfitEventKey(ULong64_t const& runLumiEvent,
                             svFitStandalone::kDecayType const& decayType1, svFitStandalone::kDecayType const& decayType2,
                             HttEnumTypes::SystematicShift const& systematicShift,
                             float const& systematicShiftSigma, IntegrationMethod const& integrationMethod, ULong64_t const& hash)
{
	Set(runLumiEvent, decayType1, decayType2, systematicShift, systematicShiftSigma, integrationMethod, hash);
}

void SvfitEventKey::Set(ULong64_t const& runLumiEvent,
                        svFitStandalone::kDecayType const& decayType1, svFitStandalone::kDecayType const& decayType2,
                        HttEnumTypes::SystematicShift const& systematicShift,
                        float const& systematicShiftSigma, IntegrationMethod const& integrationMethod, ULong64_t const& hash)
{
	this->runLumiEvent = runLumiEvent;
	this->decayType1 = Utility::ToUnderlyingValue(decayType1);
	this->decayType2 = Utility::ToUnderlyingValue(decayType2);
	this->systematicShift = Utility::ToUnderlyingValue<HttEnumTypes::SystematicShift>(systematicShift);
	this->systematicShiftSigma = systematicShiftSigma;
	this->integrationMethod = Utility::ToUnderlyingValue<IntegrationMethod>(integrationMethod);
	this->hash = hash;
}

HttEnumTypes::SystematicShift SvfitEventKey::GetSystematicShift() const
{
	return Utility::ToEnum<HttEnumTypes::SystematicShift>(systematicShift);
}

SvfitEventKey::IntegrationMethod SvfitEventKey::GetIntegrationMethod() const
{
	return Utility::ToEnum<IntegrationMethod>(integrationMethod);
}

void SvfitEventKey::CreateBranches(TTree* tree)
{
	tree->Branch("runLumiEvent", &runLumiEvent, "runLumiEvent/l");
	tree->Branch("decayType1", &decayType1);
	tree->Branch("decayType2", &decayType2);
	tree->Branch("systematicShift", &systematicShift);
	tree->Branch("systematicShiftSigma", &systematicShiftSigma);
	tree->Branch("integrationMethod", &integrationMethod);
	tree->Branch("hash", &hash, "hash/l");
}

void SvfitEventKey::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("runLumiEvent", &runLumiEvent);
	tree->SetBranchAddress("decayType1", &decayType1);
	tree->SetBranchAddress("decayType2", &decayType2);
	tree->SetBranchAddress("systematicShift", &systematicShift);
	tree->SetBranchAddress("systematicShiftSigma", &systematicShiftSigma);
	tree->SetBranchAddress("integrationMethod", &integrationMethod);
	tree->SetBranchAddress("hash", &hash);
	ActivateBranches(tree, true);
}

void SvfitEventKey::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("runLumiEvent", activate);
	tree->SetBranchStatus("decayType1", activate);
	tree->SetBranchStatus("decayType2", activate);
	tree->SetBranchStatus("systematicShift", activate);
	tree->SetBranchStatus("systematicShiftSigma", activate);
	tree->SetBranchStatus("integrationMethod", activate);
	tree->SetBranchStatus("hash", activate);
}

bool SvfitEventKey::operator<(SvfitEventKey const& rhs) const
{
	if (runLumiEvent == rhs.runLumiEvent)
	{
		if (decayType1 == rhs.decayType1)
		{
			if (decayType2 == rhs.decayType2)
			{
				if (integrationMethod == rhs.integrationMethod)
				{
					if (systematicShift == rhs.systematicShift)
					{
						if (hash == rhs.hash)
						{
							return (systematicShiftSigma < rhs.systematicShiftSigma);
						}
						else
						{
							return (hash < rhs.hash);
						}
					}
					else
					{
						return (systematicShift < rhs.systematicShift);
					}
				}
				else
				{
					return (integrationMethod < rhs.integrationMethod);
				}
			}
			else
			{
				return (decayType2 < rhs.decayType2);
			}
		}
		else
		{
			return (decayType1 < rhs.decayType1);
		}
	}
	else {
		return (runLumiEvent < rhs.runLumiEvent);
	}
}

bool SvfitEventKey::operator==(SvfitEventKey const& rhs) const
{
	return ((runLumiEvent == rhs.runLumiEvent) &&
	        (decayType1 == rhs.decayType1) &&
	        (decayType2 == rhs.decayType2) &&
	        (integrationMethod == rhs.integrationMethod) &&
	        (systematicShift == rhs.systematicShift) &&
	        CutRange::EqualsCut(systematicShiftSigma).IsInRange(rhs.systematicShiftSigma) &&
	        (hash == rhs.hash));
}

bool SvfitEventKey::operator!=(SvfitEventKey const& rhs) const
{
	return (! (*this == rhs));
}

std::string std::to_string(SvfitEventKey const& svfitEventKey)
{
	return std::string("SvfitEventKey(") +
			"runLumiEvent=" + std::to_string(svfitEventKey.runLumiEvent) + ", " +
			"decayType1=" + std::to_string(svfitEventKey.decayType1) + ", " +
			"decayType2=" + std::to_string(svfitEventKey.decayType2) + ", " +
			"systematicShift=" + std::to_string(svfitEventKey.systematicShift) + ", " +
			"systematicShiftSigma=" + std::to_string(svfitEventKey.systematicShiftSigma) + ", " +
			"integrationMethod=" + std::to_string(svfitEventKey.integrationMethod) + "," +
			"hash=" + std::to_string(svfitEventKey.hash) + ")";
}

std::ostream& operator<<(std::ostream& os, SvfitEventKey const& svfitEventKey)
{
	return os << std::to_string(svfitEventKey);
}

SvfitInputs::SvfitInputs(RMFLV const& leptonMomentum1, RMFLV const& leptonMomentum2,
                         RMDataV const& metMomentum, RMSM2x2 const& metCovariance,
                         int const& decayMode1, int const& decayMode2)
	: SvfitInputs()
{
	Set(leptonMomentum1, leptonMomentum2, metMomentum, metCovariance, decayMode1, decayMode2);
}

SvfitInputs::~SvfitInputs()
{
	/* TODO: freeing memory here creates segmentation faults
	if (leptonMomentum1)
	{
		delete leptonMomentum1;
	}
	if (leptonMomentum2)
	{
		delete leptonMomentum2;
	}
	if (metMomentum)
	{
		delete metMomentum;
	}
	if (metCovariance)
	{
		delete metCovariance;
	}
	*/
}

void SvfitInputs::Set(RMFLV const& leptonMomentum1, RMFLV const& leptonMomentum2,
                      RMDataV const& metMomentum, RMSM2x2 const& metCovariance,
                      int const& decayMode1, int const& decayMode2)
{
	if (! this->leptonMomentum1)
	{
		this->leptonMomentum1 = new RMFLV();
	}
	if (! this->leptonMomentum2)
	{
		this->leptonMomentum2 = new RMFLV();
	}
	if (! this->metMomentum)
	{
		this->metMomentum = new RMDataV();
	}
	if (! this->metCovariance)
	{
		this->metCovariance = new RMSM2x2();
	}
	if (! this->decayMode1)
	{
		this->decayMode1 = new int;
	}
	if (! this->decayMode2)
	{
		this->decayMode2 = new int;
	}
	
	*(this->leptonMomentum1) = leptonMomentum1;
	*(this->leptonMomentum2) = leptonMomentum2;
	*(this->metMomentum) = metMomentum;
	*(this->metCovariance) = metCovariance;
	*(this->decayMode1) = decayMode1;
	*(this->decayMode2) = decayMode2;
}

void SvfitInputs::CreateBranches(TTree* tree)
{
	tree->Branch("leptonMomentum1", "RMFLV", &leptonMomentum1);
	tree->Branch("leptonMomentum2", "RMFLV", &leptonMomentum2);
	tree->Branch("metMomentum", "ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>", &metMomentum);
	tree->Branch("metCovariance", "ROOT::Math::SMatrix<double, 2, 2, ROOT::Math::MatRepSym<double, 2> >", &metCovariance);
	tree->Branch("decayMode1", decayMode1);
	tree->Branch("decayMode2", decayMode2);
}

void SvfitInputs::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("leptonMomentum1", &leptonMomentum1);
	tree->SetBranchAddress("leptonMomentum2", &leptonMomentum2);
	tree->SetBranchAddress("metMomentum", &metMomentum);
	tree->SetBranchAddress("metCovariance", &metCovariance);
	tree->SetBranchAddress("decayMode1", decayMode1);
	tree->SetBranchAddress("decayMode2", decayMode2);
	ActivateBranches(tree, true);
}

void SvfitInputs::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("leptonMomentum1", activate);
	tree->SetBranchStatus("leptonMomentum2", activate);
	tree->SetBranchStatus("metMomentum", activate);
	tree->SetBranchStatus("metCovariance", activate);
	tree->SetBranchStatus("decayMode1", activate);
	tree->SetBranchStatus("decayMode2", activate);
}

bool SvfitInputs::operator==(SvfitInputs const& rhs) const
{
	return (Utility::ApproxEqual(*leptonMomentum1, *(rhs.leptonMomentum1)) &&
	        Utility::ApproxEqual(*leptonMomentum2, *(rhs.leptonMomentum2)) &&
	        Utility::ApproxEqual(*metMomentum, *(rhs.metMomentum)) &&
	        Utility::ApproxEqual(*metCovariance, *(rhs.metCovariance)) &&
	        (*decayMode1 == *(rhs.decayMode1)) &&
	        (*decayMode2 == *(rhs.decayMode2)));
}

bool SvfitInputs::operator!=(SvfitInputs const& rhs) const
{
	return (! (*this == rhs));
}

SVfitStandaloneAlgorithm SvfitInputs::GetSvfitStandaloneAlgorithm(SvfitEventKey const& svfitEventKey, int verbosity, bool addLogM) const
{
	SVfitStandaloneAlgorithm svfitStandaloneAlgorithm = SVfitStandaloneAlgorithm(GetMeasuredTauLeptons(svfitEventKey),
	                                                                             metMomentum->x(),
	                                                                             metMomentum->y(),
	                                                                             GetMetCovarianceMatrix(),
	                                                                             verbosity);
	svfitStandaloneAlgorithm.addLogM(addLogM);
	svfitStandaloneAlgorithm.setMCQuantitiesAdapter(new MCTauTauQuantitiesAdapter());
	return svfitStandaloneAlgorithm;
}

void SvfitInputs::Integrate(SvfitEventKey const& svfitEventKey, ClassicSVfit& svfitAlgorithm) const
{
	svfitAlgorithm.integrate(
			GetMeasuredTauLeptonsClassic(svfitEventKey),
			metMomentum->x(),
			metMomentum->y(),
			GetMetCovarianceMatrix()
	);
}

std::vector<svFitStandalone::MeasuredTauLepton> SvfitInputs::GetMeasuredTauLeptons(SvfitEventKey const& svfitEventKey) const
{
	double leptonMass1, leptonMass2;
	if(svfitEventKey.decayType1 == 2)
	{
		leptonMass1 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType1 == 3)
	{
		leptonMass1 = 105.658e-3;
	}
	else
	{
		leptonMass1 = leptonMomentum1->M();
	}
	if(svfitEventKey.decayType2 == 2)
	{
		leptonMass2 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType2 == 3)
	{
		leptonMass2 = 105.658e-3;
	}
	else
	{
		leptonMass2 = leptonMomentum2->M();
	}
	std::vector<svFitStandalone::MeasuredTauLepton> measuredTauLeptons {
		svFitStandalone::MeasuredTauLepton(Utility::ToEnum<svFitStandalone::kDecayType>(svfitEventKey.decayType1), leptonMomentum1->pt(), leptonMomentum1->eta(), leptonMomentum1->phi(), leptonMass1, *decayMode1),
		svFitStandalone::MeasuredTauLepton(Utility::ToEnum<svFitStandalone::kDecayType>(svfitEventKey.decayType2), leptonMomentum2->pt(), leptonMomentum2->eta(), leptonMomentum2->phi(), leptonMass2, *decayMode2)
	};
	return measuredTauLeptons;
}

std::vector<classic_svFit::MeasuredTauLepton> SvfitInputs::GetMeasuredTauLeptonsClassic(SvfitEventKey const& svfitEventKey) const
{
	double leptonMass1, leptonMass2;
	if(svfitEventKey.decayType1 == 2)
	{
		leptonMass1 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType1 == 3)
	{
		leptonMass1 = 105.658e-3;
	}
	else
	{
		leptonMass1 = leptonMomentum1->M();
	}
	if(svfitEventKey.decayType2 == 2)
	{
		leptonMass2 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType2 == 3)
	{
		leptonMass2 = 105.658e-3;
	}
	else
	{
		leptonMass2 = leptonMomentum2->M();
	}
	std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons {
		classic_svFit::MeasuredTauLepton(Utility::ToEnum<classic_svFit::MeasuredTauLepton::kDecayType>(svfitEventKey.decayType1), leptonMomentum1->pt(), leptonMomentum1->eta(), leptonMomentum1->phi(), leptonMass1, *decayMode1),
		classic_svFit::MeasuredTauLepton(Utility::ToEnum<classic_svFit::MeasuredTauLepton::kDecayType>(svfitEventKey.decayType2), leptonMomentum2->pt(), leptonMomentum2->eta(), leptonMomentum2->phi(), leptonMass2, *decayMode2)
	};
	return measuredTauLeptons;
}

TMatrixD SvfitInputs::GetMetCovarianceMatrix() const
{
	TMatrixD metCovarianceMatrix(2, 2);
	metCovarianceMatrix[0][0] = metCovariance->At(0, 0);
	metCovarianceMatrix[1][0] = metCovariance->At(1, 0);
	metCovarianceMatrix[0][1] = metCovariance->At(0, 1);
	metCovarianceMatrix[1][1] = metCovariance->At(1, 1);
	return metCovarianceMatrix;
}

SvfitResults::SvfitResults(double fittedTransverseMass, RMFLV const& fittedHiggsLV, float fittedTau1E, RMFLV const& fittedTau1LV, float fittedTau2E, RMFLV const& fittedTau2LV) :
	SvfitResults()
{
	Set(fittedTransverseMass, fittedHiggsLV, fittedTau1E, fittedTau1LV, fittedTau2E, fittedTau2LV);
	recalculated = false;
}

SvfitResults::SvfitResults(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) :
	SvfitResults()
{
	Set(svfitStandaloneAlgorithm);
}

SvfitResults::~SvfitResults()
{
	/* TODO: freeing memory here creates segmentation faults
	if (fittedTransverseMass)
	{
		delete fittedTransverseMass;
	}
	if (fittedHiggsLV)
	{
		delete fittedHiggsLV;
	}
	if (fittedTau1E)
	{
		delete fittedTau1E;
	}
	if (fittedTau1LV)
	{
		delete fittedTau1LV;
	}
	if (fittedTau2E)
	{
		delete fittedTau2E;
	}
	if (fittedTau2LV)
	{
		delete fittedTau2LV;
	}
	*/
}

void SvfitResults::Set(double fittedTransverseMass, RMFLV const& fittedHiggsLV, float fittedTau1E, RMFLV const& fittedTau1LV, float fittedTau2E, RMFLV const& fittedTau2LV)
{
	if (! this->fittedHiggsLV)
	{
		this->fittedHiggsLV = new RMFLV();
	}
	if (! this->fittedTau1LV)
	{
		this->fittedTau1LV = new RMFLV();
	}
	if (! this->fittedTau2LV)
	{
		this->fittedTau2LV = new RMFLV();
	}
	
	this->fittedTransverseMass = fittedTransverseMass;
	*(this->fittedHiggsLV) = fittedHiggsLV;
	this->fittedTau1E = fittedTau1E;
	*(this->fittedTau1LV) = fittedTau1LV;
	this->fittedTau2E = fittedTau2E;
	*(this->fittedTau2LV) = fittedTau2LV;
}

void SvfitResults::Set(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm)
{
	Set(GetFittedTransverseMass(svfitStandaloneAlgorithm),
	    GetFittedHiggsLV(svfitStandaloneAlgorithm),
	    GetFittedTau1E(svfitStandaloneAlgorithm),
	    GetFittedTau1LV(svfitStandaloneAlgorithm),
	    GetFittedTau2E(svfitStandaloneAlgorithm),
	    GetFittedTau2LV(svfitStandaloneAlgorithm));
}

void SvfitResults::CreateBranches(TTree* tree)
{
	tree->Branch("svfitTransverseMass", &fittedTransverseMass, "svfitTransverseMass/D");
	tree->Branch("svfitHiggsLV", &fittedHiggsLV);
	tree->Branch("svfitTau1E", &fittedTau1E, "svfitTau1E/F");
	tree->Branch("svfitTau1LV", &fittedTau1LV);
	tree->Branch("svfitTau2E", &fittedTau2E, "svfitTau2E/F");
	tree->Branch("svfitTau2LV", &fittedTau2LV);
}

void SvfitResults::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("svfitTransverseMass", &fittedTransverseMass);
	tree->SetBranchAddress("svfitHiggsLV", &fittedHiggsLV);
	tree->SetBranchAddress("svfitTau1E", &fittedTau1E);
	tree->SetBranchAddress("svfitTau1LV", &fittedTau1LV);
	tree->SetBranchAddress("svfitTau2E", &fittedTau2E);
	tree->SetBranchAddress("svfitTau2LV", &fittedTau2LV);
	ActivateBranches(tree, true);
}

void SvfitResults::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("svfitTransverseMass", activate);
	tree->SetBranchStatus("svfitHiggsLV", activate);
	tree->SetBranchStatus("svfitTau1E", activate);
	tree->SetBranchStatus("svfitTau1LV", activate);
	tree->SetBranchStatus("svfitTau2E", activate);
	tree->SetBranchStatus("svfitTau2LV", activate);
}

bool SvfitResults::operator==(SvfitResults const& rhs) const
{
	return (Utility::ApproxEqual(fittedTransverseMass, rhs.fittedTransverseMass) &&
	        Utility::ApproxEqual(*fittedHiggsLV, *(rhs.fittedHiggsLV)) &&
	        Utility::ApproxEqual(fittedTau1E, rhs.fittedTau1E) &&
	        Utility::ApproxEqual(*fittedTau1LV, *(rhs.fittedTau1LV)) &&
	        Utility::ApproxEqual(fittedTau2E, rhs.fittedTau2E) &&
	        Utility::ApproxEqual(*fittedTau2LV, *(rhs.fittedTau2LV)));
}

bool SvfitResults::operator!=(SvfitResults const& rhs) const
{
	return (! (*this == rhs));
}

double SvfitResults::GetFittedTransverseMass(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->getTransverseMass();
}
RMFLV SvfitResults::GetFittedHiggsLV(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->GetFittedHiggsLV();
}
float SvfitResults::GetFittedTau1E(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->GetFittedTau1E();
}
RMFLV SvfitResults::GetFittedTau1LV(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->GetFittedTau1LV();
}
float SvfitResults::GetFittedTau2E(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->GetFittedTau2E();
}
RMFLV SvfitResults::GetFittedTau2LV(SVfitStandaloneAlgorithm const& svfitStandaloneAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitStandaloneAlgorithm.getMCQuantitiesAdapter())->GetFittedTau2LV();
}


std::map<std::string, TTree*> SvfitTools::svfitCacheInputTree;
std::map<std::string, TFile*> SvfitTools::svfitCacheInputFile;
std::map<std::string, std::map<SvfitEventKey, uint64_t>> SvfitTools::svfitCacheInputTreeIndices;
std::map<std::string, SvfitResults> SvfitTools::svfitResults;

SvfitTools::SvfitTools() :
	svfitAlgorithm(1)
{
}

void SvfitTools::Init(std::vector<std::string> const& fileNames, std::string const& treeName)
{
	cacheFileName = fileNames[0];
	if ( SvfitTools::svfitCacheInputTreeIndices.find(cacheFileName) == SvfitTools::svfitCacheInputTreeIndices.end())
	{
		TDirectory *savedir(gDirectory);
		TFile *savefile(gFile);

		SvfitTools::svfitCacheInputFile[cacheFileName] = TFile::Open(cacheFileName.c_str(), "CACHEREAD", cacheFileName.c_str());
		if (SvfitTools::svfitCacheInputFile[cacheFileName] == nullptr)
		{
			LOG(WARNING) << "Could not load SVfit cache trees from file " << cacheFileName << "/" << treeName << "!" << std::endl;
		}
		else
		{
			SvfitTools::svfitCacheInputTree[cacheFileName] = dynamic_cast<TTree*>(SvfitTools::svfitCacheInputFile.at(cacheFileName)->Get(treeName.c_str()));

			LOG(INFO) << "\tLoaded SVfit cache trees from file...";
			LOG(INFO) << "\t\t" << cacheFileName << "/" << treeName << " with " << SvfitTools::svfitCacheInputTree.at(cacheFileName)->GetEntries() << " Entries" << std::endl;

			svfitEventKey.SetBranchAddresses(SvfitTools::svfitCacheInputTree[cacheFileName]);
			SvfitTools::svfitCacheInputTreeIndices[cacheFileName] = std::map<SvfitEventKey, uint64_t>();
			for (uint64_t svfitCacheInputTreeIndex = 0;
				 svfitCacheInputTreeIndex < uint64_t(SvfitTools::svfitCacheInputTree.at(cacheFileName)->GetEntries());
				 ++svfitCacheInputTreeIndex)
			{
				SvfitTools::svfitCacheInputTree.at(cacheFileName)->GetEntry(svfitCacheInputTreeIndex);

				SvfitTools::svfitCacheInputTreeIndices.at(cacheFileName)[svfitEventKey] = svfitCacheInputTreeIndex;
				LOG_N_TIMES(10,DEBUG) << std::to_string(svfitEventKey) << " --> " << svfitCacheInputTreeIndex;
				LOG_N_TIMES(10, DEBUG) << svfitEventKey << " --> " << svfitCacheInputTreeIndex;
			}
			svfitEventKey.ActivateBranches(SvfitTools::svfitCacheInputTree.at(cacheFileName), false);
			LOG(DEBUG) << "\t\t" << SvfitTools::svfitCacheInputTreeIndices.at(cacheFileName).size() << " entries found.";
		
			svfitResults[cacheFileName] = SvfitResults();
			svfitResults.at(cacheFileName).SetBranchAddresses(SvfitTools::svfitCacheInputTree.at(cacheFileName));
		}

		gDirectory = savedir;
		gFile = savefile;
	}
	else 
	{
		LOG(DEBUG) << "\tSVfit cache trees from file " << cacheFileName << " already loaded" << std::endl;
	}
}

SvfitResults SvfitTools::GetResults(SvfitEventKey const& svfitEventKey,
                                    SvfitInputs const& svfitInputs,
                                    bool& neededRecalculation,
                                    HttEnumTypes::SvfitCacheMissBehaviour svfitCacheMissBehaviour)
{
	neededRecalculation = true;
	if ((cacheFileName != NULL) && (SvfitTools::svfitCacheInputTree.count(cacheFileName) > 0) &&( SvfitTools::svfitCacheInputTreeIndices.find(cacheFileName) != SvfitTools::svfitCacheInputTreeIndices.end() ))
	{
		auto svfitCacheInputTreeIndicesItem = SvfitTools::svfitCacheInputTreeIndices.at(cacheFileName).find(svfitEventKey);
		if (svfitCacheInputTreeIndicesItem != SvfitTools::svfitCacheInputTreeIndices.at(cacheFileName).end())
		{
			SvfitTools::svfitCacheInputTree.at(cacheFileName)->GetEntry(svfitCacheInputTreeIndicesItem->second);
			svfitResults.at(cacheFileName).fromCache();
			neededRecalculation = false;
		}
	}
	if (neededRecalculation)
	{
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::recalculate)
		{
			LOG_N_TIMES(30, INFO) << "SvfitCache miss: No corresponding entry to the current inputs found in SvfitCache file. Re-Running SvFit. Did your inputs change?" 
			<< std::endl << "Cache searched in file: " << cacheFileName << std::endl;
		}
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::assert)
		{
			LOG(FATAL) << "SvfitCache miss: No corresponding entry to the current inputs found in SvfitCache file. Did your inputs change?" << std::endl;
		}
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::undefined)
		{
			svfitResults[cacheFileName] = SvfitResults();
			svfitResults.at(cacheFileName).fromRecalculation();
			return svfitResults.at(cacheFileName);
		}
		
		// construct algorithm
		if (! m_inputFile_visPtResolution)
		{
			TDirectory *savedir(gDirectory);
			TFile *savefile(gFile);
			TString cmsswBase = TString( getenv ("CMSSW_BASE") );
			m_inputFile_visPtResolution = new TFile(cmsswBase+"/src/TauAnalysis/SVfitStandalone/data/svFitVisMassAndPtResolutionPDF.root");
			gDirectory = savedir;
			gFile = savefile;
		}
		SVfitStandaloneAlgorithm svfitStandaloneAlgorithm = svfitInputs.GetSvfitStandaloneAlgorithm(svfitEventKey);
		svfitStandaloneAlgorithm.shiftVisPt(true, m_inputFile_visPtResolution);
	
		// execute integration
		if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::VEGAS)
		{
			svfitStandaloneAlgorithm.integrateVEGAS();
		}
		else if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::MARKOV_CHAIN)
		{
			svfitStandaloneAlgorithm.integrateMarkovChain();
			svfitInputs.Integrate(svfitEventKey, svfitAlgorithm);
		}
		else if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::FIT)
		{
			svfitStandaloneAlgorithm.fit();
		}
		else
		{
			LOG(FATAL) << "SVfit integration of type " << svfitEventKey.integrationMethod << " not yet implemented!";
		}
	
		// retrieve results
		svfitResults[cacheFileName].Set(svfitStandaloneAlgorithm);
		svfitResults.at(cacheFileName).fromRecalculation();
	}
	
	LOG(WARNING) << svfitAlgorithm.mass() << " (classic) vs. " << svfitResults.at(cacheFileName).fittedHiggsLV->mass() << " (standalone)";
	return svfitResults.at(cacheFileName);
}

SvfitTools::~SvfitTools()
{
	// do NOT call destructor for TTree and TFile here. They are static and the destructor is called several times when running the factory
	// We have to trust the OS does handle freeing the memory properly
}
