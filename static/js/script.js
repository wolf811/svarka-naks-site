$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})

// AUTORIZATION
$('#btnRegistration').click(function() {
    $('#formAuthorization').hide();
    $('#formRegistration').show();
    $('#authorizationModalTitle').html('Регистрация')
});
$('#btnCancelRegistration').click(function() {
    $('#formAuthorization').show();
    $('#formRegistration').hide();
    $('#authorizationModalTitle').html('Авторизация')
});
$('#linkForgotPassword').click(function() {
    $('#formForgotPassword').show();
    $('#formAuthorization').hide();
    $('#authorizationModalTitle').html('Восстановление пароля')
})
$('#btnAutorization').click(function() {
    $('#formForgotPassword').hide();
    $('#formAuthorization').show();
    $('#authorizationModalTitle').html('Авторизация')
})
$('#btnConfirmSending').click(function() {
    $('#confirmSending').show()
    $('#formForgotPassword').hide();
})
$('#btnConfirmRegistration').click(function() {
    $('#confirmRegistration').show();
    $('#formRegistration').hide();
})
$('#btnConfirmLogin').click(function() {
    $('#confirmLogin').show();
    $('#formAuthorization').hide();
    $('#iconNotAuthorizedUser').hide();
    $('#iconAuthorizedUser').show();
})
$('#logOff').click(function() {
    $('#iconNotAuthorizedUser').show();
    $('#iconAuthorizedUser').hide();
    $('#confirmLogin').hide();
    $('#formAuthorization').show();
})
// END AUTORIZATION


// Clipping text
$.fn.succinct = function(options) {

    var settings = $.extend({
        size: 240,
        omission: '...',
        ignore: true
    }, options);

    return this.each(function() {

        var textDefault,
            textTruncated,
            elements = $(this),
            regex = /[!-\/:-@\[-`{-~]$/,
            init = function() {
                elements.each(function() {
                    textDefault = $(this).html();

                    if (textDefault.length > settings.size) {
                        textTruncated = $.trim(textDefault)
                            .substring(0, settings.size)
                            .split(' ')
                            .slice(0, -1)
                            .join(' ');

                        if (settings.ignore) {
                            textTruncated = textTruncated.replace(regex, '');
                        }

                        $(this).html(textTruncated + settings.omission);
                    }
                });
            };
        init();
    });
};

$('.truncate').succinct({
    size: 200,
});

// END Clipping text

$('#btnCheckout').click(function() {
    $('#customer').show();
    $('#btnGroupSaveCustomer').show();
    $('#btnGroupCheckout').hide();
})

$('#btnCancelCustomer').click(function() {
    $('#customer').hide();
    $('#btnGroupSaveCustomer').hide();
    $('#btnGroupCheckout').show();
})