#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const wedgeId = '/people/18/';
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movies = JSON.parse(body);

  movies.results.forEach((movie) => {
    const hasWedge = movie.characters.some((character) =>
      character.includes(wedgeId)
    );

    if (hasWedge) {
      count++;
    }
  });

  console.log(count);
});
