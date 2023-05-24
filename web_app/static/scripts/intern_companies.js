/**
 * displayCompanies - sends a GET request to an api endpoint with
 * the intern_id, and return the list of companies
 */
function displayCompanies() {

    const $internId = $('section.intern-detail').attr('data-id');
    const $companiesList = $('section.companies-list');
    // console.log($companiesList);

    $.get({
        url: `http://127.0.0.1:5001/api/v1/interns/${$internId}/companies`,
        success: function (response) {


            $.each(response, function (index, obj) {


                const $article = $('<article>', { class: 'company' });

                // company name
                const $divName = $('<div>');
                const $h4 = $('<h4>');

                // company specialty
                const $divSpecial = $('<div>');
                const $pSpecial = $('<p>');

                // company website
                const $divWeb = $('<div>');
                const $pWeb = $('<p>');

                // date intern applied
                const $divDateStatus = $('<div>', { class: 'com-date-status' });
                const $divDate = $('<div>');
                const $divStatus = $('<div>', { class: 'status' });

                // Company Name
                $divName.append($h4.text(obj.name));
                $divName.appendTo($article);

                // Company specialty
                $divSpecial.append($pSpecial.text(obj.specialization));
                $divSpecial.appendTo($article);

                // Company website
                $divWeb.append($pWeb.html(`${obj.website}`));
                $article.append($divWeb);

                // Intern date of application to the company
                const date = new Date(obj.date_applied);
                // console.log(date.toDateString())
                $divDate.html(`Applied: ${date.toDateString()}`).appendTo($divDateStatus);
                $divStatus.appendTo($divDateStatus);

                $article.append($divDateStatus);

                console.log($article.innerHTML);

                // Append to static parent element
                $companiesList.append($article)
            })
        }
    })

}

$(document).ready(displayCompanies());