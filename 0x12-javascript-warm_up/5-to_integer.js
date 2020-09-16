#!/usr/bin/node
const Rex = /^[0-9]*?.[0-9]*$/;

if (Rex.test(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
