#!/usr/bin/node
const GL = require('./100-data').list;
const ML = GL.map((x, index) => x * index);
console.log(GL);
console.log(ML);
