// import { modalControl } from "./apply_to_company.js";

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

                const date = new Date(obj.date_applied);

                const article = `<article class="company">

                                    <div><h4>${obj.name}</h4></div>

                                    <div><p>${obj.specialization}</p></div>

                                    <div><p>${obj.website}</p></div>

                                    <div class="com-date-status">

                                        <div>Applied: ${date.toDateString()}</div>
                                        <div class="status"></div>

                                    </div>

                                </article>`
                    ;

                // Append to static parent element
                $companiesList.append(article)
            })
        }
    })

}

$(document).ready(displayCompanies());