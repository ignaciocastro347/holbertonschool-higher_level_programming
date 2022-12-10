#!/usr/bin/node
const args = Object.values(process.argv).slice(2);

if (!Number.isInteger(args[0])) {
  console.log('Not a number');
} else {
  console.log(parseInt(args[0]));
}
