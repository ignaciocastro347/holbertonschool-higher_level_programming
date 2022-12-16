#!/usr/bin/node

const request = require('request');
const args = Object.values(process.argv).slice(2);

request(args[0], function (error, response, body) {
  if (error) console.log(error);
  console.log('code: ', response && response.statusCode);
});
