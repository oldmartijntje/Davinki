document.getElementById("button").addEventListener("click", myFunction);

function myFunction() {
    document.getElementById('demo').innerHTML = Date();
    var imgs = document.getElementsByClassName('e');
    for (var i = 0; i < imgs.length; i++) {
        imgs[i].src = "rickroll-roll.gif";
    }
}
