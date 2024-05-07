const signupForm = document.getElementById("signup-form");
const signupInputs = signupForm.getElementsByTagName("input");
const signupBtn = document.getElementById("signup-btn");

signupBtn.addEventListener("click", (e) => {
    let isEmpty = false;

    for (let i = 0; i < signupInputs.length; i++) {
        if (signupInputs[i].value === "") {
            isEmpty = true;
            break;
        }
    }

    if (isEmpty) {
        alert("請填寫完整的姓名、帳號、密碼");
        e.preventDefault();
    }
});

const signinForm = document.getElementById("signin-form");
const signinInputs = signinForm.getElementsByTagName("input");
const signinBtn = document.getElementById("signin-btn");

signinBtn.addEventListener("click", (e) => {
    let isEmpty = false;

    for (let i = 0; i < signinInputs.length; i++) {
        if (signinInputs[i].value === "") {
            isEmpty = true;
            break;
        }
    }

    if (isEmpty) {
        alert("請填寫完整的帳號、密碼");
        e.preventDefault();
    }
});
