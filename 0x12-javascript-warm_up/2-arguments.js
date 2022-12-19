#!/usr/bin/node
const arg_v = process.argv.length;
if (arg_v === 2) console.log('No argument');
if (arg_v === 3) console.log('Argument found');
if (arg_v > 3) console.log('Arguments found');
