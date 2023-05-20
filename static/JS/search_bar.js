function makeAjaxRequest(url, method, data) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
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