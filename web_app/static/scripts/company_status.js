const $loading = $('#loading');


/**
 * displayCompanyApplicationStatus - toggles the `Close/Open Application button 
 * and the status badge depending on the action of the client
 */
$(function displayCompanyApplicationStatus() {

    const $comId = $('#showStatus').data('button');
    // console.log($('#showStatus').text());

    $.get({
        url: `http://127.0.0.1:5001/api/v1/companies/${$comId}`,
        success: function (response) {

            // console.log(response.application_open);
            if (response.application_open) {
                if ($('button#showStatus').hasClass('btn-success')) {
                    $('button#showStatus').removeClass('btn-success').addClass('btn-danger');
                    $('button#showStatus').html('Close Application')
                    $('button#display-status').removeClass('btn-danger').addClass('btn-success');
                    $('button#display-status').html('open');
                }
            } else {
                if ($('button#showStatus').hasClass('btn-danger')) {
                    $('button#showStatus').removeClass('btn-danger').addClass('btn-success');
                    $('button#showStatus').html('Open Application')
                    $('button#display-status').html('closed');
                    $('button#display-status').removeClass('btn-success').addClass('btn-danger');
                }
            }
        },
        error: function (error) {
            if (error.status === 400) {
                alert(`Something went wrong. Please check your request`);
            } else {
                alert(`${error.status}`);
                location.reload();
            }
        },
        beforeSend: function () {
            $loading.show();
        },
        complete: function () {
            $loading.hide();
        }

    })
});
/**
 * getCompanyStatus - sets the company application open window
 * to either open or closed
 */
function getCompanyStatus() {

    const $comId = $('#showStatus').data('button');
    let reqData;


    $('button#showStatus').on('click', function () {
        const $statusText = $(this).text();

        console.log($statusText);

        if ($statusText === 'Close Application') {
            reqData = false;
        } else if ($statusText === 'Open Application') {
            reqData = true
        }
        // console.log(reqData);

        $.ajax({
            url: `http://127.0.0.1:5001/api/v1/companies/${$comId}`,
            type: 'PUT',
            headers: {
                'Content-Type': 'Application/json'
            },
            data: JSON.stringify({ application_open: reqData }),

            // response is a boolean (true or false)
            success: function (response) {

                // console.log(response);
                if (response.application_open) {
                    // button to change application window status
                    $('button#showStatus').html('Close Application');
                    $('button#showStatus').removeClass('btn-success').addClass('btn-danger');

                    // button to show application window status
                    $('button#display-status').html('open');
                    $('button#display-status').removeClass('btn-danger').addClass('btn-success');

                    alert('Your company is now open for applicants');
                } else {
                    $('button#showStatus').html('Open Application');
                    $('button#display-status').html('closed');

                    $('button#showStatus').removeClass('btn-danger').addClass('btn-success');
                    $('button#display-status').removeClass('btn-success').addClass('btn-danger');

                    alert('You have now closed the application window to interns');
                }
            }
        });

    });

};

$(document).ready(getCompanyStatus());