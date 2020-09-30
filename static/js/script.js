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