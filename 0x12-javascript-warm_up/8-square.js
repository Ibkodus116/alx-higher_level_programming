#!/usr/bin/node
const myArgs = process.argv;
const sqr = parseInt(myArgs[2]);
let str = '';

if (sqr) {
  for (let i = 0; i < sqr; i++) {
    str += 'X';
  }
  for (let j = 0; j < sqr; j++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
