const signinBtn = document.getElementById("signin-btn");
const checkbox = document.getElementById("checkbox");

signinBtn.addEventListener("click", (e) => {
    if (!checkbox.checked) {
        alert("請勾選同意條款");
        e.preventDefault();
    }
});
