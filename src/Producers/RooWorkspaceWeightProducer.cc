
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/RooWorkspaceWeightProducer.h"
#include "Artus/Utility/interface/Utility.h"
#include "Artus/Utility/interface/SafeMap.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"
#include "Artus/KappaAnalysis/interface/Utility/GeneratorInfo.h"

RooWorkspaceWeightProducer::RooWorkspaceWeightProducer(
		std::string (setting_type::*GetRooWorkspace)(void) const,
		std::vector<std::string>& (setting_type::*GetRooWorkspaceWeightNames)(void) const,
		std::vector<std::string>& (setting_type::*GetRooWorkspaceObjectNames)(void) const,
		std::vector<std::string>& (setting_type::*GetRooWorkspaceObjectArguments)(void) const
):
	GetRooWorkspace(GetRooWorkspace),
	GetRooWorkspaceWeightNames(GetRooWorkspaceWeightNames),
	GetRooWorkspaceObjectNames(GetRooWorkspaceObjectNames),
	GetRooWorkspaceObjectArguments(GetRooWorkspaceObjectArguments)
{
}

RooWorkspaceWeightProducer::RooWorkspaceWeightProducer():
		RooWorkspaceWeightProducer(&setting_type::GetRooWorkspace,
								   &setting_type::GetRooWorkspaceWeightNames,
								   &setting_type::GetRooWorkspaceObjectNames,
								   &setting_type::GetRooWorkspaceObjectArguments)
{
}

void RooWorkspaceWeightProducer::Init(setting_type const& settings)
{
	ProducerBase<HttTypes>::Init(settings);
	TDirectory *savedir(gDirectory);
	TFile *savefile(gFile);
	TFile f(settings.GetRooWorkspace().c_str());
	gSystem->AddIncludePath("-I$ROOFITSYS/include");
	m_workspace = (RooWorkspace*)f.Get("w");
	f.Close();
	gDirectory = savedir;
	gFile = savefile;
	m_weightNames = Utility::ParseMapTypes<int,std::string>(Utility::ParseVectorToMap((settings.*GetRooWorkspaceWeightNames)()));

	std::map<int,std::vector<std::string>> objectNames = Utility::ParseMapTypes<int,std::string>(Utility::ParseVectorToMap((settings.*GetRooWorkspaceObjectNames)()));
    m_functorArgs = Utility::ParseMapTypes<int,std::string>(Utility::ParseVectorToMap((settings.*GetRooWorkspaceObjectArguments)()));
    for(auto objectName:objectNames)
    {
        for(size_t index = 0; index < objectName.second.size(); index++)
        {
    		std::vector<std::string> objects;
    		boost::split(objects, objectName.second[index], boost::is_any_of(","));
        	for(auto object:objects)
        	{
        		m_functors[objectName.first].push_back(m_workspace->function(object.c_str())->functor(m_workspace->argSet(m_functorArgs[objectName.first][index].c_str())));
        	}
        }
    }
}

void RooWorkspaceWeightProducer::Produce( event_type const& event, product_type & product, 
	                     setting_type const& settings) const
{

    for(auto weightNames:m_weightNames)
    {
        KLepton* lepton = product.m_flavourOrderedLeptons[weightNames.first];
        for(size_t index = 0; index < weightNames.second.size(); index++)
        {
            auto args = std::vector<double>{};
            std::vector<std::string> arguments;
            boost::split(arguments,  m_functorArgs.at(weightNames.first).at(index) , boost::is_any_of(","));
            for(auto arg:arguments)
            {
                if(arg=="m_pt" || arg=="e_pt")
                {
                    args.push_back(lepton->p4.Pt());
                }
                if(arg=="m_eta")
                {
                    args.push_back(lepton->p4.Eta());
                }
                if(arg=="e_eta")
                {
                    KElectron* electron = static_cast<KElectron*>(lepton);
                    args.push_back(electron->superclusterPosition.Eta());
                }
                if(arg=="m_iso" || arg=="e_iso")
                {
                    args.push_back(SafeMap::GetWithDefault(product.m_leptonIsolationOverPt, lepton, std::numeric_limits<double>::max()));
                }
            }
            product.m_weights[weightNames.second.at(index)+"_"+std::to_string(weightNames.first+1)] = m_functors.at(weightNames.first).at(index)->eval(args.data());
        }
    }
    if((product.m_weights.find("idweight_1") != product.m_weights.end()) && (product.m_weights.find("isoweight_1") != product.m_weights.end()))
    {
        product.m_weights["identificationWeight_1"] = product.m_weights["idweight_1"]*product.m_weights["isoweight_1"];
        product.m_weights["idweight_1"] = 1.0;
        product.m_weights["isoweight_1"] = 1.0;
    }
    if((product.m_weights.find("idweight_2") != product.m_weights.end()) && (product.m_weights.find("isoweight_2") != product.m_weights.end()))
    {
        product.m_weights["identificationWeight_2"] = product.m_weights["idweight_2"]*product.m_weights["isoweight_2"];
        product.m_weights["idweight_2"] = 1.0;
        product.m_weights["isoweight_2"] = 1.0;
    }
    if(product.m_weights.find("idIsoWeight_1") != product.m_weights.end())
    {
    	product.m_weights["identificationWeight_1"] = product.m_weights["idIsoWeight_1"];
    	product.m_weights["idIsoWeight_1"] = 1.0;
    }
    if(product.m_weights.find("idIsoWeight_2") != product.m_weights.end())
    {
    	product.m_weights["identificationWeight_2"] = product.m_weights["idIsoWeight_2"];
    	product.m_weights["idIsoWeight_2"] = 1.0;
    }
}

