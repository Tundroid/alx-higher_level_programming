#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  let square = 'X'.repeat(size) + '\n';
  square = square.repeat(size);
  console.log(square);
}
