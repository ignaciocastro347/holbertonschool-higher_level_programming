#!/usr/bin/node
const amountArgs = Object.keys(process.argv).length - 2;

if (amountArgs === 0) {
  console.log('No argument');
} else if (amountArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
