#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file_path = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file_path, body, 'utf8', (err) => {
    if (err) {
      console.log(error);
    }
  });
});
