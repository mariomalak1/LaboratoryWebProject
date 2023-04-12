let problems = [];
const loadFromLocalStortage = JSON.parse(localStorage.getItem("problems"));
const loadIndex = JSON.parse(localStorage.getItem("indx"));
const newLapIdEL = document.getElementById("newLapId-in");
const newPcIdEL = document.getElementById("newPcId-in");
const newSTypeEl = document.getElementById("newS-in");
const newHTypeEl = document.getElementById("newH-in");
const newDateEl = document.getElementById("newDate-in");
const newDescEl = document.getElementById("newDesc-in");
const editSubmitBtn = document.getElementById("editSubmit-btn");
const deleteBtn = document.getElementById("delete-btn");
let sC = "";
let hC = "";
let indx;
window.onload = function () {
    if (loadFromLocalStortage) {
        problems = loadFromLocalStortage;
        indx = loadIndex;
        renderOld(problems);
    }
}
function renderOld(problems) {

    if (problems[indx]["problemType"] === "Software") {
        newSTypeEl.checked = true;
    } else if (problems[indx]["problemType"] === "Hardware") {
        newHTypeEl.checked = true;
    }
    newLapIdEL.value = problems[indx]["lapId"];
    newPcIdEL.value = problems[indx]["pcId"];
    newDateEl.value = problems[indx]["date"];
    newDescEl.value = problems[indx]["description"];
}

editSubmitBtn.addEventListener("click", function () {
    problems[indx]["lapId"] = newLapIdEL.value;
    problems[indx]["pcId"] = newPcIdEL.value;
    if (newSTypeEl.checked == true) {
        problems[indx]["problemType"] = "Software";
    } else if (newHTypeEl.checked == true) {
        problems[indx]["problemType"] = "Hardware";
    }
    problems[indx]["date"] = newDateEl.value;
    problems[indx]["description"] = newDescEl.value;
    localStorage.setItem("problems", JSON.stringify(problems));
    renderOld(problems);
})
deleteBtn.addEventListener("click", function () {
    if (window.confirm("Are You Sure You Want to Delete This Report")) {
        problems.splice(indx, 1);
        localStorage.setItem("problems", JSON.stringify(problems));
        //window.location.replace('../AllProjects.html');
    }
})