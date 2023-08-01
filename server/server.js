const express = require('express');
const path = require('path');
const bodyParser = require('body-parser'); // Add this line


const app = express();
const port = process.env.PORT || 8080;


app.use(express.static(__dirname));
app.use(express.static('assets'))
app.use(express.static('/node_modules/perfume.js/dist/'))
app.use(bodyParser.urlencoded({ extended: true })); // Add this line


app.post('/performance_results', bodyParser.json(), (req, res) => {
    // print JSON response to output console
    console.log("result: ", req.body);
    res.send('POST request to the homepage');
});

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.listen(port);
console.log('Server started at http://localhost:' + port);
