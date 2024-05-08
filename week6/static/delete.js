const deleteBtns = document.querySelectorAll(".delete-btn");

deleteBtns.forEach((deleteBtn) => {
    deleteBtn.addEventListener("click", (e) => {
        let deleteMessage = confirm("確定要刪除此訊息嗎？");

        if (!deleteMessage) {
            e.preventDefault();
        }
    });
});
