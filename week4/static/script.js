const signinBtn = document.getElementById("signin-btn");
const checkbox = document.getElementById("checkbox");

signinBtn.addEventListener("click", (e) => {
    if (!checkbox.checked) {
        alert("請勾選同意條款");
        e.preventDefault();
    }
});

const calculatorForm = document.getElementById("calculator-form");
const numberInput = document.getElementById("number");
const calculatorBtn = document.getElementById("calculator-btn");

calculatorBtn.addEventListener("click", (e) => {
    e.preventDefault();

    let number = parseFloat(numberInput.value);

    if (isNaN(number) || number <= 0) {
        alert("Please enter a positive number.");
    } else {
        window.location.href = `http://127.0.0.1:8000/square/${number}`;
    }
});
