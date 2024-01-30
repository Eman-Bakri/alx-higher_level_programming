#!/usr/bin/node
// prints the title of a Star Wars movie.
const request = require('request');
const epNum = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/';

request(link + epNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
