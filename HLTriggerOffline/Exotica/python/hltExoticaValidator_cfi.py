### Configuration Fragment Include for HLTExoticaValidator module.
### In this file we instantiate the HLTExoticaValidator, with
### some default configurations. The specific analyses are loaded
### as cms.PSets, which are then added to this module with
### specific names. The canonical example is 
#
# from HLTriggerOffline.Exotica.hltExoticaHighPtDimuon_cff import HighPtDimuonPSet
#
# which is then made known to the module by the line
#
# analysis       = cms.vstring("HighPtDimuon"),
#

import FWCore.ParameterSet.Config as cms

# Validation categories (sub-analyses)
from HLTriggerOffline.Exotica.analyses.hltExoticaHighPtDimuon_cff      import HighPtDimuonPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaHighPtDielectron_cff  import HighPtDielectronPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaLowPtDimuon_cff       import LowPtDimuonPSet
#from HLTriggerOffline.Exotica.analyses.hltExoticaLowPtDielectron_cff   import LowPtDielectronPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaHighPtElectron_cff    import HighPtElectronPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaLowPtElectron_cff     import LowPtElectronPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaHighPtPhoton_cff      import HighPtPhotonPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaDiPhoton_cff          import DiPhotonPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaHT_cff                import HTPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaJetNoBptx_cff         import JetNoBptxPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaMuonNoBptx_cff        import MuonNoBptxPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaDisplacedEleMu_cff    import DisplacedEleMuPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaDisplacedDimuon_cff   import DisplacedDimuonPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaDisplacedL2Dimuon_cff import DisplacedL2DimuonPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaPureMET_cff           import PureMETPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaMETplusTrack_cff      import METplusTrackPSet
from HLTriggerOffline.Exotica.analyses.hltExoticaMonojet_cff           import MonojetPSet

