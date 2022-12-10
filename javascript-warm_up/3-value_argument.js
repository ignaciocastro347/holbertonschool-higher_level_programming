#!/usr/bin/node
const args = Object.values(process.argv).slice(2);

if (!args[0]) {
  console.log('No argument');
} else {
  for (arg of args) {
    console.log(arg);
  }
}
