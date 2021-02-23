$(document).ready(function () {
    activeNavItem();
});

/**
 * Adds 'active' class to the current page
 */
function activeNavItem() {
    $('nav-item.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
}