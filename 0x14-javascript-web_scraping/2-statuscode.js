#!/usr/bin/node

'use strict';

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
