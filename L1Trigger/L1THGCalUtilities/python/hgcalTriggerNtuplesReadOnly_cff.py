import FWCore.ParameterSet.Config as cms

from L1Trigger.L1THGCalUtilities.hgcalTriggerNtuplesReadOnly_cfi import *

hgcalTriggerNtuplesReadOnly = cms.Sequence(hgcalTriggerNtuplizerReadOnly)

from Configuration.Eras.Modifier_phase2_hgcalV9_cff import phase2_hgcalV9
from L1Trigger.L1THGCalUtilities.customNtuples import custom_ntuples_V9
modifyHgcalTriggerNtuplesWithV9Geometry_ = phase2_hgcalV9.makeProcessModifier(custom_ntuples_V9)


