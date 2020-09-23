#!/usr/bin/node

const sys = require('fs');
const req = require('request');

req(process.argv[2], function (error, body, response) {
  if (body !== undefined) {
    sys.writeFile(process.argv[3], response, 'utf-8', function (error) {
      if (error) console.log(error);
    });
  } else console.log(error);
});
