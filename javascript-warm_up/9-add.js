#!/usr/bin/node

const args = Object.values(process.argv).slice(2);

function add (a, b) {
  return Number(a) + Number(b);
}

console.log(add(args[0], args[1]));
