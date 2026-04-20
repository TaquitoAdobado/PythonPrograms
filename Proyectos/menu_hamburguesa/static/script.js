const hmbButton = document.querySelector(".hamburguer");
hmbButton.addEventListener("click", button_click);

function button_click() {
    const hmb_lines = document.querySelectorAll(".l1, .l2, .l3");
    hmb_lines.forEach((line) => {
        line.classList.toggle("active");
    });
}