let problem = {};
let problems = [];
const reportsEL = document.getElementById("reportsTable-el");
const lapIdEL = document.getElementById("lapid-in");
const pcIdEL = document.getElementById("pcid-in");
const sTypeEl = document.getElementById("softwaretype-in");
const hTypeEl = document.getElementById("hardwaretype-in");
const dateEl = document.getElementById("date-in");
const descEl = document.getElementById("desc-in");
const submitBtn = document.getElementById("submit-btn");
const loadLaps = JSON.parse(localStorage.getItem("Labs"));
let Laps = [];
const loadFromLocalStortage = JSON.parse(localStorage.getItem("problems"));
const loadIndex = JSON.parse(localStorage.getItem("indx"));
const editIndx = JSON.parse(localStorage.getItem("LapIndx"));
let indx;
let lapindx = editIndx;
window.onload = function () {
  if (loadFromLocalStortage) {
    problems = loadFromLocalStortage;
    indx = loadIndex;
    Laps = loadLaps;
    renderInReport(lapindx);

  }
};
function render(problems) {
  let listItems = "";
  for (let i = 0; i < problems.length; i++) {
    listItems += `
            <tr>
                <td>${i + 1}</td>
                <td>${problems[i]["lapId"]}</td>
                <td>${problems[i]["pcId"]}</td>
                <td>${problems[i]["problemType"]}</td>
                <td>${problems[i]["description"]}</td>
                <td>${problems[i]["date"]}</td>
                <td>
                  <a href="EditReport.html">
                    <button id="tableEdit-btn"  class="EditButton" name="button" onclick="saveIndx(${i})">
                      Edit
                    </button>
                  </a>
                </td>
            </tr>
        `;
  }
  reportsEL.innerHTML = `
  <thead>
  <tr>
    <th>ID</th>
    <th>Laboratory Name</th>
    <th>PC ID</th>
    <th>Hardware | SoftWare</th>
    <th>Description</th>
    <th>Problem Date</th>
    <th>Delete\Edit</th>
  </tr>
  </thead>
  <tbody>
    ${listItems} 
  </tbody>
  <tfoot>
    <tr>
      <td colspan="6">Number Of Reports</td>
      <td>${problems.length}</td>
    </tr>
  </tfoot>
  `;
}
function renderInReport(lapindx) {
  lapIdEL.value = Laps[lapindx]["labName"];
  lapIdEL.setAttribute("readonly", true)
}
submitBtn.addEventListener("click", function () {
  problem["lapId"] = lapIdEL.value;
  problem["pcId"] = pcIdEL.value;
  if (sTypeEl.checked == true) {
    problem["problemType"] = "Software";
  } else if (hTypeEl.checked == true) {
    problem["problemType"] = "Hardware";
  }
  problem["date"] = dateEl.value;
  problem["description"] = descEl.value;
  problems.push(problem);
  problem = {};
  localStorage.setItem("problems", JSON.stringify(problems));
  alert("Saved");
  render(problems);
});
function saveIndx(index) {
  localStorage.setItem("indx", JSON.stringify(index));

}
