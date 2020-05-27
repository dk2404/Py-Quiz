
function mainHeader(){
    let headers=document.getElementsByClassName("header");
            
    headers[0].style.fontWeight="bold";
    headers[0].style.textAlign="center";

    for(let h in headers) {
        headers[h].style.background="orange";
        headers[h].style.padding="20px";
        headers[h].style.marginLeft="50px";
        headers[h].style.marginRight="50px";
    }
}



function headerStyle(){
    let head=document.getElementsByClassName("header1");

    head[0].style.fontWeight="bold";
    head[0].style.marginLeft="50px"
    
}

function openNav() {
    document.getElementById("nav").style.width = "250px";
    document.getElementById("nav").style.backgroundImage="url('nav2.jpg')";
  }
  
  function closeNav() {
    document.getElementById("nav").style.width = "0";
  }

  var target = document.querySelector('.H1');
 
  function selection(elem) {
    var elem   = document.querySelector(elem);
    var select = window.getSelection();
    var range  = document.createRange();
   
    range.selectNodeContents(elem);
    select.addRange(range);
  }

  target.onclick = function() {
    selection('.H1');
  };


  function para(){
    let paras = document.getElementsByClassName("para");


    for (let p in paras){
        paras[p].style.fontStyle="Helvetica Neue";
        paras[p].style.fontSize = "120%";
        paras[p].style.marginLeft="50px";  
        paras[p].style.marginRight="100px";

    }
}

