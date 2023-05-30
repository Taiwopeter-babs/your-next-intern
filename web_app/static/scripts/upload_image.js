
/**
 * Allows a user select and upload a profile image
 */
function imageUpload() {

    $('.upload-button').on('click', function () {

        $('.popup').css("display", "block");
    })
    // submit the form
    $('#submit-file').on('click', function () {
        $('.upload-img').submit();
    })

    // Modal control
    $('button.cancel').on('click', function () {
        $('.popup').fadeOut(300);
    });

    // performs action when user clicks any inner content (children)
    $('.popup').children().on('click', function () {
        return true;
    });


};
$(document).ready(imageUpload());
