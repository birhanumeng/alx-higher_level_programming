#!/usr/bin/node
let prNum = 0;
exports.logMe = function (item) {
  console.log(`${prNum++}: ${item}`);
};
