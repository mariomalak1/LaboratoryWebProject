const labName = document.getElementById("name");
const bulidNumber = document.getElementById("buildnumber");
const floorNumber = document.getElementById("floornumber");
const pcNumber = document.getElementById("pcnumber");
const chairNumber = document.getElementById("chairnumber");
const active = document.getElementById("active");
const underMaintenance = document.getElementById("underMaintenance");
const addEl = document.getElementById("add");
const reset = document.getElementById("reset");
const loadFromLocalStortage = JSON.parse(localStorage.getItem("Labs"));
const lapTableEL = document.getElementById("lapTable");
let labs = [];
window.onload = function () {
  if (loadFromLocalStortage) {
    labs = loadFromLocalStortage;
    render(labs)
  }
};
addEl.onclick = function () {
  let newlab = {
    labName: labName.value,
    bulidNumber: bulidNumber.value,
    floorNumber: floorNumber.value,
    pcNumber: pcNumber.value,
    chairNumber: chairNumber.value,
  };
  if (active.checked == true) {
    newlab["status"] = "Active";
  } else {
    newlab["status"] = "UnderMaintenance";
  }
  // labs.push(newlab);
  // localStorage.setItem("Labs",JSON.stringify(labs));
  let result = labs.find((item) => item.labName === newlab["labName"]);
  if (result) {
    alert("This lab is already added");
  } else {
    labs.push(newlab);
    localStorage.setItem("Labs", JSON.stringify(labs));
  }
};

reset.onclick = function () {
  labName.value = "";
  bulidNumber.value = "";
  floorNumber.value = "";
  pcNumber.value = "";
  chairNumber.value = "";
  active.checked = false;
  underMaintenance.checked = false;
};
function render(laps) {
  console.log(laps)
  let listItems = "";
  for (let i = 0; i < laps.length; i++) {
    listItems += `
            <tr>
                <td>${i + 1}</td>
                <td>${laps[i]["labName"]}</td>
                <td>${laps[i]["bulidNumber"]}</td>
                <td>${laps[i]["floorNumber"]}</td>
                <td>${laps[i]["pcNumber"]}</td>
                <td>${laps[i]["chairNumber"]}</td>
                <td>${laps[i]["status"]}</td
                <!-- Button to Go to Edit Page, to Edit or Delete This Lab -->
          <td>
            <a href="EditLaboratory.html">
              <button type="button" class="EditButton" name="button">
                Edit
              </button>
            </a>
          </td>

          <!-- Button to go to report page, to Report This Lab -->
          <td>
            <a href="ReportProblem.html">
              <button type="button" class="ReportButton" name="button">
                Report
              </button>
            </a>
          </td>
        </tr>
            </tr>
        `;
  }
  lapTableEL.innerHTML = `
  <thead>
  <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Building No.</th>
      <th>Floor No.</th>
      <th>PCs No.</th>
      <th>Chair No.</th>
      <th>Status</th>
      <th>Delete\Edit</th>
      <th>Report</th>
  </tr>
  </thead>
  <tbody>
    ${listItems} 
  </tbody>

<tfoot>
<tr>
  <td colspan="8">Number Of Laboratories</td>
  <td>${laps.length}</td>
</tr>
</tfoot>
  `;
}
