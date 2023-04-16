const editIndx = JSON.parse(localStorage.getItem("LapIndx"));
const loadLaps = JSON.parse(localStorage.getItem("Labs"));
const newLapIdEl = document.getElementById("nweLapId-in");
const newBuildNoEl = document.getElementById("newBuildNo-in");
const newFloorNoEl = document.getElementById("newFloorNo-in");
const newPcNoEl = document.getElementById("newPcNo-in");
const newChairNoEl = document.getElementById("newChairNo-in");
const newAS = document.getElementById("newActive-radio");
const newUMS = document.getElementById("newUM-radio");
const editLapBtn = document.getElementById("editLap-Btn");
const deleteLapBtn = document.getElementById("deleteLap-Btn");
let problems = [];
const loadFromLocalStortage = JSON.parse(localStorage.getItem("problems"));
let Laps = [];
let indx;
// on window load 
window.onload = function () {
    if (loadLaps) {
        problems = loadFromLocalStortage;
        Laps = loadLaps;
        indx = editIndx;
        renderOld(Laps);
    }
}
function renderOld(Laps) {
    if (Laps[indx]["status"] == "Active") {
        newAS.checked = true;
    } else if (Laps[indx]["status"] == "UnderMaintenance") {
        newUMS.checked = true;
    }
    newLapIdEl.value = Laps[indx]["labName"];
    newBuildNoEl.value = Laps[indx]["bulidNumber"];
    newChairNoEl.value = Laps[indx]["chairNumber"];
    newFloorNoEl.value = Laps[indx]["floorNumber"];
    newPcNoEl.value = Laps[indx]["pcNumber"];
    newLapIdEl.setAttribute("readonly", true);
}
editLapBtn.addEventListener("click", function () {
    if (newAS.checked == true) {
        Laps[indx]["status"] = "Active";
    } else if (newUMS.checked == true) {
        Laps[indx]["status"] = "UnderMaintenance"
    }
    Laps[indx]["labName"] = newLapIdEl.value;
    Laps[indx]["bulidNumber"] = newBuildNoEl.value;
    Laps[indx]["chairNumber"] = newChairNoEl.value;
    Laps[indx]["floorNumber"] = newFloorNoEl.value;
    Laps[indx]["pcNumber"] = newPcNoEl.value;
    localStorage.setItem("Labs", JSON.stringify(Laps));
    renderOld(Laps);
})
deleteLapBtn.addEventListener("click", function () {
    if (window.confirm("Are You Sure You Want to Delete This Report")) {
        Laps.splice(indx, 1);
        localStorage.setItem("Labs", JSON.stringify(Laps));
        for (let i = 0; i < problems.length; i++) {
            if (problems[i]["lapId"] == newLapIdEl.value) {
                problems.splice(i, 1);
                localStorage.setItem("problems", JSON.stringify(problems));
            }
        }
        newLapIdEl.value = "";
        newBuildNoEl.value = "";
        newChairNoEl.value = "";
        newFloorNoEl.value = "";
        newPcNoEl.value = "";
        newAS.checked = false;
        newUMS.checked = false;

        //window.location.replace('../AllProjects.html');
    }
})