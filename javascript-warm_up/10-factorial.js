#!/usr/bin/node

const args = require('process').argv;
const num = parseInt(args[2]);
console.log(factorialize(num));

function factorialize (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0 || !num) {
    return 1;
  } else if (num === 1) {
    return 1;
  } else {
    return num * factorialize(num - 1);
  }
}
