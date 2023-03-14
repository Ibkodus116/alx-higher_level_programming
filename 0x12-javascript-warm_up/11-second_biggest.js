#!/usr/bin/node
function sBig (x) {
  let num = 0;
  let sec = 0;
  for (let i = 0; i < x.length; i++) {
    if (parseInt(x[i]) > num) {
      sec = num;
      num = parseInt(x[i]);
    } else if (parseInt(x[i]) > sec && parseInt(x[i]) < num) {
      sec = parseInt(x[i]);
    }
  }
  return sec;
}
const myArgs = process.argv;
const myArr = myArgs.slice(2);

console.log(sBig(myArr));
