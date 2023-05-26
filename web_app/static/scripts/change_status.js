
/**
 * changeApplicationStatus - changes the `Action` status column of companies
 * depending on whether their application window is open or closed.
 * 
 * Description - if the Intern already applied or not, and the company has
 * closed its application window, the `button` will display `closed` and it will
 * be disabled
 */
function changeCompanyApplicationStatus() {
    const idArray = [];

    // Iterate through all the company-info buttons
    $('button.company-info').each(function (idx, item) {
        idArray.push($(item).attr('data-button'));
    });
    // console.log(idArray);

    $('button.show-availability').on('click', function () {

        $.each(idArray, function (idx, Id) {
            // console.log(Id);

            $.get({
                url: `http://127.0.0.1:5001/api/v1/companies/${Id}`,
                success: function (response, jqXHR) {
                    const Id = response.id;
                    console.log(Id, response);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        });
    });
}




// $(document).ready(changeCompanyApplicationStatus());