#!/usr/bin/node

const args = Object.values(process.argv).slice(2);

const n = Number(args[0]);

let factorial = 1;
for (let i = n; i > 1; i--) {
  factorial *= i;
}

console.log(factorial);
