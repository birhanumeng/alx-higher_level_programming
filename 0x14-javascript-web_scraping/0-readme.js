#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (data, err) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
