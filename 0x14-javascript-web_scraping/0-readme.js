#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (err, content) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(content);
});