// ==========================================================================================

MuMuTriggerWeightProducer::MuMuTriggerWeightProducer() :
		RooWorkspaceWeightProducer(&setting_type::GetMuMuTriggerWeightWorkspace,
								   &setting_type::GetMuMuTriggerWeightWorkspaceWeightNames,
								   &setting_type::GetMuMuTriggerWeightWorkspaceObjectNames,
								   &setting_type::GetMuMuTriggerWeightWorkspaceObjectArguments)
{
}

void MuMuTriggerWeightProducer::Produce( event_type const& event, product_type & product,
	                     setting_type const& settings) const
{
	double muTrigWeight = 1.0;

	for(auto weightNames:m_weightNames)
	{
		KLepton* lepton = product.m_flavourOrderedLeptons[weightNames.first];
		for(size_t index = 0; index < weightNames.second.size(); index++)
		{
			if(weightNames.second.at(index) != "triggerWeight")
				continue;
			auto args = std::vector<double>{};
			std::vector<std::string> arguments;
			boost::split(arguments,  m_functorArgs.at(weightNames.first).at(index) , boost::is_any_of(","));
			for(auto arg:arguments)
			{
				if(arg=="m_pt")
				{
					args.push_back(lepton->p4.Pt());
				}
				if(arg=="m_eta")
				{
					args.push_back(lepton->p4.Eta());
				}
			}
			muTrigWeight *= (1.0 - m_functors.at(weightNames.first).at(index)->eval(args.data()));
		}
	}

	product.m_weights["triggerWeight_1"] = 1-muTrigWeight;
}

// ==========================================================================================

TauTauTriggerWeightProducer::TauTauTriggerWeightProducer() :
		RooWorkspaceWeightProducer(&setting_type::GetTauTauTriggerWeightWorkspace,
								   &setting_type::GetTauTauTriggerWeightWorkspaceWeightNames,
								   &setting_type::GetTauTauTriggerWeightWorkspaceObjectNames,
								   &setting_type::GetTauTauTriggerWeightWorkspaceObjectArguments)
{
}

void TauTauTriggerWeightProducer::Produce( event_type const& event, product_type & product,
						   setting_type const& settings) const
{
	double tauTrigWeight = 1.0;

	for(auto weightNames:m_weightNames)
	{
		KLepton* lepton = product.m_flavourOrderedLeptons[weightNames.first];
		KGenParticle* genParticle = product.m_flavourOrderedGenLeptons[weightNames.first];
		for(size_t index = 0; index < weightNames.second.size(); index++)
		{
			if(weightNames.second.at(index) != "triggerWeight")
				continue;
			if(m_functors.at(weightNames.first).size() != 2)
			{
				LOG(WARNING) << "TauTauTriggerWeightProducer: two object names are required in json config file. Trigger weight will be set to 1.0!";
				break;
			}
			auto args = std::vector<double>{};
			std::vector<std::string> arguments;
			boost::split(arguments,  m_functorArgs.at(weightNames.first).at(index) , boost::is_any_of(","));
			for(auto arg:arguments)
			{
				if(arg=="t_pt")
				{
					args.push_back(lepton->p4.Pt());
				}
			}
			if(genParticle && (GeneratorInfo::GetGenMatchingCode(genParticle) == KappaEnumTypes::GenMatchingCode::IS_TAU_HAD_DECAY))
			{
				tauTrigWeight = m_functors.at(weightNames.first).at(index)->eval(args.data());
			}
			else
			{
				tauTrigWeight = m_functors.at(weightNames.first).at(index+1)->eval(args.data());
			}
			product.m_weights[weightNames.second.at(index)+"_"+std::to_string(weightNames.first+1)] = tauTrigWeight;
		}
	}
}
