#!/usr/bin/node
const myArgs = process.argv;
if (parseInt(myArgs[2])) {
  for (let i = 0; i < myArgs[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
