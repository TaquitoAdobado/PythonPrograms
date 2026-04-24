const hmbButton = document.querySelector(".hamburguer");
hmbButton.addEventListener("click", button_click);
hmbButton.addEventListener("click", toggle_menu);
hmbButton.addEventListener("click", toggle_hmbMenu);

function button_click() {
    const hmb_lines = document.querySelectorAll(".l1, .l2, .l3");
    hmb_lines.forEach((line) => {
        line.classList.toggle("active");
    });
}

function toggle_menu() {
    const offMenu = document.querySelector(".offScreenMenu");
    offMenu.classList.toggle("active");
}

function toggle_hmbMenu() {
    const hmbMenu = document.querySelector(".hamburguerMenu");
    hmbMenu.classList.toggle("active");
}