hltExoticaValidator = cms.EDAnalyzer(

    "HLTExoticaValidator",
		
    hltProcessName = cms.string("HLT"),
    
    # -- The name of the analysis. This is the name that
    # appears in Run summary/Exotica/ANALYSIS_NAME

    analysis       = cms.vstring("HighPtDimuon",
                                 "HighPtDielectron",
                                 "LowPtDimuon",
                                 #"LowPtDielectron",
                                 "HighPtElectron",
                                 "LowPtElectron",
                                 "HighPtPhoton",
                                 "DiPhoton",
                                 "JetNoBptx",
                                 "MuonNoBptx",
                                 "HT",
                                 "DisplacedEleMu",
                                 "DisplacedDimuon",
                                 "DisplacedL2Dimuon",
                                 "PureMET",
                                 "METplusTrack",
                                 "Monojet"
                                 ),
    
    # -- The instance name of the reco::GenParticles collection
    genParticleLabel = cms.string("genParticles"),

    # -- The binning of the Pt efficiency plots
    # NOTICE: these DEFINITELY should be tuned for the different analyses.
    # What we have there is a generic, 0-100 GeV uniform binning.
    parametersTurnOn = cms.vdouble( 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
                                   22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
                                   42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
                                   62, 64, 66, 68, 70, 72, 74, 76, 78, 80,
                                   82, 84, 86, 88, 90, 92, 94, 96, 98, 100,
                                   ),

    # -- (NBins, minVal, maxValue) for the Eta and Phi efficiency plots
    parametersEta      = cms.vdouble(48, -2.400, 2.400),
    parametersPhi      = cms.vdouble(50, -3.142, 3.142),

    # Definition of generic cuts on generated and reconstructed objects (note that
    # these cuts can be overloaded inside a particular analysis)
    # Objects recognized: Mu Ele Photon PFTau Jet MET => recognized by the method EVTColContainer::getTypeString
    # Syntax in the strings: valid syntax of the StringCutObjectSelector class

    # --- Muons
    Mu_genCut     = cms.string("pt > 10 && abs(eta) < 2.4 && abs(pdgId) == 13 && status == 1"),
    Mu_recCut     = cms.string("pt > 10 && abs(eta) < 2.4 && isPFMuon && (isTrackerMuon || isGlobalMuon)"), # Loose Muon
    
    # --- MuonTracks
    #refittedStandAloneMuons_genCut  = cms.string("pt > 10 && abs(eta) < 2.4 && abs(pdgId) == 13 && status == 1"),
    refittedStandAloneMuons_genCut  = cms.string("pt > 10 && abs(eta) < 2.4"),
    #refittedStandAloneMuons_recCut  = cms.string("pt > 10 && abs(eta) < 2.4 && isPFMuon && (isTrackerMuon || isGlobalMuon)"), # Loose Muon
    refittedStandAloneMuons_recCut  = cms.string("pt > 10 && abs(eta) < 2.4"), 

    # --- Electrons
    Ele_genCut      = cms.string("pt > 10 && (abs(eta)<1.444 || abs(eta)>1.566) && abs(eta)<2.5 && abs(pdgId) == 11 && status==3 "),
    Ele_recCut      = cms.string(
        "pt > 10 && (abs(eta)<1.444 || abs(eta)>1.566) && abs(eta)< 2.5 "+
        " && hadronicOverEm < 0.05 "+ #&& eSuperClusterOverP > 0.5 && eSuperClusterOverP < 1.5 "+
        " && abs(deltaEtaSuperClusterTrackAtVtx)<0.007 &&  abs(deltaPhiSuperClusterTrackAtVtx)<0.06 "+
        " && sigmaIetaIeta<0.03 "+
        " && (pfIsolationVariables.sumChargedParticlePt + pfIsolationVariables.sumNeutralHadronEtHighThreshold + pfIsolationVariables.sumPhotonEtHighThreshold )/pt < 0.10 "+
        " && abs(1/energy - 1/p)<0.05"),
        #" && abs(trackPositionAtVtx.z-vertexPosition.z)<"),
    #" && "), # Loose-like electron

    # --- Photons
    Photon_genCut     = cms.string("pt > 20 && abs(eta) < 2.4 && abs(pdgId) == 22 && status == 1"),
    Photon_recCut     = cms.string("pt > 20 && abs(eta) < 2.4"), # STILL MISSING THIS INFO
    Photon_genCut_leading  = cms.string("pt > 150 "),
    Photon_recCut_leading  = cms.string("pt > 150 "),
   
    # --- Taus: 
    PFTau_genCut      = cms.string("pt > 20 && abs(eta) < 2.4 && abs(pdgId) == 15 && status == 3"),
    PFTau_recCut      = cms.string("pt > 20 && abs(eta) < 2.4"),  # STILL MISSING THIS INFO
   
    # --- Jets: 
    PFJet_genCut      = cms.string("pt > 30 && abs(eta) < 2.4"),
    PFJet_recCut      = cms.string("pt > 30 && abs(eta) < 2.4 &&"+
                                     "(neutralHadronEnergy + HFHadronEnergy)/energy < 0.99 &&"+
                                     "neutralEmEnergyFraction < 0.99 &&"+
                                     "numberOfDaughters > 1 &&"+
                                     "chargedHadronEnergyFraction > 0 &&"+
                                     "chargedMultiplicity > 0 && "+
                                     "chargedEmEnergyFraction < 0.99"),  # Loose PFJet

    CaloJet_genCut      = cms.string("pt > 30 && abs(eta) < 2.4"),
    CaloJet_recCut      = cms.string("pt > 30 && abs(eta) < 2.4"), # find realistic cuts
   
    # --- MET (PF)    
    PFMET_genCut      = cms.string("pt > 75"),
    PFMET_recCut      = cms.string("pt > 75"),  
   
    # The specific parameters per analysis: the name of the parameter set has to be 
    # the same as the defined ones in the 'analysis' datamember. Each analysis is a PSet
    # with the mandatory attributes:
    #    - hltPathsToCheck (cms.vstring) : a list of all the trigger pats to be checked 
    #                 in this analysis. Up to the version number _v, but not including 
    #                 the number in order to avoid this version dependence. Example: HLT_Mu18_v
    #    - recVarLabel (cms.string): where Var is Mu, Ele, Photon, MET, Jet, PFTau, MET. This
    #                 attribute is the name of the INSTANCE LABEL for each RECO collection to 
    #                 be considered in the analysis. Note that the trigger paths rely on some 
    #                 objects which need to be defined here, otherwise the code will complain. 
    #    - minCandidates (cms.uint32): the minimum number of GEN/RECO objects in the event
    # Besides the mandatory attributes, you can redefine the generation and reconstruction cuts
    # for any object you want.
    #    * Var_genCut, Var_recCut (cms.string): where Var=Mu, Ele, Photon, Jet, PFTau, MET (see above)

    HighPtDimuon     = HighPtDimuonPSet,
    HighPtDielectron = HighPtDielectronPSet,
    LowPtDimuon      = LowPtDimuonPSet,
    #LowPtDielectron  = LowPtDielectronPSet,
    HighPtElectron   = HighPtElectronPSet,
    LowPtElectron    = LowPtElectronPSet,
    HighPtPhoton     = HighPtPhotonPSet,                                 
    DiPhoton         = DiPhotonPSet,                                 
    JetNoBptx        = JetNoBptxPSet,
    MuonNoBptx       = MuonNoBptxPSet,
    DisplacedEleMu   = DisplacedEleMuPSet,
    DisplacedDimuon  = DisplacedDimuonPSet,
    DisplacedL2Dimuon = DisplacedL2DimuonPSet,
    PureMET          = PureMETPSet,                                 
    METplusTrack     = METplusTrackPSet,                                 
    Monojet          = MonojetPSet,
    HT               = HTPSet
)
