#!/usr/bin/node
// define rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = h;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
