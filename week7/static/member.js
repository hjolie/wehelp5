const queryBtn = document.getElementById("query-btn");
const queryResult = document.getElementById("query-result");

queryBtn.addEventListener("click", (e) => {
    e.preventDefault();

    const query = document.getElementById("query").value;

    if (query === "") {
    } else {
        fetch(`http://127.0.0.1:8000/api/member?username=${query}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.data !== null) {
                    queryResult.innerHTML = `<p>${data.data.name} (${data.data.username})</p>`;
                } else {
                    queryResult.innerHTML = "<p>查無此會員</p>";
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }
});

const updateBtn = document.getElementById("update-btn");
const updateResult = document.getElementById("update-result");
const welcomeMessage1 = document.getElementById("welcome-msg-1");
const welcomeMessage2 = document.getElementById("welcome-msg-2");

welcomeMessage2.style.display = "none";

updateBtn.addEventListener("click", (e) => {
    e.preventDefault();

    const updatedName = document.getElementById("update").value;

    if (updatedName === "") {
    } else {
        fetch("http://127.0.0.1:8000/api/member", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name: `${updatedName}` }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.ok) {
                    updateResult.innerHTML = "<p>更新成功</p>";
                    welcomeMessage1.style.display = "none";
                    welcomeMessage2.innerText = `${updatedName}，歡迎登入系統`;
                    welcomeMessage2.style.display = "block";
                }
                if (data.error) {
                    updateResult.innerHTML = "<p>更新失敗</p>";
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }
});

const deleteBtns = document.querySelectorAll(".delete-btn");

deleteBtns.forEach((deleteBtn) => {
    deleteBtn.addEventListener("click", (e) => {
        let deleteMessage = confirm("確定要刪除此訊息嗎？");

        if (!deleteMessage) {
            e.preventDefault();
        }
    });
});
