/**
 * Created by jagannath on 19-03-2025.
 */
$(document).ready(function () {
    $("#login").click(function () {
        verifyLoginDetails()
    })
});

function generateCAPTCHA() {
    var $captchaText = $('#captchaText');
    var charsArray = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lengthOtp = 6;
    var captcha = [];

    for (var i = 0; i < lengthOtp; i++) {
        var index = Math.floor(Math.random() * charsArray.length);
        captcha.push(charsArray[index]);
    }

    var captchaString = captcha.join("");
    $captchaText.html(captchaString);  // Display the generated CAPTCHA using jQuery
}

function verifyLoginDetails() {
    var userName = $("#email_contact").val();
    var password = $("#password").val();
    var captcha_input = $("#captcha_input").val();
    var captchaText = $("#hiddenCaptchaText").val();

    if (userName === '' || userName === undefined) {
        swal("Please Enter User Name");
        return false;
    } else if (password === '' || password === undefined) {
        swal("Please Enter Password");
        return false;
    } else if (captcha_input === '' || captcha_input === undefined) {
        swal("Please enter captcha");
        return false;
    } else if (captchaText !== captcha_input) {
        swal("Please enter valid captcha");
        generateCAPTCHA();
        return false;
    } else if (!checkuser(userName, password)) {
        generateCAPTCHA();
        return false;
    } else {
    }
}

function checkuser(username, password) {
    var UserDetails = {
        "username": username,
        "password": password
    };
    $.ajax({
        type: "POST",
        url: "/login_with_username/",
        data: {'UserDetails': JSON.stringify(UserDetails)},
        async: false,
        success: function (data) {
            if (data.result === "valid") {
                setTimeout(function () {
                    gotoRespectiveLogin(data.u_id);
                }, 20);
            } else{
               swal("Oops!", data.msg, "error");
                generateCAPTCHA();
            }
        },
        error: function (error) {
            swal("Please check your internet connection and try again.");
        }
    });

}

function gotoRespectiveLogin(u_id) {
    window.location.href = '/manager-dashboard/';
}