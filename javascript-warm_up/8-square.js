#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < size; count++) {
    console.log('X'.repeat(size));
  }
}
