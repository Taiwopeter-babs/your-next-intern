/**
 * applyToCompany - retrieves info about an intern and
 * displays it in the modal container
 */
function applyToCompany() {

    $('button.company-info').on('click', function () {
        const $companyId = $(this).data('button');
        const $applyButton = $(this);

        // Retrieve the data of the selected company
        $.get({
            url: `http://127.0.0.1:5001/api/v1/companies/${$companyId}`,
            success: function (response) {
                const $popupHead = $('.popup h2');
                const $expertiseItem = $('.expertise-item');
                const $websiteItem = $('.website-item');
                const $applicantsNum = $('.applicants-num');

                const numberOfInterns = response.interns.length;
                const strNum = numberOfInterns <= 1 ? 'intern' : 'interns';

                $popupHead.html(`${response.name}`);
                $expertiseItem.html(response.specialization);
                $websiteItem.html(response.website);
                $applicantsNum.html(`${numberOfInterns} ${strNum}`);
            },
            error: function (error) {
                console.log(error);
            }
        })
        $('.popup').fadeIn(300);

        // Send Intern data to api to apply to selected company
        applicantsControl($companyId);
    });

    // Modal control section
    $('button.close-modal').on('click', function () {
        $('.popup').fadeOut(300);
    });
    // Close Popup when user clicks outside the modal
    $('.popup').on('click', function () {
        $('.popup').fadeOut(300);
    }).children().click(function () {
        return false;
    });

    changeApplicationStatus();


}
/**
 * applicantsControl - controls the query of the Intern application
 * to the api endpoint.
 */
function applicantsControl(comId) {
    // const $com_id = $('button.company-info').attr('data-button');

    $('button.apply-to').on('click', function () {
        const $intId = $(this).data('button');

        $.post({
            url: `http://127.0.0.1:5001/api/v1/companies/${comId}/interns/${$intId}`,
            success: function (response, textStatus, jqXHR) {
                const statusCode = jqXHR.status;
                console.log(statusCode)
                if (statusCode === 201) {
                    alert('You application is successful!');
                } else if (statusCode === 200) {
                    alert('You already applied to this company')
                }
            },
            error: function (xhr) {
                alert('Error in the response');
                throw new Error('Error in the response');

            }
        })
    });
}


/**
 * changeApplicationStatus - Gets all the companies an intern applied
 * to and changes their `Action` status to `Applied
 */
function changeApplicationStatus() {
    const $allCompanies = $('section.companies').find('button.company-info');
    const $intId = $('button.apply-to').attr('data-button');
    const $modalApplyButton = $('button.apply-to');
    // console.log($('section.companies').find('button.apply-to'));

    $.get({
        url: `http://127.0.0.1:5001/api/v1/interns/${$intId}`,
        success: function (response, jqXHR) {
            const companies = response.companies;

            $.each(companies, function (index, obj) {
                for (let i = 0; i < $allCompanies.length; i++) {
                    if ($allCompanies[i].dataset.button === obj.id) {
                        $allCompanies[i].innerHTML = 'Applied';
                        // console.log($allCompanies[i]);
                    }
                }
            });
        }
    });
    $.each($modalApplyButton, function (index, obj) {
        // console.log(obj);
    })


}

$(document).ready(applyToCompany());