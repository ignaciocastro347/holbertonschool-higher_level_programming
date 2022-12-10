#!/usr/bin/node
const args = Object.values(process.argv).slice(2);
const number = parseInt(args[0])
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
