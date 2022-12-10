#!/usr/bin/node

const args = Object.values(process.argv).slice(2);

if (!args[0]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
