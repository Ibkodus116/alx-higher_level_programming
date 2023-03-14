#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const myArgs = process.argv;
const a = parseInt(myArgs[2]);
const b = parseInt(myArgs[3]);
add(a, b);
