#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = Object.values(process.argv).slice(2);

request(args[0], function (error, response, body) {
  if (error) console.log(error);

  fs.writeFile(args[1], body, err => {
    if (err) console.error(err);
  });
});
