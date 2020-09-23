#!/usr/bin/node
const req = require('request');
const pnt = process.argv[2];
const zelda = `https://swapi-api.hbtn.io/api/films/${pnt}/`;
req.get(zelda, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
