const menuItems = document.getElementById("menu-items");
const openIcon = document.getElementById("open-icon");
const closeIcon = document.getElementById("close-icon");

openIcon.addEventListener("click", () => {
    menuItems.style.right = "0";
});

closeIcon.addEventListener("click", () => {
    menuItems.style.right = "-50vw";
});
