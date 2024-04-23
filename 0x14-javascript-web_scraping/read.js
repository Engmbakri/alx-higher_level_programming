#!/usr/bin/node

const fs = require('fs');

fs.readFile('0-readme.js', 'utf-8', (err, data) => {
	if (err)
	{
		console.error('Error reading file', error);
	}
	else 
	{
		console.log('File content', data);
	}
});
