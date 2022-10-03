#!/usr/bin/node
// prints C is fun 'x' times
let x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= x; x++) { console.log(process.argv[i]); }
}
