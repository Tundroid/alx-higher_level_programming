#!/usr/bin/node
if (!Number(process.argv[2])) {
  console.log('No a number');
} else {
  console.log('My number:', Number(process.argv[2]));
}
