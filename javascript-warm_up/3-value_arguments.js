#!/usr/bin/node
const amountArgs = Object.keys(process.argv).length - 2;

if (amountArgs === 0) {
  console.log('No argument');
} else {
	for (arg of process.argv.slice(2)) {
		console.log(arg);
	}
}
