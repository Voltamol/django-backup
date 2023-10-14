//<li class="toDoItem">
      //<input type="checkbox" name="proposal" class="complete">
      //<p id="proposal" class="text-truncate">proposal</p>
      //<img src="md-trash.svg" class="icon delete">
      //</li>
      let toDoList=""
      let trash=""
      function addItem(itemName,listID){
        //creation
        let item=document.createElement("li")
        item.classList.add("toDoItem")
        item.classList.add("horizontal-start")
        let img=document.createElement("img")
        img.classList.add("icon")
        if(listID=="todo"){
          let checkbox=document.createElement("input")
          checkbox.type="checkbox"
          checkbox.name=itemName
          checkbox.classList.add("complete")
          item.appendChild(checkbox)
          img.src="assets/SVGs/md-trash.svg"
          img.classList.add("delete")
          img.addEventListener("click",e=>{
            let txt=e.target.parentElement.innerText
            e.target.parentElement.replaceWith("")
            addItem(txt,"trash")
        })
        }else{
          img.src="assets/dist/SVGs/md-restore.svg"
          img.classList.add("restore")
          img.addEventListener("click",e=>{
            let txt=e.target.parentElement.innerText
            e.target.parentElement.replaceWith("")
            addItem(txt,"todo")
        })
        }
        if(toDoList==""){
          toDoList=document.getElementById(listID);
        }else{
          if(toDoList.id!=listID){
            toDoList=document.getElementById(listID);
          }
        }

        let p=document.createElement("p")
        p.id=itemName
        p.innerText=itemName
        p.classList.add("text-truncate")
        
        //insertion
        item.appendChild(p)
        item.appendChild(img)
        
        toDoList.appendChild(item)
        registerCheckBoxes()
        registerDelete()
        registerRestore()
      }

document.getElementById("saveChangesForm").addEventListener("submit",e=>{
    e.preventDefault()
    let name=e.target.taskName.value
    addItem(name,"todo")
})

