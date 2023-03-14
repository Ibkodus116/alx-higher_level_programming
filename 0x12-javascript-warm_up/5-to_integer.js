#!/usr/bin/node
const myArgs = process.argv;
if (parseInt(myArgs[2])) {
  console.log(`My number: ${parseInt(myArgs[2])}`);
} else {
  console.log('Not a number');
}
