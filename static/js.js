
var nav = document.querySelector(".navigation-menu");
var links = document.querySelectorAll(".nav-links li");
var give_btn = document.querySelector(".give-btn");
nav.addEventListener("click", () => {
    nav.classList.toggle("open");
    give_btn.classList.toggle("hide");
    links.forEach(link => {
        link.classList.toggle("fade");
    });
});
