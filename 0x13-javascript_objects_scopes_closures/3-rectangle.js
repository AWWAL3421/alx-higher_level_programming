#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let rectangle = '';
    for (let i = 0; i < this.height; i++) {
      rectangle += 'X'.repeat(this.width) + '\n';
    }
    console.log(rectangle);
  }
}

module.exports = Rectangle;
