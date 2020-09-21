#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if ((parseInt(width) > 0) && (parseInt(height) > 0)) {
      this.width = width;
      this.height = height;
    }
  }
}
module.exports = Rectangle;
