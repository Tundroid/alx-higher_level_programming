#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length == 1) {
	console.log('No argument');
} else {
	console.log('Argument', argv.length == 2 ? 's ' : ' ', 'found');
}
