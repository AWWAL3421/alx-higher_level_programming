#!/usr/bin/node
// Prints the first argument passed to the script
const firstArg = process.argv[2];

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
