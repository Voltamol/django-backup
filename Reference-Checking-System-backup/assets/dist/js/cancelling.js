function strikeout(elemID){
    let element=document.getElementById(elemID)
    let strike=document.createElement("del")
    let para=document.createElement("p")
    para.innerText=elemID
    para.id=elemID
    para.classList.add("text-truncate")
    strike.appendChild(para)
    element.replaceWith(strike)
    para.style.color="gray";
}

function unstrike(elemID){
    let para=document.getElementById(elemID)
    para.style.color="black"
    para.classList.add("text-truncate")
    para.parentElement.replaceWith(para)
}

function registerCheckBoxes(){
    for(let checkbox of document.getElementsByClassName("complete")){
        checkbox.addEventListener("click",e=>{
            if(checkbox.checked){
                strikeout(checkbox.name)
            }else{
                unstrike(checkbox.name)
            }
        })
    }
    
}

registerCheckBoxes()