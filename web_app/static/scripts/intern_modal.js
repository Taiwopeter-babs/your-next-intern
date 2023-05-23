/**
 * toggleInternInfo - retrieves info about an intern and
 * displays it in the modal container
 */
function toggleInternInfo() {

    $('button.intern-info').on('click', function () {
        const $intern_id = $(this).data('button');
        $.get({
            url: `http://127.0.0.1:5001/api/v1/interns/${$intern_id}`,
            success: function (response) {
                const $popupHead = $('.popup h2');
                const $courseItem = $('.course-item');
                const $schoolItem = $('.school-item');
                const $companyNum = $('.company-num');

                const numberOfCompanies = response.companies.length
                const strNum = numberOfCompanies <= 1 ? 'company' : 'companies';

                $popupHead.html(`${response.first_name} ${response.last_name}`);
                $courseItem.html(response.course);
                $schoolItem.html(response.school);
                $companyNum.html(`${numberOfCompanies} ${strNum}`);
            },
            error: function (error) {
                console.log(error);
            }
        })
        $('.popup').fadeIn(300);
    });
    $('button.close-modal').on('click', function () {
        $('.popup').fadeOut(300);
    });
    // Close Popup when Click outside
    $('.popup').on('click', function () {
        $('.popup').fadeOut(300);
    }).children().click(function () {
        return false;
    });

}
$(document).ready(toggleInternInfo());