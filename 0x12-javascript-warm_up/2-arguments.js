#!/usr/bin/node
const arg_v = process.argv.length;
if (arg_v === 2) {
  console.log('No argument');
} else if (arg_v === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
