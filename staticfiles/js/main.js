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

    const isMobile = () => window.innerWidth <= 768; // Mobile check

    // Function to hide navbars
    const hideNavbars = () => {
        if (isMobile() && topNavbar) {
            topNavbar.style.transform = "translateY(-100%)";
        }
    };

    // Function to show navbars
    const showNavbars = () => {
        if (isMobile() && topNavbar) {
            topNavbar.style.transform = "translateY(0)";
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

    // Show navbar on user interaction
    ["mousemove", "touchstart", "keydown"].forEach(event => {
        window.addEventListener(event, () => {
            if (isMobile()) {
                showNavbars();
                clearTimeout(hideTimeout);
                hideTimeout = setTimeout(hideNavbars, 3000);
            }
        });
    });

    if (isMobile()) {
        hideTimeout = setTimeout(hideNavbars, 3000);
    }
});
