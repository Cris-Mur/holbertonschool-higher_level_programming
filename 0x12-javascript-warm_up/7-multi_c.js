#!/usr/bin/node
let i;
const Rex = /^[0-9]*.[0-9]*$/;

if (Rex.test(process.argv[2])) {
  for (i = 0; i <= (parseInt(process.argv[2]) - 1); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
