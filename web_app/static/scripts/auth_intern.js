
import { emailRegex } from './auth_login.js';
/**
 * authIntern - validates that the user provides values to the form fields.
 * It does not validate the correctness of the fields, this is done server-side   
 */
function authIntern() {

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
    // password
    $('#password1').on('input', function () {
        const $obj = $(this).val();

        if ($obj.length >= 8) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    $('#password2').on('input', function () {
        const $obj = $(this).val();

        if ($obj.length >= 8) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    // first name
    $('#first_name').on('input', function () {
        const $first_name = $(this).val();

        if ($first_name) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    // last name
    $('#last_name').on('input', function () {
        const $last_name = $(this).val();

        if ($last_name) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    // gender
    $('#gender').on('input', function () {
        const $gender = $(this).val();

        if ($gender) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    })
    // birthday
    $('#birthday').on('change', function () {
        const $obj = $(this).val();

        if ($obj) {
            $(this).removeClass('invalid').addClass('valid');
            // console.log($obj, typeof $obj);
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    })
    // phone
    $('#phone').on('input', function () {
        const $obj = $(this).val();

        if ($obj) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    // school
    $('#school').on('input', function () {
        const $obj = $(this).val();
        console.log($obj);

        if ($obj) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
    // course
    $('#course').on('input', function () {
        const $obj = $(this).val();

        if ($obj) {
            $(this).removeClass('invalid').addClass('valid');
        } else {
            $(this).removeClass('valid').addClass('invalid');
        }
    });
}

$(document).ready(authIntern());