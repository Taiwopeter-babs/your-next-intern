
import applyToCompany from './open_org_apply.js';


const url = 'http://127.0.0.1:5001/api/v1/all_companies';

/**
 * displays all the companies registered on the platform.
 * Interns can also `apply` to the company if the application is `open`,
 * otherwise, a `disabled` button is shown
 */
async function displayCompanies() {

    const $sectionCompanies = $('section.companies');

    return $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            // console.log(response);

            $.each(response, function (index, obj) {

                let buttonInfo = '';
                let applyStatus = '';

                if (obj.application_open) {
                    buttonInfo = `<button type="button" class="btn btn-success" disabled>open</button>`;
                    applyStatus = `<button type="button" data-id="${obj.id}" class="apply-to btn btn-primary">Apply</button>`;
                } else {
                    buttonInfo = `<button type="button" class="btn btn-danger" disabled>closed</button>`;
                    applyStatus = `<button type="button" class="btn btn-primary" disabled>disabled</button>`;
                }

                let article = `<article>`;
                article += `<div class="org-name">`;

                article += `<div>
                                <h3>${obj.name}</h3>
                            </div>`;
                article += `<div>
                                <p>${obj.specialization}</p>
                            </div></div>`;
                article += `<div class="org-contact">
                                <div><a href="${obj.website}">${obj.website}</a></div>
                                <div>${obj.email}</div>
                                <div>Applicants: &ensp; ${obj.interns.length}</div>
                            </div>`;
                article += `<div class="apply-info">
                                ${buttonInfo}
                                ${applyStatus}
                            </div></article>`;
                article += `<div class="popup">
                                <div class="popup-content">
                                    
                                    <div>Application successful</div>                                 

                                </div>
                            </div>`

                $sectionCompanies.append(article);
            })
        },
        error: function (error) {
            console.log(`A ${error} occured!`);
        },
        beforeSend: function () {
            $('#loading').show();
        },
        complete: function () {
            $('#loading').hide();


        }
    });
}

/**
 * runPage - solves the problem of dynamic rendering and delivery
 * of API results
 */
async function runPage() {
    try {
        const res = await displayCompanies();
        if (res) {
            applyToCompany();
        }
    } catch (error) {
        alert(error)
    }

}

$(document).ready(function () {
    runPage();

});