$(document).ready(function () {
    activeNavItem();
    stickyNavbar();
    autoCloseNavbar();
});

/**
 * Adds 'active' class to the current page
 */
function activeNavItem() {
    $('nav-item.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
}

/**
 * Adds/removes 'hidden' class from navbar when scrolling
 */
function stickyNavbar() {
    var navbarHeight = $(".navbar").height();
    var lastScrollTop = 0;
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var currentScrollTop = $(this).scrollTop();
        if (scroll >= navbarHeight && currentScrollTop > lastScrollTop) {
            $("nav").addClass('hidden');
        } else {
            $("nav").removeClass('hidden');
        }
        lastScrollTop = currentScrollTop;

    });
}

/**
 * Auto-clicks the navbar button to close it on scroll down for mobiles
 */
function autoCloseNavbar() {
    $(document).scroll(function (event) {
        var clickover = $(event.target);
        var navbarOpen = $(".navbar-collapse").hasClass("collapse show");

        if (navbarOpen == true && !clickover.hasClass("navbar-toggler")) {
            $("button.navbar-toggler").click();
        }
    });
}