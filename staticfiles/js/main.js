document.addEventListener("DOMContentLoaded", function () {
    const date = new Date();
    const yearElement = document.querySelector('.year');
    if (yearElement) {
        yearElement.innerHTML = date.getFullYear();
    }

    let lastScrollY = window.scrollY;
    const topNavbar = document.querySelector(".sticky-top");
    const bottomNavbar = document.querySelector(".fixed-bottom");
    let hideTimeout;
    let isScrollingUp = false;

    if (topNavbar) topNavbar.style.transition = "transform 0.3s ease-in-out";
    if (bottomNavbar) bottomNavbar.style.transition = "transform 0.3s ease-in-out";

    const hideNavbars = () => {
        if (topNavbar) topNavbar.style.transform = "translateY(-100%)";
        if (bottomNavbar) bottomNavbar.style.transform = "translateY(100%)";
    };

    const showNavbars = () => {
        if (topNavbar) topNavbar.style.transform = "translateY(0)";
        if (bottomNavbar) bottomNavbar.style.transform = "translateY(0)";
    };

    window.addEventListener("scroll", () => {
        requestAnimationFrame(() => {
            if (!topNavbar || !bottomNavbar) return;

            // Ensure we don't hide navbars when at the very top
            if (window.scrollY === 0) {
                showNavbars();
                return;
            }

            if (window.scrollY < lastScrollY) {
                // If scrolling up but NOT at the very top, hide navbars
                if (!isScrollingUp) {
                    hideNavbars();
                    isScrollingUp = true;
                }
            } else {
                // If scrolling down, reset scrolling flag
                isScrollingUp = false;
                showNavbars();
            }

            lastScrollY = window.scrollY;

            // Reset inactivity timer
            clearTimeout(hideTimeout);
            hideTimeout = setTimeout(hideNavbars, 3000); // Hide after 3 sec of inactivity
        });
    });

    // Detect user interactions to show navbars
    ["mousemove", "touchstart", "keydown"].forEach(event => {
        window.addEventListener(event, () => {
            showNavbars();
            clearTimeout(hideTimeout);
            hideTimeout = setTimeout(hideNavbars, 3000); // Hide after 3 sec of inactivity
        });
    });

    // Initially start the inactivity timer
    hideTimeout = setTimeout(hideNavbars, 3000);
});
