#!/usr/bin/node
const ng_universities = require('ng_universities')
const fs = require('fs');


function exportDataToFile() {
    const allUniversities = ng_universities.getUniversities();
    fs.writeFile('universities.json', allUniversities, (err) => {
        if (err) {
            throw Error("Unable to write to file");
        } else {
            console.log("Write success!");
        }
    });
}
exportDataToFile();
