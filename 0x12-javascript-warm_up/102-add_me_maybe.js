#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const plus = number + 1;
  theFunction(plus);
};
