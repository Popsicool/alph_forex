function changeSign(a){
    let box = document.getElementById(a);
    let arr = String(box.textContent);
    if (arr.length == 2){
        box.innerHTML = "v";  
    }
    else{
        box.innerHTML = "&lt";  
    }
  
}
