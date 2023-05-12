let pcid = document.getElementById("pcid");
let underMaintenance = document.getElementById("underMaintenance");
let active = document.getElementById("active");
let button = document.getElementById("button");
let localStoragelap = JSON.parse(localStorage.getItem("Labs"));
let localStoragepc = JSON.parse(localStorage.getItem("pc"));
let lapid = document.getElementById("lapid");
let pcs = [];
let laps=[];



window.onload=function(){
    if(localStoragepc && localStoragelap )
    pcs=localStoragepc;
    laps=localStoragelap;




}



button.addEventListener("click", function ()

 {   
    
    
    for (i = 1; i <= localStoragelap.length; i++) {
         
        
        let flag=false;

        if (lapid.value == (i))
        {

            addpc()
            flag=true;


        }


            
            

        
    }

    if(flag===false)
    {
          window.alert("chcek Lap Id");

    }

})





function addpc() {


  

    var newpc = {

        pcid: pcid.value,
        lapid: lapid.value,


    }
    if (active.checked == true) {
        newpc["status"] = "Active";
    } else {
        newpc["status"] = "UnderMaintenance";
    }


    pcs.push(newpc);
    localStorage.setItem("pc", JSON.stringify(pcs));

    



   
}
 







