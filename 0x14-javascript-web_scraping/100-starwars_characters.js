#!/usr/bin/node
// prints all characters of a Star Wars movie.
const req = require('request');
const id = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/';
req.get(link + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const moviedd = data.characters;
  for (const i of moviedd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
