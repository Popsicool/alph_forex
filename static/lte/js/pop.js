function changeSign(){
    let box = document.getElementById("arr1");
    let arr = String(box.textContent);
    if (arr.length == 2){
        box.innerHTML = "v";  
    }
    else{
        box.innerHTML = "&lt";  
    }
  
}
    