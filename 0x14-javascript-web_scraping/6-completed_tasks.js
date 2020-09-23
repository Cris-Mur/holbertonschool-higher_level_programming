#!/usr/bin/node
const req = require('request');
const nget = {};

req(process.argv[2], function (error, response, body) {
  if (!error) {
    const killer = JSON.parse(body);
    for (const yale of killer) {
      if (yale.completed === true) {
        if (nget[yale.userId] === undefined) { nget[yale.userId] = 0; }
        nget[yale.userId]++;
      }
    }
    console.log(nget);
  }
});
