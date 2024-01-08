#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.forEach(element => {
    console.log(element);
  });
}
