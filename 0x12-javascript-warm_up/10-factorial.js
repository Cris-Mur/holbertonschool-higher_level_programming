#!/usr/bin/node
const Rex = /^[0-9]*?.[0-9]*$/;
const n = process.argv[2];

function facto = (n) => {
  if (n === 0) {
    return 1;
  }
  return n * facto(n - 1);
};

if (Rex.test(n)) {
  console.log(facto(parseInt(n)));
} else {
  console.log(1);
}
