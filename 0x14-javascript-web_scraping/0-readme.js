#!/usr/bin/node
const sys = require('fs');
const file = process.argv[2];
sys.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
