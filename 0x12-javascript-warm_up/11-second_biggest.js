#!/usr/bin/node
if (!parseInt(process.argv[2] || process.argv.length === 3)) {
  console.log(0);
} else {
  process.argv.forEach(element => {
    console(element);
  });
}
