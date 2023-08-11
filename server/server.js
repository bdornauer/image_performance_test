const express = require('express');
const path = require('path');
const bodyParser = require('body-parser'); // Add this line
const fs = require('fs');
const cors = require('cors');
const {spawn} = require("child_process");


const app = express();
const port = process.env.PORT || 8080;

let standard_image_format = "png"
let image_run_id = 0

app.use(cors({origin:"http://192.168.1.145:8080"}))
app.use(express.static(__dirname));
app.use(express.static('assets'))
app.use(express.static('/node_modules/perfume.js/dist/'))
app.use(bodyParser.urlencoded({extended: true})); // Add this line

function appendDataToFile(filePath, data) {
    fs.appendFile(filePath, data, function (err) {
        if (err) throw err;
    });
}

app.post('/performance_results', bodyParser.json(), (req, res) => {
    let result = req.body;

    new_line =
        image_run_id + ',' +
        result.browser + ',' +
        standard_image_format + ',' +
        result.FP + ',' +
        result.FCP + ',' +
        result.TTFB + ',' +
        result.PLT + ',' +
        result.navigationTiming.fetchTime+ "\n";

    new_line_file = ""
    result.resourceTiming.forEach(element => {
        if (element.initiatorType === "img") {
            new_line_file += image_run_id + "," + element.name + ',' + element.duration +"\n"
        }
    })

    let browser = result.browser;

    switch (browser) {
        case 'chrome':
            appendDataToFile('./results/chrome.csv', new_line);
            appendDataToFile('./results/chrome_resources.csv', new_line_file);
            break;
        case 'firefox':
            appendDataToFile('./results/firefox.csv', new_line);
            appendDataToFile('./results/firefox_resources.csv', new_line_file);
            break;
        case 'safari':
            appendDataToFile('./results/safari.csv', new_line);
            appendDataToFile('./results/safari_resources.csv', new_line_file);
            break;
        case 'edge_old':
            appendDataToFile('./results/edge_old.csv', new_line);
            appendDataToFile('./results/edge_old_resources.csv', new_line_file);
            break;
        case 'opera':
            appendDataToFile('./results/opera.csv', new_line);
            appendDataToFile('./results/opera_resources.csv', new_line_file);
            break;
        case 'edge_chromium':
            appendDataToFile('./results/edge_chrome.csv', new_line);
            appendDataToFile('./results/edge_chrome_resources.csv', new_line_file);
            break;
        default:
            appendDataToFile('./results/other.csv', new_line);
            appendDataToFile('./results/other_resources.csv', new_line_file);
            break;
    }

    console.log("Results logged from: " + result.browser );
    console.log("Image run id: " + image_run_id);
    image_run_id += 1
    res.send('POST request to the homepage');
});


app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.get("/mix", function (req, res) {
    console.log("mixing images");
    const spawn = require('child_process').spawn;
    const ls = spawn('python3', ['randomize_images.py']);
    //print output of randomize_images.py
    ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    res.send('Proceeded mix');
});


app.post("/change_image_format",bodyParser.json(), function (req, res) {
    console.log("changed image format to: " + req.body.image_format);

    standard_image_format = req.body.image_format;
    const spawn = require('child_process').spawn;
    const ls = spawn('python3', ['change_image_format.py', standard_image_format]);

    ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    res.send('Proceeded change format');
})

app.listen(port);
console.log('Server started at http://192.168.1.145:' + port);