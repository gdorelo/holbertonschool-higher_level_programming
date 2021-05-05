#!/usr/bin/node

// Read the file and print its contents.
const link = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(link, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filename, body, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
