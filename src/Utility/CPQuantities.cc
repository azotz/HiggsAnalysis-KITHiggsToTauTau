
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/CPQuantities.h"

// this version uses tau 4-momenta to calculate decay planes (useful for GenTauCPProducer)
double CPQuantities::CalculatePhiStarCP(RMFLV tau1, RMFLV tau2, RMFLV chargPart1, RMFLV chargPart2)
{
	//Momentum vectors of the Taus
	RMFLV::BetaVector k1, k2;
	k1.SetXYZ(tau1.Px(), tau1.Py() , tau1.Pz());
	k2.SetXYZ(tau2.Px(), tau2.Py() , tau2.Pz());
	return this->CalculatePhiStarCPSame(k1, k2, chargPart1, chargPart2, "gen");
}


// this version uses track and vertex information to calculate the decay planes (useful for RecoTauCPProducer)
double CPQuantities::CalculatePhiStarCP(KVertex pv, KTrack track1, KTrack track2,  RMFLV chargPart1, RMFLV chargPart2)
{
	//Primary vertex
	RMFLV::BetaVector pvpos;
	pvpos.SetXYZ((pv.position).X(), (pv.position).Y(), (pv.position).Z());

	//Points on tau tracks
	RMFLV::BetaVector track1pos, track2pos;
	track1pos.SetXYZ((track1.ref).X(), (track1.ref).Y(), (track1.ref).Z());
	track2pos.SetXYZ((track2.ref).X(), (track2.ref).Y(), (track2.ref).Z());

	//Flight direction of taus determined from pv and trackpos
	RMFLV::BetaVector k1, k2;
	k1 = track1pos - pvpos;
	k2 = track2pos - pvpos;
	return this->CalculatePhiStarCPSame(k1, k2, chargPart1, chargPart2, "reco");

}


// calculation of variables Phi* and Phi*CP
double CPQuantities::CalculatePhiStarCPSame(RMFLV::BetaVector k1, RMFLV::BetaVector k2, RMFLV chargPart1, RMFLV chargPart2, std::string level)
{
	//Step 1: Creating a Boost M into the ZMF of the (chargPart1+, chargedPart2-) decay
	RMFLV ProngImp = chargPart1 + chargPart2;
	RMFLV::BetaVector boostvec = ProngImp.BoostToCM();
	ROOT::Math::Boost M(boostvec);

	//Step 2: Calculating impact parameter vectors n1 n2

	//Momentum vectors of the charged particles
	RMFLV::BetaVector p1, p2;
	p1.SetXYZ(chargPart1.Px(), chargPart1.Py() , chargPart1.Pz());
	p2.SetXYZ(chargPart2.Px(), chargPart2.Py() , chargPart2.Pz());
	
	//Not normalized n1, n2
	RMFLV::BetaVector n1 = k1 - ((k1.Dot(p1)) / (p1.Dot(p1))) * p1;
	RMFLV::BetaVector n2 = k2 - ((k2.Dot(p2)) / (p2.Dot(p2))) * p2;
	
	if(level=="reco")
	{
		this->SetRecoIP1(n1.R());
		this->SetRecoIP2(n2.R());
	}
	//Normalized n1, n2
	n1 = n1.Unit();
	n2 = n2.Unit();

	//Step 3: Boosting 4-vectors (n1,0), (n2,0), p1, p2 with M
	RMFLV n1_mu, n2_mu;
	n1_mu.SetPxPyPzE(n1.X(), n1.Y(), n1.Z(), 0);
	n2_mu.SetPxPyPzE(n2.X(), n2.Y(), n2.Z(), 0);

	n1_mu = M * n1_mu;
	n2_mu = M * n2_mu;
	chargPart1 = M * chargPart1;
	chargPart2 = M * chargPart2;

	//Step 4: Calculation of the transverse component of n1, n2 to p1, p2 (after Boosting)
	n1.SetXYZ(n1_mu.Px(), n1_mu.Py(), n1_mu.Pz());
	n2.SetXYZ(n2_mu.Px(), n2_mu.Py(), n2_mu.Pz());
	p1.SetXYZ(chargPart1.Px(), chargPart1.Py(), chargPart1.Pz());
	p2.SetXYZ(chargPart2.Px(), chargPart2.Py(), chargPart2.Pz());

	RMFLV::BetaVector n1t = n1 - ((n1.Dot(p1)) / (p1.Dot(p1))) * p1;
	n1t = n1t.Unit();
	RMFLV::BetaVector n2t = n2 - ((n2.Dot(p2)) / (p2.Dot(p2))) * p2;
	n2t = n2t.Unit();
	RMFLV::BetaVector p1n = p1.Unit();

	if(level=="reco")
	{
		this->SetRecoPhiStar(acos(n2t.Dot(n1t)));
	}
	else if (level=="gen")
	{
		this->SetGenPhiStar(acos(n2t.Dot(n1t)));
	}
	//Step 5: Calculating Phi*CP
	double phiStarCP = 0;
	if(p1n.Dot(n2t.Cross(n1t))>=0)
	{
		phiStarCP = acos(n2t.Dot(n1t));
	}
	else
	{
		phiStarCP = 2*ROOT::Math::Pi()-acos(n2t.Dot(n1t));
	}
	return phiStarCP;
}


