frappe.ready(() => {
    if (window.location.pathname.includes("login")) {

        // Add animation
        document.querySelector(".card")?.classList.add("animate__animated", "animate__fadeInUp");

        // Auto-focus email
        setTimeout(() => {
            document.querySelector('input[type="text"], input[type="email"]')?.focus();
        }, 300);
    }
});
