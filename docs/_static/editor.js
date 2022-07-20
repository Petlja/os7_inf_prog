function WrappingAscorinaion(){
    var editorArray = [];

    

    function Editor(opts){
        if(opts){
        this.init(opts);
        }
    }

    Editor.prototype.init =  function(opts){
        this.opts = opts;
        this.data = JSON.parse(popAttribute(opts,"data"));
        this.id = opts.id;
    }

    Editor.prototype.funkcija = function(group){
        
        // nesto
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
        var editors = document.getElementsByClassName('petlja-editor');
        for (var i = 0; i < editors.length; i++) {
            editorArray[i] = new Editor(editors[i]);		
        }

        editorArray.forEach(editor => {
            var editorsContainer = document.createElement('div');
            editorsContainer.setAttribute('class', 'editor-cotainer');
            var editorsContainerTabs = document.createElement('div');
            editorsContainerTabs.setAttribute('id', 'tabs-' + editor.id);
            editorsContainerTabs.setAttribute('class','title-tab');
            editorsContainer.append(editorsContainerTabs);
            document.getElementById(editor.id).append(editorsContainer);
            if (editor.data.hasOwnProperty('html')) {
                var htmlDiv = document.createElement('div');
                htmlDiv.setAttribute('class', 'editor-container');
                htmlDiv.setAttribute('id', 'htmleditor-' + editor.id);
                var editorTabLabel = document.createElement('div');
                editorTabLabel.setAttribute('class', 'editor-title active');
                editorTabLabel.setAttribute('data-editorid', editor.id);
                editorTabLabel.setAttribute('data-tab', 'html');
                editorTabLabel.setAttribute('id', 'htmltab-' + editor.id);
                editorTabLabel.innerHTML =  editor.data['html'].name;
                editorsContainerTabs.append(editorTabLabel);
               // htmlDiv.innerHTML = editorTitle;
                document.getElementById(editor.id).append(htmlDiv);
                var htmlCodeMirror = CodeMirror(htmlDiv, {
                    value: editor.data['html'].source,
                    mode:  "htmlmixed",
                    lineNumbers: true,
                    id: 'codeMirror-' + editor.id + '-html'
                  });
                  htmlCodeMirror.setSize(null,275);
                  editor.htmlEditor  = htmlCodeMirror;
            }

            if (editor.data.hasOwnProperty('js')) {
                var jsDiv = document.createElement('div');
                jsDiv.setAttribute('class', 'editor-container d-none');
                jsDiv.setAttribute('id', 'jseditor-' + editor.id);
                var editorTabLabel = document.createElement('div');
                editorTabLabel.setAttribute('class', 'editor-title');
                editorTabLabel.setAttribute('data-editorid', editor.id);
                editorTabLabel.setAttribute('data-tab', 'js');
                editorTabLabel.setAttribute('id', 'jstab-' + editor.id);
                editorTabLabel.innerHTML =  editor.data['js'].name;
                editorsContainerTabs.append(editorTabLabel);
                document.getElementById(editor.id).append(jsDiv);
                var jsCodeMirror = CodeMirror(jsDiv, {
                    value: editor.data['js'].source,
                    mode:  "javascript",
                    lineNumbers: true,
                    id: 'codeMirror-' + editor.id + '-js'
                  });
                  jsCodeMirror.setSize(null,275);
                editor.jsEditor  = jsCodeMirror;
            }
            if (editor.data.hasOwnProperty('css')) {
                var cssDiv = document.createElement('div');
                cssDiv.setAttribute('class', 'editor-container d-none');
                cssDiv.setAttribute('id', 'csseditor-' + editor.id);
                var editorTabLabel = document.createElement('div');
                editorTabLabel.setAttribute('class', 'editor-title');
                editorTabLabel.setAttribute('data-editorid', editor.id);
                editorTabLabel.setAttribute('data-tab', 'css');
                editorTabLabel.setAttribute('id', 'csstab-' + editor.id);
                editorTabLabel.innerHTML =  editor.data['css'].name;
                editorsContainerTabs.append(editorTabLabel);
                document.getElementById(editor.id).append(cssDiv);
                var cssCodeMirror = CodeMirror(cssDiv, {
                    value: editor.data['css'].source,
                    mode:  "css",
                    lineNumbers: true,
                    id: 'codeMirror-' + editor.id + '-css'
                  });
                  cssCodeMirror.setSize(null,275);
                  editor.cssEditor  = cssCodeMirror;
            }


            Array.prototype.forEach.call(document.getElementsByClassName('editor-title'), function(elem) {
                elem.addEventListener("click", function(e) {
                    var editorId = e.currentTarget.dataset.editorid;
                    var tab = e.currentTarget.dataset.tab;
                    var currentActiveTab = document.querySelector('[id="'+editorId+'"]').querySelector('.editor-title.active');
                    if (currentActiveTab != null) {
                        currentActiveTab.classList.remove('active');
                        var currentActiveEditor = currentActiveTab.dataset.tab;
                        document.getElementById(currentActiveEditor + 'editor-' + editorId).classList.add('d-none');
                    }
                    document.getElementById(tab + 'tab-' + editorId).classList.add('active');
                    document.getElementById(tab + 'editor-' + editorId).classList.remove('d-none');
                    document.getElementById(tab + 'editor-' + editorId).children[0].CodeMirror.refresh()
                    document.getElementById(editorId + "-iframe").classList.add('d-none');
                    
                })
            })
            

            var htmliframe = document.createElement('iframe');
            htmliframe.setAttribute('class', 'editor-container d-none');
            htmliframe.setAttribute('id', editor.id + "-iframe");
            document.getElementById(editor.id).append(htmliframe);
                
            var playBtn = document.createElement('div');
            playBtn.innerHTML = $.i18n("show_page");;
            playBtn.setAttribute('data-editorId', editor.id);
            playBtn.setAttribute('class', 'editor-play');
            playBtn.addEventListener('click', function(e) {
                var editorsId = e.currentTarget.dataset.editorid;
                var editor = editorArray.find(e => e.id == editorsId);

                var htmlData = editor.htmlEditor.getValue();

                if (editor.data.hasOwnProperty('css')) {
                    var cssBlob = new Blob(["" + editor.cssEditor.getValue()], {type: "text/css"});
                    htmlData = htmlData.replaceAll(editor.data["css"].name, URL.createObjectURL(cssBlob));

                }
                
                if (editor.data.hasOwnProperty('js')) {
                    var jsBlob = new Blob(["" + editor.jsEditor.getValue()], {type: "text/javascript"});
                    htmlData = htmlData.replaceAll(editor.data["js"].name, URL.createObjectURL(jsBlob));

                }


                var htmlBlob = new  Blob(["" + htmlData], {type: "text/html"});
                var htmlURL = URL.createObjectURL(htmlBlob);

                if(!document.getElementById(editor.id + "-iframe")) {
                var htmliframe = document.createElement('iframe');
                htmliframe.setAttribute('style', 'width: calc(50% - 3px); height: 330px; display: none;');
                htmliframe.setAttribute('id', editor.id + "-iframe");
                document.getElementById(editor.id).append(htmliframe);
                } else {
                    document.getElementById(editor.id + "-iframe").classList.remove('d-none');
                    var currentActiveTab = document.querySelector('[id="'+editor.id+'"]').querySelector('.editor-title.active');
                    currentActiveTab.classList.remove('active');
                    var currentActiveEditor = currentActiveTab.dataset.tab;
                    document.getElementById(currentActiveEditor + 'editor-' + editor.id).classList.add('d-none');
                }
                
                document.getElementById(editor.id + "-iframe").setAttribute('src', htmlURL);

                

            });


            var downloadBtn = document.createElement('div');
            downloadBtn.innerHTML = '<i class="fa fa-download" aria-hidden="true"></i>';
            downloadBtn.setAttribute('data-editorId', editor.id);
            downloadBtn.setAttribute('class', 'editor-play ml-3');
            downloadBtn.addEventListener('click', function(e) {
                var editorsId = e.currentTarget.dataset.editorid;
                var editor = editorArray.find(e => e.id == editorsId);

                var zip = new JSZip();

                zip.file(editor.data["html"].name, editor.htmlEditor.getValue());
                zip.file(editor.data["js"].name, editor.jsEditor.getValue());
                zip.file(editor.data["css"].name , editor.cssEditor.getValue());


                zip.generateAsync({type:"base64"}).then(function (content) {
                    var link = document.createElement('a');
                    link.href = "data:application/zip;base64," + content;
                    link.download = "petlja-files.zip";
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
               });

                

            });
            var btnDiv = document.createElement('div');
            editorsContainerTabs.append(downloadBtn)
            editorsContainerTabs.append(playBtn);
            btnDiv.setAttribute('class', 'editor-btn');
            document.getElementById(editor.id).append(btnDiv);
        });


    });
}
WrappingAscorinaion();