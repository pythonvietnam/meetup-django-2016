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
    // $('#id_attachment').replaceWith(function () {
    //     return $(
    //         '<a class=\'btn btn-primary\' href=\'javascript:;\' style="margin-top: 12px;">' +
    //         'Choose File...' +
    //         '<input type="file" style=\'position:absolute;z-index:2;top:0;left:0;filter: alpha(opacity=0);-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";opacity:0;background-color:transparent;color:transparent;width: 140px !important;\' name="file_source" size="40"  onchange=\'$("#upload-file-info").html($(this).val());\'>' +
    //         '</a>' + '&nbsp;' +
    //         '<span class=\'label label-info\' id="upload-file-info"></span>', {
    //         html: $(this).html()
    //     });
    // });
    $('label').addClass('col-md-3 control-label');
    $('input').addClass('form-control');
    $('#id_captcha_1').removeClass('form-control')
});



