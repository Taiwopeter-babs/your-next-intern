
export const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
/**
 * authIntern - validates that the user provides values to the form fields.
 * It does not validate the correctness of the fields, this is done server-side   
 */
function authLogin() {

    // validate that email follows a pattern
    $('#email').on('input', function () {
        const $email = $(this).val();

        const isEmail = emailRegex.test($email);
        if (isEmail) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });

    $('#password').on('input', function () {
        const $password = $(this).val();

        if ($password) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    })
}

$(document).ready(authLogin());