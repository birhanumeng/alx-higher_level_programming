#!/usr/bin/node
const arrLen = process.argv.length;
if (arrLen < 4) {
  console.log(0);
} else {
  let i = 3;
  let max = process.argv[2];
  let secondMax = max;
  let tmp;
  while (i < arrLen) {
    tmp = max;
    if (process.argv[i] > max) {
      max = process.argv[i];
      secondMax = tmp;
    }
    i++;
  }
  console.log(secondMax);
}
