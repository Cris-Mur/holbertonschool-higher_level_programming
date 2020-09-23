#!/usr/bin/node
const req = require('request');
const zelda = process.argv[2];
req.get(zelda).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
