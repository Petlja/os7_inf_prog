var p5jsEditors = {}
var p5jsEditorsWidths = {}
window.addEventListener('load',function(){
    p5jsEditors = document.getElementsByClassName('p5js-resize');
    for(var i=0; i<p5jsEditors.length;i++){
        var editorWidth = p5jsEditors[i].getBoundingClientRect().width;
        p5jsEditorsWidths[i] = editorWidth;
        var mainContentWidth = document.getElementById('main-content').getBoundingClientRect().width;
        if(editorWidth >  mainContentWidth){
           if(!p5jsEditors[i].classList.contains('p5js-resize-ss')){
            p5jsEditors[i].classList.add('p5js-resize-ss');
            p5jsEditors[i].parentElement.classList.add('p5js-container-ss');
           }
        }
    }
});

window.addEventListener('resize', function(event){
    for(var i=0; i<p5jsEditors.length;i++){
        var editorWidth = p5jsEditors[i].getBoundingClientRect().width;
        var mainContentWidth = document.getElementById('main-content').getBoundingClientRect().width;
        if(editorWidth >  mainContentWidth){
           if(!p5jsEditors[i].classList.contains('p5js-resize-ss')){
            p5jsEditors[i].classList.add('p5js-resize-ss');
            p5jsEditors[i].parentElement.classList.add('p5js-container-ss');
           }
        }
        if((editorWidth < mainContentWidth) && mainContentWidth > 780 && p5jsEditorsWidths[i] < mainContentWidth){
            if(p5jsEditors[i].classList.contains('p5js-resize-ss')){
             p5jsEditors[i].classList.remove('p5js-resize-ss');
             p5jsEditors[i].parentElement.classList.remove('p5js-container-ss');
            }
         }
    }
  });