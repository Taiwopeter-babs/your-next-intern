
/**
 * applyToCompany - enables the intern to apply to a company.
 * If the intern already applied to the company, a `You already applied`
 * message is shown, otherwise, an `Application successful` message is displayed  
 */
export default function applyToCompany() {

    $('div.apply-info button.apply-to').on('click', function () {
        const $comId = $(this).attr('data-id');
        const $intId = $('section.companies').attr('data-intern');

        // Retrieve the data of the selected company
        $.ajax({
            url: `http://127.0.0.1:5001/api/v1/companies/${$comId}/interns/${$intId}`,
            type: 'POST',
            success: function (response, textStatus, jqXHR) {

                const statusCode = jqXHR.status;
                if (statusCode === 200) {
                    $('div.popup-content div').html('You already applied to this company');
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
        })

        // Shows a popup after the click and fades out after 2 seconds
        $('.popup').fadeIn(300);
        const timeOut = setTimeout(() => {
            $('.popup').fadeOut(300)
        }, 2000);
        // location.reload();
    });

    // Close Popup when user clicks outside the modal
    $('.popup').on('click', function () {
        $('.popup').fadeOut(300);
    }).children().click(function () {
        return false;
    });

};
