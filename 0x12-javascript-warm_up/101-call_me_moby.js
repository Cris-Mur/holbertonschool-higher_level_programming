#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let stp = 0;
  for (stp = 0; stp < x; stp++) {
    theFunction();
  }
};
