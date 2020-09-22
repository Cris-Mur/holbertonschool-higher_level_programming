#!/usr/bin/node
const GL = require('./100-data').list;
const ML = GL.man((x, index) => x * index);
console.log(GL);
console.log(ML);
