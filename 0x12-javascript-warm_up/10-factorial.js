#!/usr/bin/node

const n = parseInt(process.argv[2]);

const facto = (n) => {
  if (n > 1) {
    return (facto(n - 1) * n);
  } else {
    return (n < 0 ? -1 : 1);
  }
};

console.log(facto(n));
