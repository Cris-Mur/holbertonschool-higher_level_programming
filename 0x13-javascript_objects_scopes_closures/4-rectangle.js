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

  double () {
    this.height = parseInt(this.height) * 2;
    this.width = parseInt(this.width) * 2;
  }

  rotate () {
    const aux = parseInt(this.height);
    this.height = parseInt(this.width);
    this.width = aux;
  }
}
module.exports = Rectangle;
