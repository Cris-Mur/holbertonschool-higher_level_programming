#!/usr/bin/node
const req = require('request');
const zelda = process.argv[2];
req.get(zelda, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let cont = 0;
    const ready = JSON.parse(body).results;
    for (const titles of ready) {
      const into = titles.characters;
      for (const charter of into) {
        if (charter.includes('18')) cont++;
      }
    }
    console.log(cont);
  }
});