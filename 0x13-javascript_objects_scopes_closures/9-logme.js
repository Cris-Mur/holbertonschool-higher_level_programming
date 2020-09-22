#!/usr/bin/node
let nunm = 0;
exports.logMe = function (item) {
  console.log(nunm + `: ${item}`);
  nunm++;
};
