#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (cosito) {
    if (cosito === undefined) {
      this.print();
    } else {
      let y;
      for (y = 0; y < this.height; y++) {
        console.log(cosito.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
