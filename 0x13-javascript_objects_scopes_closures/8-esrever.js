#!/usr/bin/node
exports.esrever = function (list) {
  const reversL = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversL[j] = list[i];
    j++;
  }
  return reversL;
};
