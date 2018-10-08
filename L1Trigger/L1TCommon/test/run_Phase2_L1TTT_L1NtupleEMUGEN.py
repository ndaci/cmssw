# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --python_filename=run_Phase2_L1TTT_L1NtupleEMUGEN.py --no_exec -s L1 --datatier GEN-SIM-DIGI-RAW -n 10 --era Phase2_trigger --eventcontent FEVTDEBUGHLT --filein root://cms-xrd-global.cern.ch//store/mc/PhaseIIFall17D/SingleNeutrino/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/80000/00157B11-405C-E811-89CA-0CC47AFB81B4.root --fileout file:step2_2ev_rerun-L1_slim.root --conditions 100X_upgrade2023_realistic_v1 --beamspot HLLHC14TeV --geometry Extended2023D17 --customise=L1Trigger/Configuration/customiseUtils.L1TrackTriggerTracklet --customise=L1Trigger/Configuration/customiseUtils.DropDepricatedProducts --customise=L1Trigger/Configuration/customiseUtils.DropOutputProducts --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN --customise_commands process.FEVTDEBUGHLToutput.compressionLevel = cms.untracked.int32(2)
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('L1',eras.Phase2_trigger)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        #'root://cms-xrd-global.cern.ch//store/mc/PhaseIIFall17D/SingleNeutrino/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/80000/00157B11-405C-E811-89CA-0CC47AFB81B4.root'
        #'root://cms-xrd-global.cern.ch//store/mc/PhaseIIFall17D/SingleE_FlatPt-2to100/GEN-SIM-DIGI-RAW/L1TnoPU_93X_upgrade2023_realistic_v5-v1/80000/FC8DFF4F-B437-E811-8EE8-001E67792486.root'
        'root://cms-xrd-global.cern.ch//store/mc/PhaseIIFall17D/SingleE_FlatPt-2to100/GEN-SIM-DIGI-RAW/L1TPU200_93X_upgrade2023_realistic_v5-v1/80000/009B95F6-2438-E811-AEED-0090FAA58254.root'
        ),
    secondaryFileNames = cms.untracked.vstring()
    )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2_2ev_rerun-L1_slim.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2023_realistic_v1', '')

# Path and EndPath definitions
process.pL1TkPrimaryVertex = cms.Path(process.L1TkPrimaryVertex)
process.pL1TkElectrons = cms.Path(process.L1TkElectrons)
process.pL1TrackerHTMiss = cms.Path(process.L1TrackerHTMiss)
process.pL1TkPhotons = cms.Path(process.L1TkPhotons)
process.pL1TkGlbMuon = cms.Path(process.L1TkGlbMuons)
process.pL1TkMuon = cms.Path(process.L1TkMuons)
process.pL1TrkMET = cms.Path(process.L1TrackerEtMiss)
process.pL1TkTauFromCalo = cms.Path(process.L1TkTauFromCalo)
process.pL1TkCaloHTMissVtx = cms.Path(process.L1TkCaloHTMissVtx)
process.pL1TrackerJets = cms.Path(process.L1TrackerJets)
process.pL1TkCaloJets = cms.Path(process.L1TkCaloJets)
process.pL1TkIsoElectrons = cms.Path(process.L1TkIsoElectrons)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput) #ND

# HGCAL Ntuples: original clusters #ND
process.load('L1Trigger.L1THGCal.hgcalTriggerNtuplesReadOnly_cff')
process.hgc_ntuple_step_readonly = cms.Path(process.hgcalTriggerNtuplesReadOnly)

# HGCAL Ntuples: latest collections (ie the reproduced ones if any) #ND
process.load('L1Trigger.L1THGCal.hgcalTriggerNtuples_cff')
process.hgc_ntuple_step = cms.Path(process.hgcalTriggerNtuples)

# Schedule definition #ND
process.schedule = cms.Schedule(
    process.L1simulation_step,
    process.hgc_ntuple_step_readonly, #ND
    process.hgc_ntuple_step, #ND
    process.endjob_step,
    #process.FEVTDEBUGHLToutput_step #ND
    )

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseUtils
from L1Trigger.Configuration.customiseUtils import L1TrackTriggerTracklet,DropDepricatedProducts,DropOutputProducts 

#call to customisation function L1TrackTriggerTracklet imported from L1Trigger.Configuration.customiseUtils
process = L1TrackTriggerTracklet(process)

#call to customisation function DropDepricatedProducts imported from L1Trigger.Configuration.customiseUtils
process = DropDepricatedProducts(process)

#call to customisation function DropOutputProducts imported from L1Trigger.Configuration.customiseUtils
process = DropOutputProducts(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleEMU,L1NtupleGEN 

#call to customisation function L1NtupleEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleEMU(process)

#call to customisation function L1NtupleGEN imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleGEN(process)

# End of customisation functions

# Customisation from command line

process.FEVTDEBUGHLToutput.compressionLevel = cms.untracked.int32(2)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
