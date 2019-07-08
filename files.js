var fs  = require("fs");

//Asynchronous read
fs.readFile('files.txt', function (err, data){
	if(err){
		return console.error(err);
	}
	console.log("Asynchronous read" + data.toString());
});

//synchronous read
var data = fs.readFileSync('files.txt');
console.log("synchronous read" + data.toString());
console.log("Program ended");