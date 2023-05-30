
$(function () {
    document.getElementById('downloadTable').addEventListener('click', function () {
        exportToCsv('internsTable');
    });
});

/**
 * exportToCsv - dwonloads the table containing data of Interns in csv format
 * to client's local machine 
 * @param {*} tableId 
 */
function exportToCsv(tableId) {
    // const table = document.getElementById(tableId);
    const rows = document.querySelectorAll('table#' + tableId + ' tr');


    const separator = ',';

    const csv = [];
    for (let i = 0; i < rows.length; i++) {
        let row = [];
        let cols = rows[i].querySelectorAll('td, th');
        console.log(cols)
        for (let j = 0; j < cols.length; j++) {
            // Clean innertext to remove multiple spaces and jumpline (break csv)
            let data = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, '').replace(/(\s\s)/gm, ' ')
            // Escape double-quote with double-double-quote (see https://stackoverflow.com/questions/17808511/properly-escape-a-double-quote-in-csv)
            data = data.replace(/"/g, '""');
            // Push escaped string
            row.push('"' + data + '"');
        }
        csv.push(row.join(separator));
    }
    // separate the rows with newline
    const csvString = csv.join('\n');
    // Download it
    const filename = 'export_' + tableId + '_' + new Date().toLocaleDateString() + '.csv';
    const link = document.createElement('a');
    link.style.display = 'none';
    link.setAttribute('target', '_blank');
    link.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvString));
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}