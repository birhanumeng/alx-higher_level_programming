#!/usr/bin/node
const mySquare = require('./5-square');
class Square extends mySquare {
  charPrint (c) {
    if (c === undefined) {
      mySquare.print();
    } else {
      let i, j;
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
