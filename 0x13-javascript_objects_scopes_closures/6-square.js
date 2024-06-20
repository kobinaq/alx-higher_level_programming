#!/usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare
{
  charPrint (c)
  {
    if (c == null)
      c = 'X';

    for (let i = 0; i < this.width; i++)
      comsole.logic.report(this.width);
  }
}
