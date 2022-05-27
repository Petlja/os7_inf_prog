function WrappingAscorinaion(){
    var associationsList = [];
    const checkMarkSVG =  `
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16">
        <path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/>
    </svg>
    `;

    function Associations(opts){
        if(opts){
        this.init(opts);
        }
    }

    Associations.prototype.init =  function(opts){
        this.opts = opts;
        this.game = JSON.parse(popAttribute(opts,"data-game"));
        this.groupList = this.game["clues"];
        this.finalAnswer = this.game["answer"];
        this.finalAnswerRegex = new RegExp(this.finalAnswer);
        this.clueGroupFealdMap = {};
        this.maxNumberOfClues = Math.max.apply(Math, this.groupList.map(function(gr) { return gr.clues.length; }))
        for(var i=0;i<this.groupList.length;i++){
            if (this.groupList[i]["clues"].length > 0 &&  this.groupList[i]["group-answ"] !== "")
                this.createAscGroup(this.groupList[i]);
        }
        this.createFinalAnswerDiv();
    }

    Associations.prototype.createAscGroup = function(group){
        var groupDiv = document.createElement("div");
        groupDiv.classList.add("asc-group");
        var cluesDiv = document.createElement("div");
        if (window.screen.width > 700) 
            cluesDiv.style.height = (this.maxNumberOfClues*35)+"px";
        groupDiv.appendChild(cluesDiv);
        for(var i=0;i<group["clues"].length;i++){
            const clueDiv = document.createElement("div");
            clueDiv.classList.add("asc-clue");
            clueDiv.classList.add("asc-clue-hidden");
            var feald = group["group"] + (i+1);
            this.clueGroupFealdMap[feald] = group["clues"][i];
            clueDiv.setAttribute("data-ord",feald);
            clueDiv.innerText = feald;
            clueDiv.addEventListener("click",function(clicked){
                clicked.currentTarget.innerText = this.clueGroupFealdMap[clicked.currentTarget.getAttribute("data-ord")];
            }.bind(this), {once : true});
            cluesDiv.appendChild(clueDiv);
        }
        var inputDiv = document.createElement("div");
        inputDiv.classList.add("group-test-div");
        var inputButtonDiv = document.createElement("div");
        var input = document.createElement("input");
        input.classList.add("asc-input");
        input.id = "group" + group["group"];
        var inputButton = document.createElement("div");
        inputButton.classList.add("asc-test-answer");
        inputButton.innerText = $.i18n("msg_asc_solve_group");
        inputButton.setAttribute("data-input-id", "group" + group["group"]);
        inputButton.addEventListener("click",function(clicked){
            userAnswer = document.getElementById(clicked.currentTarget.getAttribute("data-input-id")).value.trim()
            if(userAnswer.match(group['group-answ'])){
                clicked.currentTarget.parentElement.nextElementSibling.innerText = userAnswer;
                clicked.currentTarget.parentElement.nextElementSibling.style.display = "block";
                clicked.currentTarget.parentElement.remove();
            }
            else{
                input.classList.add("error-border");
            }
        });
        var corectMsg = document.createElement("div");
        corectMsg.classList.add("correct-msg");
        inputButtonDiv.appendChild(input);
        inputButtonDiv.appendChild(inputButton);
        inputDiv.appendChild(inputButtonDiv);
        inputDiv.appendChild(corectMsg);
        groupDiv.appendChild(inputDiv);
        this.opts.appendChild(groupDiv);
    }

    Associations.prototype.createFinalAnswerDiv = function(){
        var finalAnswerDiv = document.createElement("div");
        finalAnswerDiv.classList.add("answer");
        var input = document.createElement("input");
        var inputTestButton = document.createElement("div");
        inputTestButton.classList.add("asc-final-test-answer");
        inputTestButton.innerText = $.i18n("msg_asc_solve_final");
        inputTestButton.addEventListener("click",function(){
            userAnswer = input.value.trim();
            if(userAnswer.match(this.finalAnswerRegex)){
                inputTestButton.remove();
                input.remove();
                var correctDiv = document.createElement("div");
                correctDiv.classList.add("correct-msg-final");
                correctDiv.innerText = userAnswer;
                correctDiv.innerHTML += checkMarkSVG;
                finalAnswerDiv.appendChild(correctDiv);
            }
            else{
                input.classList.add("error-border");
            }
        }.bind(this));
        finalAnswerDiv.appendChild(input);
        finalAnswerDiv.appendChild(inputTestButton);
        this.opts.appendChild(finalAnswerDiv);
    }

    function popAttribute(element, atribute, fallback){
        var atr = fallback;
        if (element.hasAttribute(atribute)){
            atr = element.getAttribute(atribute);
            element.removeAttribute(atribute);
        }
        return atr;
    }

    window.addEventListener('load',function() {
        associations = document.getElementsByClassName('asc');
        for (var i = 0; i < associations.length; i++) {
            associationsList[associations[i].id] = new Associations(associations[i]);		
        }
    });
}
WrappingAscorinaion();