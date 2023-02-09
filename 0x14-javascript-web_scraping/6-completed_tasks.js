#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const users = JSON.parse(body).reduce((accumulator, currentValue) => {
    if (currentValue.completed) {
      if (accumulator[currentValue.userId]) {
        accumulator[currentValue.userId]++;
      } else {
        accumulator[currentValue.userId] = 1;
      }
    }
    return accumulator;
  }, {});
  console.log(users);
});
