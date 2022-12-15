#!/usr/bin/node

const fs = require('fs');
const args = Object.values(process.argv).slice(2);

fs.writeFile(args[0], args[1], err => {
  if (err) {
    console.error(err);
  }
});
