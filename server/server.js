const express = require('express');
const path = require('path');
const bodyParser = require('body-parser'); // Add this line
const fs = require('fs');
const cors = require('cors');
const {spawn} = require("child_process");


const app = express();
const port = process.env.PORT || 8080;

app.use(cors({origin:"http://192.168.1.145:8080"}))
app.use(express.static(__dirname));
app.use(express.static('assets'))
app.use(express.static('/node_modules/perfume.js/dist/'))
app.use(bodyParser.urlencoded({extended: true})); // Add this line

let counter = 0; // change for number of browser you are using (e.g Mac with Safari or not )

function appendDataToFile(filePath, data) {
    fs.appendFile(filePath, data, function (err) {
        if (err) throw err;
        console.log('Saved!')
    });
}

app.post('/performance_results', bodyParser.json(), (req, res) => {
    let result = req.body;

    new_line =
        result.browser + ',' +
        result.FCP + ',' +
        result.TTFB + ',' +
        //result.LCP + ',' +
        //result.FID + ',' +
        result.PLT + ',' +
        result.navigationTiming.fetchTime+ "\n";

    new_line_file = ""

    result.resourceTiming.forEach(element => {
        if (element.initiatorType === "img") {
            new_line_file += element.name + ',' + element.duration +"\n"
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
        case 'brave':
            appendDataToFile('./results/brave.csv', new_line);
            appendDataToFile('./results/brave_resources.csv', new_line_file);
        default:
            appendDataToFile('./results/other.csv', new_line);
            appendDataToFile('./results/other_resources.csv', new_line_file);
            break;
    }

    console.log("Results logged from: " + result.browser );
    console.log("Counter < 5 change images: " + counter);

    counter += 1;
    console.log(counter)

    if(counter === 5){
        const spawn = require('child_process').spawn;
        const ls = spawn('python', ['script.py', 'arg1', 'arg2']);
    }

    res.send('POST request to the homepage');
});


app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.get("/mix", function (req, res) {
    const spawn = require('child_process').spawn;
    const ls = spawn('python3', ['randomize_images.py']);
    //print output of randomize_images.py
    ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    res.send('Proceeded');
});

app.listen(port);
console.log('Server started at http://192.168.1.145:' + port);