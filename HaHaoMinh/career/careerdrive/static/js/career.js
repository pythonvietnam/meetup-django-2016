jQuery(document).ready(function ($) {
    $('#id_gender').replaceWith(function () {
        return $(
            '<select name="gender" class="form-control" title="">' +
            '<option value="None selected">Select below</option>' +
            '<option value="Male">Male</option>' +
            '<option value="Female">Female</option>' +
            '<option value="Other">Other</option>' +
            '</select>', {
            html: $(this).html()
        });
    });
    $('label').addClass('col-md-3 control-label');
    $('input').addClass('form-control');
    $('#id_captcha_1').removeClass('form-control');
    $('#id_attachment').removeClass('form-control');
});



