#!/usr/bin/node
// prints all characters of a Star Wars movie.
const request = require('request');
const link = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(link, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    _printChars(characters, 0);
  }
});

function _printChars (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        _printChars(characters, index + 1);
      }
    }
  });
}
