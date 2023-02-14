var e = 0;
function populate() {
    while (true) {
        let windowRelativeBottom = document.documentElement.getBoundingClientRect().bottom;
        if (windowRelativeBottom > document.documentElement.clientHeight + 100) break;

        e += 1;
        console.log(e)
        document.body.insertAdjacentHTML("beforeend", `<img src="rickroll-roll.gif" alt=""><img src="rickroll-roll.gif" alt=""><img src="rickroll-roll.gif" alt=""><img src="rickroll-roll.gif" alt="">`);
    }
}

window.addEventListener('scroll', populate);

populate();
