#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < x; count++) {
    console.log('C is fun');
  }
}
