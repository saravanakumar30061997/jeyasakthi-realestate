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

    // Apply transition only if navbar exists
    if (topNavbar) topNavbar.style.transition = "transform 0.3s ease-in-out";
    if (bottomNavbar) bottomNavbar.style.transition = "transform 0.3s ease-in-out";

    const isMobile = () => window.innerWidth <= 768; // Mobile screen check

    const hideNavbars = () => {
        if (isMobile()) {
            if (topNavbar) topNavbar.classList.add("hide");
            if (topBar) topBar.classList.add("hide");
        }
    };
    
    const showNavbars = () => {
        if (isMobile()) {
            if (topNavbar) topNavbar.classList.remove("hide");
            if (topBar) topBar.classList.remove("hide");
        }
    };
    

    window.addEventListener("scroll", () => {
        requestAnimationFrame(() => {
            if (!topNavbar || !bottomNavbar || !isMobile()) return; // Stop execution if not mobile

            if (window.scrollY === 0) {
                showNavbars(); // Always show at the top of the page
                return;
            }

            if (window.scrollY < lastScrollY) {
                if (!isScrollingUp) {
                    hideNavbars();
                    isScrollingUp = true;
                }
            } else {
                isScrollingUp = false;
                showNavbars();
            }

            lastScrollY = window.scrollY;

            clearTimeout(hideTimeout);
            hideTimeout = setTimeout(hideNavbars, 3000); // Hide after 3 sec of inactivity
        });
    });

    // Detect user interactions to show navbars
    ["mousemove", "touchstart", "keydown"].forEach(event => {
        window.addEventListener(event, () => {
            if (isMobile()) {
                showNavbars();
                clearTimeout(hideTimeout);
                hideTimeout = setTimeout(hideNavbars, 3000); // Hide after 3 sec of inactivity
            }
        });
    });

    // Initially start the inactivity timer (only on mobile)
    if (isMobile()) {
        hideTimeout = setTimeout(hideNavbars, 3000);
    }
});
