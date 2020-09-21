#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if ((parseInt(width) > 0) && (parseInt(height) > 0)) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let y;
    for (y = 0; y < this.height; y++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
