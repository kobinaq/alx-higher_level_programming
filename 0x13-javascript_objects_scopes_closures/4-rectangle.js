#!/usr/bin/node

class Ractangle
{
  constructor (w,h)
  {
    if (w > 0 && h > 0)
    {
      this.width = w;
      this.height = h;
    }
  }

  print ()
  {
    for (let i = 0; i < this.height; i++)
    {
      console.log('X'.repeat(this.width));
    }
  }

  Rotate ()
  {
    [this.width, this.height] = [this.height, this.width];
  }

  Double ()
  {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
