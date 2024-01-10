#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      const shape = (c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1);
      console.log(shape);
    }
  }
}
module.exports = Square;
