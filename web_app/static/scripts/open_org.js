import { applyToCompany } from "./open_org_apply.js";

const url = 'http://127.0.0.1:5001/api/v1/all_companies';

/**
 * displays all the companies registered on the platform.
 * Interns can also `apply` to the company if the application is `open`,
 * otherwise, a `disabled` button is shown
 */
function displayCompanies() {

    const $sectionCompanies = $('section.companies');
    const $intId = $('section.companies').attr('data-intern');

    return $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            // console.log(response, response.length);

            $.each(response, function (index, obj) {

                let buttonInfo = '';
                let applyStatus = '';
                let cancelBtn = '';



                if (obj.application_open) {
                    buttonInfo = `<button type="button" class="btn btn-success" disabled>open</button>`;

                    // check if the intern already applied to the company
                    const res = () => {
                        for (let i = 0; i < obj.interns.length; i++) {
                            if (obj.interns[i].id == $intId) {
                                return true;
                            }
                        }
                        return false;
                    }

                    /**
                     * disable button and set it to `Applied` if true,
                     * otherwise enable button and set to `Apply`
                     */
                    if (res()) {
                        applyStatus = `<button type="button" data-id="${obj.id}" class="apply-to btn btn-success" disabled>Applied</button>`;
                        cancelBtn = `<button type="button" id="btn-cancel" class="btn btn-info">cancel application</button>`
                    } else {
                        applyStatus = `<button type="button" data-id="${obj.id}" class="apply-to btn btn-primary">Apply</button>`;
                        cancelBtn = `<button type="button" id="btn-cancel" class="btn btn-info" disabled>cancel application</button>`
                    }

                } else {
                    buttonInfo = `<button type="button" class="btn btn-danger" disabled>closed</button>`;
                    applyStatus = `<button type="button" class="btn btn-primary" disabled>disabled</button>`;
                    cancelBtn = `<button type="button" id="btn-cancel" class="btn btn-info" disabled>cancel application</button>`;
                }


                const article = `<article>
                                    <div class="org-name">
                                        <div>
                                            <h3>${obj.name}</h3>
                                        </div>
                                        <div>
                                            <p>${obj.specialization}</p>
                                        </div>
                                    </div>

                                    <div class="org-contact">
                                        <div><a href="${obj.website}">${obj.website}</a></div>
                                        <div>${obj.email}</div>
                                        <div>Applicants: &ensp; ${obj.interns.length}</div>
                                    </div>
                                    
                                    <div class="apply-info">
                                        ${buttonInfo}
                                        ${applyStatus}
                                    </div>
                                    <div class="cancel-btn">
                                        ${cancelBtn}
                                    </div>

                                </article >

        <div class="popup">
            <div class="popup-content">
                <div>Application successful</div>
            </div>
        </div>`;

                $sectionCompanies.append(article);
            });
        },
        error: function (error) {
            $('#loading').show();
            setTimeout(() => window.location.replace(`/intern_profile/${$intId}`), 5000);

        },
        beforeSend: function () {
            $('#loading').show();
            setTimeout(() => $('#loading').hide(), 6000)
        },
        complete: function () {
            $('#loading').hide();
        }
    });
}

/**
 * runPage - solves the problem of dynamic rendering and delivery
 * of API results. Awaits the rendering of the companies, then performs
 * other tasks
 */
async function runPage() {
    try {
        const res = await displayCompanies();
        if (res) {
            applyToCompany();
        }
    } catch (error) {
        console.log(error);
    }

}

$(document).ready(function () {
    runPage();

})