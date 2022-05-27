function WrappingRegexCheck(){ 
var regexCheckList = [];

function RegexCheck(opts){
    if(opts){
    this.init(opts);
    }
}

RegexCheck.prototype.init =  function(opts){
    this.opts = opts;
    this.data =  JSON.parse(popAttribute(opts,'data-regex'));
    this.text = this.data['text'];
    this.solution = this.data['solution'];
    this.hasSolution = this.solution.length != 0;
    this.editableText = this.data['editable'];
    this.regexFlags = this.data['flags'];
    this.regexArea = this.opts.querySelector('.regex-input');
    this.textArea =  this.opts.querySelector('.text-input'); 
    this.customArea =  this.opts.querySelector('.front'); 
    // regex title
    this.opts.querySelectorAll('.title')[0].innerHTML =  $.i18n("regex_title");
    // flags title`
     this.opts.querySelectorAll('.title')[1].innerHTML =  `${$.i18n("flag_title")}  <span class="flag-markers">${this.regexFlags}</span>`;
    // text flags
    this.opts.querySelectorAll('.title')[2].innerHTML =  $.i18n("text_title");

    
    this.textArea.value = this.text;
    this.customArea.innerHTML =htmlEscape(this.textArea.value);

    if(this.hasSolution){
        this.msg = document.createElement('p');
        this.msg.classList.add("msg-testing")
        this.opts.appendChild(this.msg);
    
        this.solButton = this.opts.querySelector('.sol-button');
        this.solButton.innerHTML = $.i18n("button_text"); 
        this.solButton.addEventListener("click", function(){
            var text = this.textArea.value;
            try{
               var re = new RegExp('('+ this.solution+ ')',flag=this.regexFlags);
               this.customArea.innerHTML = htmlEscape(text.replace(re,"<span class='blue'>$1</span>"));
            }
            catch{
            }
        }.bind(this));
        this.testButton = this.opts.querySelector('.test-button');
        this.testButton.innerHTML = $.i18n("button_test"); 
        this.testButton.addEventListener("click", function(){
            var text = this.textArea.value;         
            try{
               var re = new RegExp('('+ this.solution+ ')',flag=this.regexFlags);
               var reUser =  new RegExp('('+ this.regexArea.value + ')',flag=this.regexFlags);
               var match = text.match(re);
               var matchUser = text.match(reUser);         
               if( match.length === matchUser.length && match.every(function(value, index) { return value === matchUser[index]})){
                    this.msg.innerText = $.i18n("correct")
                    this.msg.classList.remove("incorrect");
                    this.msg.classList.add("correct");
               }
               else{
                    this.msg.innerText = $.i18n("incorrect")
                    this.msg.classList.remove("correct");
                    this.msg.classList.add("incorrect");
               }
            }
            catch{
            }
        }.bind(this));
    }
    if(!this.editableText){
        this.textArea.setAttribute('disabled', 'true');
    }
    else{   
        this.textArea.addEventListener('input', function(){
            this.customArea.innerHTML = htmlEscape(this.textArea.value);
        }.bind(this));


        this.textArea.addEventListener('keydown', function(e) {
           if (e.key == 'Tab') {
               e.preventDefault();
               var start =  this.textArea.selectionStart;
               var end =  this.textArea.selectionEnd;
   
               this.textArea.value =  this.textArea.value.substring(0, start) + '\t' + this.textArea.value.substring(end);
               this.textArea.selectionStart =  this.textArea.selectionEnd = start + 1;
               this.customArea.innerHTML = htmlEscape(this.textArea.value);
           }
         }.bind(this));
    }

    this.regexArea.addEventListener('input', function(){
        this.msg.innerText = ""
        if (this.regexArea.value == ''){
           this.customArea.innerHTML = htmlEscape(this.textArea.value);
           return 
        }
        var text = this.textArea.value;
        try{
           var re = new RegExp('('+ this.regexArea.value+ ')',flag=this.regexFlags);
           this.customArea.innerHTML = htmlEscape(text.replace(re,"<span class='blue'>$1</span>"));
        }
        catch{
        }
    }.bind(this));
    
}

function popAttribute(element, atribute, fallback = ''){
    var atr = fallback;
    if (element.hasAttribute(atribute)){
        atr = element.getAttribute(atribute);
        element.removeAttribute(atribute);
    }
    return atr;
}
function htmlEscape(str){
    return str.replaceAll('\n' ,'<br>').replaceAll(' </span>', '&nbsp;</span>').replaceAll("<span class='blue'><br></span>","<span class='blue eol'></span><br>");
}

String.prototype.replaceAt = function(index, replacement) {
    return this.substring(0, index) + replacement + this.substring(index + this.length);
}

window.addEventListener('load',function() {
    regexCheckers = document.getElementsByClassName('regex-check');
    for (var i = 0; i < regexCheckers.length; i++) {
        regexCheckList[regexCheckers[i].id] = new RegexCheck(regexCheckers[i]);		
    }
});

};
WrappingRegexCheck();
