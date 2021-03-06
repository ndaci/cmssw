#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/TransientTrack/interface/TrackTransientTrack.h"

#include <iostream>

using namespace reco;

typedef TrackTransientTrack                              TTT;


TransientTrack::TransientTrack( const Track & tk , const MagneticField* field) : 
  Base( new TTT(tk, field)) {}


TransientTrack::TransientTrack( const TrackRef & tk , const MagneticField* field) : 
  Base( new TTT(tk, field)) {}

TransientTrack::TransientTrack( const Track & tk , const MagneticField* field,
				const edm::ESHandle<GlobalTrackingGeometry>& tg) :
  Base( new TTT(tk, field, tg)) {}

TransientTrack::TransientTrack( const TrackRef & tk , const MagneticField* field,
				const edm::ESHandle<GlobalTrackingGeometry>& tg) :
  Base( new TTT(tk, field, tg)) {}


// TransientTrack::TransientTrack( const TransientTrack & tt ) :
//   Base( new TTT(tt)) {}


// TransientTrack& TransientTrack::operator=(const TransientTrack & tt) {
// //   std::cout << "assign op." << std::endl;
//   if (this == &tt) return *this;
//   //
//   //  std::cout << tt.tk_ << std::endl;
// //   std::cout << "assign base." << std::endl;
//   Track::operator=(tt);
// //   std::cout << "done assign base." << std::endl;
//   //  tk_ = &(tt.persistentTrack());
//   //  tk_ = tt.tk_;
// //   std::cout << "assign ref." << std::endl;
//   tkr_ = tt.persistentTrackRef();
//   initialTSOSAvailable =  tt.initialTSOSAvailable;
//   initialTSCPAvailable = tt.initialTSCPAvailable;
//   initialTSCP = tt.initialTSCP;
//   initialTSOS = tt.initialTSOS;
//   theField = tt.field();
//   initialFTS = tt.initialFreeState();
// //   std::cout << "assign op. OK" << std::endl;
//   
//   return *this;
// }
