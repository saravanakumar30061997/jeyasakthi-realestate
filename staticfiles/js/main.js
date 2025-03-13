document.addEventListener("DOMContentLoaded", function () {
    const date = new Date();
    const yearElement = document.querySelector('.year');
    if (yearElement) {
        yearElement.innerHTML = date.getFullYear();
    }

    let lastScrollY = window.scrollY;
    const topNavbar = document.querySelector(".sticky-top");
    const bottomNavbar = document.querySelector(".fixed-bottom");

    if (topNavbar) topNavbar.style.transition = "transform 0.3s ease-in-out";
    if (bottomNavbar) bottomNavbar.style.transition = "transform 0.3s ease-in-out";

    window.addEventListener("scroll", () => {
        requestAnimationFrame(() => {
            if (!topNavbar || !bottomNavbar) return;

            if (window.scrollY > lastScrollY) {
                // Scrolling Down - Hide Navbars
                topNavbar.style.transform = "translateY(-100%)";
                bottomNavbar.style.transform = "translateY(100%)";
            } else {
                // Scrolling Up - Show Navbars
                topNavbar.style.transform = "translateY(0)";
                bottomNavbar.style.transform = "translateY(0)";
            }
            lastScrollY = window.scrollY;
        });
    });
});
