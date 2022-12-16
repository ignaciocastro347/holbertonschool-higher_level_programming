#!/usr/bin/node

const request = require('request');
const args = Object.values(process.argv).slice(2);

request(`https://swapi-api.hbtn.io/api/films/${args[0]}`, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  console.log(data.title);
});
