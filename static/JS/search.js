let r = [];
let laps = [];
const searchList = document.getElementById("search-list");
const loadReports = JSON.parse(localStorage.getItem("problems"));
const loadlaps = JSON.parse(localStorage.getItem("Labs"));
const searchBar = document.getElementById("search-bar");
const itemlists = document.querySelectorAll(".items")
const name = document.getElementsByTagName("h4")
r = loadReports;
laps = loadlaps;
renderList(r, laps);
searchBar.addEventListener("focus", function () {
    searchList.style.display = "block";
})
searchBar.addEventListener("focusout", function () {
    searchList.style.display = "none";
})
function renderList(r, laps) {
    let items = "";
    for (let i = 0; i < r.length; i++) {
        items += `
            <div id="item" class="items">
                <h4>${r[i]["lapId"]} ==> Report</h4>
            </div>
        `
    }
    for (let i = 0; i < laps.length; i++) {
        items += `
            <div id="item" class="items">
                <h4>${laps[i]["labName"]} ==> Lap</h4>
            </div>
        `
    }
    searchList.innerHTML = items;
}
searchBar.addEventListener("keyup", function () {
    let itemlists = document.querySelectorAll(".items")
    let name = document.getElementsByTagName("h4")
    let searchBAR = document.querySelector(".searchbar").value.toUpperCase();
    let searchList = document.getElementById("search-list");
    for (let i = 0; i < name.length; i++) {
        if (name[i].innerHTML.toUpperCase().indexOf(searchBAR) >= 0) {
            itemlists[i].style.display = "";
        } else {
            itemlists[i].style.display = "none";
        }
    }
})


