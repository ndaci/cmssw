import FWCore.ParameterSet.Config as cms

from L1Trigger.L1THGCal.hgcalTriggerNtuplesReadOnly_cfi import *

hgcalTriggerNtuplesReadOnly = cms.Sequence(hgcalTriggerNtuplizerReadOnly)



