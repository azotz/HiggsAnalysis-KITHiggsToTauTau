
#include "Artus/Utility/interface/SafeMap.h"
#include "Artus/Utility/interface/Utility.h"

#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/DiTauPair.h"


DiTauPair::DiTauPair(KLepton* lepton1, KLepton* lepton2) :
	std::pair<KLepton*, KLepton*>(lepton1, lepton2)
{
}


// TODO: this function should probably get cached
std::vector<std::string> DiTauPair::GetCommonHltPaths(std::map<KLepton*, std::map<std::string, std::map<std::string, KLV*> >* >* detailedTriggerMatchedLeptons)
{
	std::map<std::string, std::map<std::string, KLV*> >* detailedTriggerMatchedLepton1 = SafeMap::GetWithDefault(
			*detailedTriggerMatchedLeptons,
			&(*first),
			new std::map<std::string, std::map<std::string, KLV*> >()
	);
	
	std::vector<std::string> hltPaths1;
	for (std::map<std::string, std::map<std::string, KLV*> >::iterator it = detailedTriggerMatchedLepton1->begin();
	     it != detailedTriggerMatchedLepton1->end(); ++it)
	{
		hltPaths1.push_back(it->first);
	}
	
	std::map<std::string, std::map<std::string, KLV*> >* detailedTriggerMatchedLepton2 = SafeMap::GetWithDefault(
			*detailedTriggerMatchedLeptons,
			&(*second),
			new std::map<std::string, std::map<std::string, KLV*> >()
	);
	
	std::vector<std::string> hltPaths2;
	for (std::map<std::string, std::map<std::string, KLV*> >::iterator it = detailedTriggerMatchedLepton2->begin();
	     it != detailedTriggerMatchedLepton2->end(); ++it)
	{
		hltPaths2.push_back(it->first);
	}
	
	std::vector<std::string> commonHltPaths;
	std::set_intersection(hltPaths1.begin(), hltPaths1.end(), hltPaths2.begin(), hltPaths2.end(), commonHltPaths.begin());
	return commonHltPaths;
}

DiTauPairIsoPtComparator::DiTauPairIsoPtComparator(const std::map<KLepton*, double>* leptonIsolationOverPt):
	m_leptonIsolationOverPt(leptonIsolationOverPt)
{
}

bool DiTauPairIsoPtComparator::operator() (DiTauPair const& diTauPair1, DiTauPair const& diTauPair2) const
{
	// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2015#Pair_Selection_Algorithm
	
	double isoPair1Lepton1 = SafeMap::Get(*m_leptonIsolationOverPt, diTauPair1.first);
	double isoPair2Lepton1 = SafeMap::Get(*m_leptonIsolationOverPt, diTauPair2.first);
	
	if (! Utility::ApproxEqual(isoPair1Lepton1, isoPair2Lepton1))
	{
		return (isoPair1Lepton1 < isoPair2Lepton1);
	}
	else
	{
		if (! Utility::ApproxEqual(diTauPair1.first->p4.Pt(), diTauPair2.first->p4.Pt()))
		{
			return (diTauPair1.first->p4.Pt() > diTauPair2.first->p4.Pt());
		}
		else
		{
			double isoPair1Lepton2 = SafeMap::Get(*m_leptonIsolationOverPt, diTauPair1.second);
			double isoPair2Lepton2 = SafeMap::Get(*m_leptonIsolationOverPt, diTauPair2.second);
			
			if (! Utility::ApproxEqual(isoPair1Lepton2, isoPair2Lepton2))
			{
				return (isoPair1Lepton2 < isoPair2Lepton2);
			}
			else
			{
				return (diTauPair1.second->p4.Pt() > diTauPair2.second->p4.Pt());
			}
		}
	}
}

