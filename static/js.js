var hamburger = document.querySelector(".hamburger");
var nav = document.querySelector(".navigation-menu");
var links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("open");
    nav.classList.toggle("open");
    links.forEach(link => {
        link.classList.toggle("fade");
    });
});
