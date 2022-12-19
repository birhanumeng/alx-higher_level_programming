#!/usr/bin/node
const size = parseInt(process.argv[2]);
let i = 0;
let j;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    for (j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
    i++;
  }
}
