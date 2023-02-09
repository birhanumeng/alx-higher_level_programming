#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const chars = JSON.parse(body).characters;
    chars.forEach((ch) => {
      request(ch, (err, res, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
