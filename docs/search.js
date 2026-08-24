/* Site search: filters search-index.json as you type. */
(function () {
    var input = document.getElementById("site-search");
    if (!input) return;
    var results = document.getElementById("search-results");
    var index = null;
    var base = window.SITE_BASE || "";

    fetch(base + "search-index.json")
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (data) { index = data; })
        .catch(function () { input.hidden = true; });

    function matches(article, tokens) {
        var hay = (article.title + " " + article.keywords + " " +
                   article.date + " " + article.elevator_pitch).toLowerCase();
        return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
    }

    function render() {
        var q = input.value.trim();
        if (!q || !index) { results.hidden = true; return; }
        var tokens = q.toLowerCase().split(/\s+/);
        var hits = [];
        for (var i = 0; i < index.length && hits.length < 8; i++) {
            if (matches(index[i], tokens)) hits.push(index[i]);
        }
        if (!hits.length) {
            results.innerHTML = '<div class="search-empty">No results for "' +
                q.replace(/"/g, "&quot;") + '"</div>';
        } else {
            results.innerHTML = hits.map(function (a) {
                return '<a href="' + base + a.url + '">' + a.title +
                    '<span class="search-date">' + a.date + "</span></a>";
            }).join("");
        }
        results.hidden = false;
    }

    var timer = null;
    input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(render, 150);
    });
    input.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            var first = results.querySelector("a");
            if (first) { window.location.href = first.getAttribute("href"); }
        } else if (e.key === "Escape") {
            results.hidden = true;
            input.blur();
        }
    });
    document.addEventListener("click", function (e) {
        if (!e.target.closest(".nav-search")) results.hidden = true;
    });
})();
