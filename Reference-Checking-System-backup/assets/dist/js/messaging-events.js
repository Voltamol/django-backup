
        let textarea=document.querySelector("#textArea");
        let form=document.getElementById("message-form");
        form.addEventListener('submit',(e)=>{
            e.preventDefault()
            let message=e.target.message.value
            let filename=e.target.chat_images.value
            //chatsocket.send(JSON.stringify({'message':message}))
            
            if(filename!=''){
                children=paraContents()
                para=createResponse(children,"me")
                scrollDown()
            }
            createResponse(message,'me')
            scrollDown()
            //let elements=upload_file(src)
        form.reset()

    })


        function resize_textarea(){
            textarea.style.height='60px';
        }

        is_string = function(input) {
            if (Object. prototype. toString. call(input) === '[object String]'){
                return true;
            }
            
            else{
                return false;
            }
            
            };

    
        function createPara(userInput,user){
            let para=document.createElement("p")
            if(is_string(userInput)){
                para.innerText=userInput
            }else{
                for(let child of userInput){
                    para.appendChild(child)
                }
            }
            para.classList.add("message")
            para.classList.add(user)
            para.classList.add("relative")
            return para
        }

        function paraContents(){
            let main_img=document.createElement("img")
            main_img.classList.add("rounded")
            main_img.style.width="300px"
            let src=document.getElementById("chat-preview").src
            main_img.src=src
            let download_icon=document.createElement("img")
            let classNames=Array("absolute-bottom","medium-icon","rounded","download-icon")
            for(let classname of classNames){
                download_icon.classList.add(classname)
            }
            download_icon.src="assets/dist/images/Download icon.jpg"
            console.log(src)
            return Array(main_img,download_icon)
        }

        function createResponse(userInput,user){
          
            let container=document.querySelector(".message-area")
            let message_container=document.createElement("div")
            let container_classes=Array("message-container","full-width","vertical-start")
            for(let classname of container_classes){
                message_container.classList.add(classname)
            }
            if(userInput){
                let para=createPara(userInput,user)
                if(user=="me"){
                    para.classList.add("bg-info")
                }else{
                    para.classList.add("bg-light")
                }
                message_container.appendChild(para)
                container.appendChild(message_container)
                
            }else{

            }
        }

        function send_message(){
            let submitBtn=document.querySelector("#submit-button");
            submitBtn.click()
            
        }

        function scrollDown(){
            let chartArea=document.querySelector(".message-area");
            chartArea.scrollTop=chartArea.scrollHeight;
        }