#!/usr/bin/node

const requests = require('request');
const url = process.argv[2];

requests(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const lists = JSON.parse(body).results;
  let count = 0;
  for (const l of lists) {
    for (const chars of l.characters) {
      if (chars.includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
