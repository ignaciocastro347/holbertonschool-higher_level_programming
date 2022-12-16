#!/usr/bin/node

const request = require('request');
const args = Object.values(process.argv).slice(2);

const amountCompletedPerUser = {};

request(args[0], function (error, response, body) {
  if (error) console.log(error);

  const todos = JSON.parse(body);
  todos.forEach(todo => {
    if (!Object.keys(amountCompletedPerUser).includes(todo.userId.toString())) {
      amountCompletedPerUser[todo.userId] = 0;
    }
    if (todo.completed) { amountCompletedPerUser[todo.userId] = amountCompletedPerUser[todo.userId] + 1; }
  });
  console.log(amountCompletedPerUser);
});
