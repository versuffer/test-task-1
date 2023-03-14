function make_visible() {
    success_button = document.querySelector("button");
    success_button.onclick = () => {
        document.querySelector(".alert").style.visibility = "visible";
        alert('Success!')
    }
}