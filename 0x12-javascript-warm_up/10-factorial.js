#!/usr/bin/node
function fac (num) {
  if (num !== 0) {
    return num * fac(num - 1);
  } else {
    return 1;
  }
}
const myArgs = process.argv;
if (parseInt(myArgs[2])) {
  console.log(fac(parseInt(myArgs[2])));
} else {
  console.log(1);
}
