#!/usr/bin/node
const Rex = /^[0-9]*?.[0-9]*$/;
const n = process.argv[2];

const facto = (n) => {
  if (n === 0) {
    return 1;
  }
  return n * facto(n - 1);
};

if (Rex.text(n)) {
  console.log(facto(parseInt(n)));
} else {
  console.log(1);
}
