#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[1];
const filePath = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8');
  }
});
