#!/usr/bin/node
let i;
const Rex = /^[0-9]*.[0-9]*$/;

if (Rex.test(process.argv[2])) {
  for (i = 0; i <= (parseInt(process.argv[2]) - 1); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
