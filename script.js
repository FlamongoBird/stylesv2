function reloadCSS() {
    var links = document.getElementsByTagName("link");
    for (var link of links) {
        if (link.rel == "stylesheet") {
            link.href += "";
        }
    }
}