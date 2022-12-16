#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films', function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  const movies = data.results;
  let counter = 0;
  movies.forEach(movie => {
    for (const character of movie.characters) {
      const characterId = character.split('/')[5];
      if (characterId === '18') {
        counter++;
        break;
      }
    }
  });
  console.log(counter);
});
