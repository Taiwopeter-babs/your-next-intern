
/**
 * applyToCompany - enables the intern to apply to a company, and
 * to cancel application
 */
export function applyToCompany() {

    const $intId = $('section.companies').attr('data-intern');

    // POST REQUESTS
    $('div.apply-info button.apply-to').on('click', async function () {
        const $comId = $(this).attr('data-id');


        // Retrieve the data of the selected company
        const result = await $.ajax({
            url: `http://127.0.0.1:5001/api/v1/companies/${$comId}/interns/${$intId}`,
            type: 'POST',
            success: function (response, textStatus, jqXHR) {
                console.log(response)

                const statusCode = jqXHR.status;
                if (statusCode === 201) {
                    // $('div.popup-content div').html('You already applied to this company');
                    // location.replace(`/intern_profile/${$intId}`);
                }
            },
            error: function (error, jqXHR) {
                // console.log(jqXHR, error.status);
                alert(`${error.status}: Error in the request`);

            },
            beforeSend: function () {
                $('#loading').show();
            },
            complete: function () {
                $('#loading').hide();
            }
        });

        // Shows a popup after the click and fades out after 2 seconds
        $('.popup').fadeIn(300);
        const timeOut = setTimeout(() => {
            $('.popup').fadeOut(300)
        }, 2000);
        // location.reload();

        return result;
    });

    // DELETE REQUESTS
    $('div.cancel-btn button#btn-cancel').on('click', async function () {

        const comId = $('div.apply-info button.apply-to').attr('data-id');


        // Retrieve the data of the selected company
        const result = await $.ajax({
            url: `http://127.0.0.1:5001/api/v1/companies/${comId}/interns/${$intId}`,
            type: 'DELETE',
            success: function (response, textStatus, jqXHR) {
                console.log(response);

                const statusCode = jqXHR.status;
                if (statusCode === 200) {
                    $('div.popup-content div').html('You have cancelled your application');
                }
            },
            error: function (error, jqXHR) {
                // console.log(jqXHR, error.status);
                alert(`${error.status}: Error in the request`);
                // location.reload()
            },
            beforeSend: function () {
                $('#loading').show();
            },
            complete: function () {
                $('#loading').hide();
            }
        });

        // Shows a popup after the click and fades out after 2 seconds
        $('.popup').fadeIn(300);
        const timeOut = setTimeout(() => {
            $('.popup').fadeOut(300)
        }, 2000);
        // location.reload();

        return result;
    });

    // Close Popup when user clicks outside the modal
    $('.popup').on('click', function () {
        $('.popup').fadeOut(300);
    }).children().click(function () {
        return false;
    });

};
