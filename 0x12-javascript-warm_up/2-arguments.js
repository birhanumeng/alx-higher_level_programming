#!/usr/bin/node
const Argv = process.argv.length;
if (Argv === 2) {
  console.log('No argument');
} else if (Argv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
