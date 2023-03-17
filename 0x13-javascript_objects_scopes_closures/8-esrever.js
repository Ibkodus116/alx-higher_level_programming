#!/usr/bin/node
function esrever (list) {
  const nList = [];
  const size = list.length - 1;
  for (let i = size; i >= 0; i--) {
    nList.push(list[i]);
  }
  return nList;
}
exports.esrever = function (list) {
  return esrever(list);
};
