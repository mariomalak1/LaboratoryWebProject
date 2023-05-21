function makeAjaxRequest(url, method, data) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                searchSuggestion(JSON.parse(xhr.responseText));
            } else {
                errorCallback(xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify(data));
}

function callAjax(search_string){
    makeAjaxRequest("/search_bar_response/?search_string=" + search_string, "get", {"search_string":search_string});
}

// search bar suggestion
let searchBar = document.getElementById("search-bar");
let resultOfSearch = document.getElementById("resultOfSearch");
function searchSuggestion(data){
   
    let res="";
    
    if (data.labs.length == 0 && data.reports.length == 0 || searchBar.value.trim() == ""){
        resultOfSearch.style.display ="none";
    }
  else{

    resultOfSearch.style.display ="block";
    for (let i = 0;i < Math.min(data.labs.length,3);i++){
        // need to write link well
        res += " <a href = \"/edit_lab/" + data.labs[i].id + "\" " + "\" ><div> <h5>" + data.labs[i].name+ "</h5> </div></a>";
        resultOfSearch.innerHTML = res;
    }
    for (let i = 0;i < Math.min(data.reports.length,2);i++){
         // need to write link well
        res += " <a href = \"/edit_report/" + data.reports[i].id + "\" " +  "\" ><div> <h5>" + data.reports[i].description + "</h5> </div></a>";
        resultOfSearch.innerHTML = res;
    }
    }
}