// calculation of the hadron Energies in the approximate diTau restframe
double CPQuantities::CalculateChargedHadronEnergy(RMFLV diTauMomentum, RMFLV chargHad)
{
	// Step 1: Creating Boost into diTau rest frame
	RMFLV::BetaVector boostditau = diTauMomentum.BoostToCM();
	ROOT::Math::Boost Mditau(boostditau);
	// Step 2: Boosting hadron and extracting energy
	chargHad = Mditau * chargHad;
	return chargHad.E();
}


// estimation of the impact parameter error (used on recostruction level)
double CPQuantities::CalculateTrackReferenceError(KTrack track)
{
	return sqrt(track.errDz*track.errDz+track.errDxy*track.errDxy);
}


// calculation of the angle Phi between the tau decay planes
// - using tau- direction in the tautau RF as reference
// - calculating the normal vectors to the planes
// - everything is defined in the Higgs boson rest frame
double CPQuantities::CalculatePhiCP(RMFLV boson, RMFLV tau1, RMFLV tau2, RMFLV chargPart1, RMFLV chargPart2)
{
	// Step 1: Boosts into the boson rest frames to boost charged particles 4-momentums
	RMFLV::BetaVector boostvech = boson.BoostToCM();
	ROOT::Math::Boost Mh(boostvech);

	// Step 2: Boosting the 4-momentum vectors to boson rest frame
	tau1 = Mh * tau1;
	tau2 = Mh * tau2;

	//std::cout << tau1 << "               " << -1*tau2 << std::endl;

	chargPart1 = Mh * chargPart1;
	chargPart2 = Mh * chargPart2;

	// Step 3: Creating 3-momentum normal vectors on decay planes
	RMFLV::BetaVector km, pm, pp, nm, np, ez;
	km.SetXYZ(tau1.Px(),tau1.Py(),tau1.Pz());
	pm.SetXYZ(chargPart1.Px(),chargPart1.Py(),chargPart1.Pz());
	pp.SetXYZ(chargPart2.Px(),chargPart2.Py(),chargPart2.Pz());

	nm = (km.Cross(pm)).Unit(); np = (km.Cross(pp)).Unit(); ez = km.Unit();

	// Step 4: Calculating PhiCP
	this->SetGenPhi(acos(np.Dot(nm)));
	double phiCP = 0;
	if(ez.Dot(np.Cross(nm))>=0)
	{
		phiCP = acos(np.Dot(nm));
	}
	else
	{
		phiCP = 2*ROOT::Math::Pi()-acos(np.Dot(nm));
	}
	return phiCP;
}


// calculation of the charged prong energy in tau restframe
double CPQuantities::CalculateChargedProngEnergy(RMFLV tau, RMFLV chargedProng)
{
	// Step 1: Creating boost to Tau restframe
	RMFLV::BetaVector boosttauvect = tau.BoostToCM();
	ROOT::Math::Boost TauRestFrame(boosttauvect);

	// Step 2: Boosting charged Prong 4-momentum vector and extracting energy
	chargedProng = TauRestFrame * chargedProng;
	return chargedProng.E();
}


// Calculate longitudinal polarization variables (z+, z-, zs)
double CPQuantities::CalculateZPlusMinus(RMFLV higgs, RMFLV chargedPart)
{
	//calculating boost into higgs restframe
	RMFLV::BetaVector boostHiggs = higgs.BoostToCM();
	ROOT::Math::Boost higgsRestFrame(boostHiggs);

	//boost particles into rest frame
	higgs = higgsRestFrame * higgs;
	chargedPart = higgsRestFrame * chargedPart;

	// calculate Z+-
	double zPlusMinus = 2 * chargedPart.E() / higgs.E();
	return zPlusMinus;
}


double CPQuantities::CalculateZs(double zPlus, double zMinus)
{
	//calculate the surface between z+ = z- and z+ = z- + a for each event
	//z+ and z- are in range [0,1]. So maximum surface is 0.5
	//negative a defines the surface below the diagonal line
	double a = zPlus - zMinus;
	double zs = 0;
	if (a >= 0)
	{
		zs = 0.5 * (1 - ((1 - a) * (1 - a)));
	}
	else
	{
		a = -a;
		zs = 0.5 * (1 - ((1 - a) * (1 - a)));
		zs = -zs;
	}
	return zs;
}


double CPQuantities::PhiTransform(double phi)
{
	phi = 	fmod((phi + ROOT::Math::Pi()),(2 * ROOT::Math::Pi()));
	return phi;
}
