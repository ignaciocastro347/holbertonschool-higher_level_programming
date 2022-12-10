#!/usr/bin/node

const args = Object.values(process.argv).slice(2);

if (!args[0] || args[0] === 1) {
  console.log(0);
} else {
  const sorted = arr.slice().sort((a, b) => a - b);
  const secondBiggest = sorted.slice(-2, -1)[0];
  console.log(secondBiggest);
}
