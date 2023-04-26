#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completed = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (!completed[todo.userId]) {
        completed[todo.userId] = 0;
      }

      completed[todo.userId]++;
    }
  }

  for (const userId in completed) {
    console.log(`${userId} : ${completed[userId]}`);
  }
});
