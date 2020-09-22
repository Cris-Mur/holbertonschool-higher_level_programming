#!/usr/bin/node
const sys = require('fs');
const file = process.argv[2];
const info = process.argv[3];

sys.writeFile(file, info, 'utf-8', function (err) {
  if (err) console.log(err);
});