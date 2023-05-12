// let problems = [];
// const loadLaps = JSON.parse(localStorage.getItem("Labs"));
// const loadFromLocalStortage = JSON.parse(localStorage.getItem("problems"));
window.onload = function () {
    if (loadFromLocalStortage) {
        problems = loadFromLocalStortage;
        indx = loadIndex;
        Laps = loadLaps;
        render(problems);
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