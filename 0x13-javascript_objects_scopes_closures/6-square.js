#!/usr/bin/node
const Squares = require('./5-square');

class Square extends Squares {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let x = 0; x < this.height; x++) {
      console.log(row);
    }
  }
}

module.exports = Square;
