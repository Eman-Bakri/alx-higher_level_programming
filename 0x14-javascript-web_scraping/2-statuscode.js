#!/usr/bin/node
// displays status code of a GET request.
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});