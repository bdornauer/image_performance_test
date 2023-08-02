const express = require('express');
const path = require('path');
const bodyParser = require('body-parser'); // Add this line
const fs = require('fs');
const cors = require('cors');


const app = express();
const port = process.env.PORT || 8080;

app.use(cors({origin:"http://192.168.1.145:8080"}))

app.use(express.static(__dirname));
app.use(express.static('assets'))
app.use(express.static('/node_modules/perfume.js/dist/'))
app.use(bodyParser.urlencoded({extended: true})); // Add this line

function appendDataToFile(filePath, data) {
    fs.appendFile(filePath, data + '\n', function (err) {
        if (err) throw err;
        console.log('Data appended to file');
    });
}

app.post('/performance_results', bodyParser.json(), (req, res) => {
    let result = req.body;
    console.log(req.body)
    console.log(result);
    // Browser,FCP,TTFB,LCP,FID,PLT,fetch_time
    new_line =
        result.browser + ',' +
        result.FCP + ',' +
        result.TTFB + ',' +
        result.LCP + ',' +
        result.FID + ',' +
        result.PLT + ',' +
        result.navigationTiming.fetchTime;

    new_line_file = ""

    result.resourceTiming.forEach(element => {
        if (element.initiatorType === "img") {
            new_line_file += element.name + ',' + element.duration
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

    res.send('POST request to the homepage');
});


app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.listen(port);
console.log('Server started at http://192.168.1.145:' + port);
