document.getElementById("navbar-toggle").addEventListener("click", function() {
    var dropdownMenu = document.getElementById("dropdown-menu");
    if (dropdownMenu.style.display === "block") {
        dropdownMenu.style.display = "none";
    } else {
        dropdownMenu.style.display = "block";
    }
});

window.addEventListener("resize", function() {
    var width = window.innerWidth;
    var dropdownMenu = document.getElementById("dropdown-menu");
    if (width > 768) {
        dropdownMenu.style.display = "none";
    }
});
