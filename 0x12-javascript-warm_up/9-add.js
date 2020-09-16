#!/usr/bin/node

const y = process.argv[2];
const z = process.argv[3];
let x;
const plus = (y, z) => {
  x = parseInt(y) + parseInt(z);
  console.log(x);
};

plus(y, z);
