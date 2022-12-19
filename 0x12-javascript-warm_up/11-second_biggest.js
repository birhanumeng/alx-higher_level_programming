#!/usr/bin/node
const arrLen = process.argv.length;
if (arrLen < 4) {
  console.log(0);
} else {
  let i = 2;
  let max = 0;
  let secondMax = 0;
  let tmp;
  while (i < arrLen) {
    tmp = max;
    if (process.argv[i] > max) {
      max = process.argv[i];
      secondMax = tmp;
    } else if (process.argv[i] > secondMax) {
      secondMax = process.argv[i];
    }
    i++;
  }
  console.log(secondMax);
}
