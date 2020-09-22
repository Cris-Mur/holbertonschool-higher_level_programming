#!/usr/bin/node

exports.esrever = function (list) {
  let x = list.length - 1;
  const NL = [];
  for (let i = 0; x >= 0; x--, i++) {
    NL[i] = list[x];
  }
  return NL;
};
