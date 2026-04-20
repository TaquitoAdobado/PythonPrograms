const hmbButton = document.querySelector(".hamburguer");
hmbButton.addEventListener("click", button_click);
hmbButton.addEventListener("click", toggle_menu);

function button_click() {
    const hmb_lines = document.querySelectorAll(".l1, .l2, .l3");
    hmb_lines.forEach((line) => {
        line.classList.toggle("active");
    });
}

function toggle_menu() {
    const hmb_menu = document.querySelector(".offScreenMenu");
    hmb_menu.classList.toggle("active");
}