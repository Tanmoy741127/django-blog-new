const select = (el, all = false) => {
    el = el.trim();
    if (all) {
        return [...document.querySelectorAll(el)];
    } else {
        return document.querySelector(el);
    }
};

/**
 * Easy event listener function
 */
const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
        if (all) {
            selectEl.forEach((e) => e.addEventListener(type, listener));
        } else {
            selectEl.addEventListener(type, listener);
        }
    }
};

/**
 * Easy on scroll event listener
 */
const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
};

/**
 * Toggle .header-scrolled class to #header when page is scrolled
 */


const navSlide = () => {
    const burger = document.querySelector(".burger");
    const burgerIcon = document.querySelector(".fa-bars");
    const timesIcon = document.querySelector(".fa-times");
    const nav = document.querySelector(".main-nav-list");
    const backdrop = document.querySelector(".backdrop");
    const navLinks = document.querySelectorAll("main-nav-link");
    //Toggle Navb
    burger.addEventListener("click", () => {
        nav.classList.toggle("nav-active");
        burgerIcon.classList.toggle("hidden");
        timesIcon.classList.toggle("hidden");
        backdrop.classList.toggle("hidden");
    });

    //Animate links
    navLinks.forEach((link, index) => {
        link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s`;
    });
};

navSlide();


const modalOperation = () => {
    const signupbtn = document.getElementById("signup");
    const loginbtn = document.getElementById("login");
    const signupModal = document.getElementById("signup-modal");
    const loginModal = document.getElementById("login-modal");
    const closeSignup = document.getElementById("close-signup");
    const closeLogin = document.getElementById("close-login");

    signupbtn.addEventListener("click", () => {
        signupModal.classList.toggle("hidden");
    });

    loginbtn.addEventListener("click", () => {
        loginModal.classList.toggle("hidden");
    });

    closeSignup.addEventListener("click", () => {
        signupModal.classList.add("hidden");
    });

    closeLogin.addEventListener("click", () => {
        loginModal.classList.add("hidden");
    });

}

modalOperation();




const alertOperation = () => {
    const alert = document.querySelector(".alert");
    const closeAlert = document.getElementById("close-alert");

    closeAlert.addEventListener("click", () => {
        alert.classList.add("hidden");
    });
}

alertOperation();