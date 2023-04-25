#!/usr/bin/node

'use strict';

const request = require('request');

const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
