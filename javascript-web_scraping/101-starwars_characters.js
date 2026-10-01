#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  const names = [];
  let completed = 0;

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }

      const character = JSON.parse(body);

      names[index] = character.name;
      completed += 1;

      if (completed === characters.length) {
        names.forEach((name) => {
          console.log(name);
        });
      }
    });
  });
});
