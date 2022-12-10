#!/usr/bin/node

const args = Object.values(process.argv).slice(2);

const n = Number(args[0]);

function factorial (n) {
  let factorial = 1;
  for (let i = n; i > 1; i--) {
    factorial *= i;
  }
  return factorial;
}

console.log(factorial(n));
