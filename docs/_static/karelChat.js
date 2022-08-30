var Chat = (function() { 
    function Chat(node) {
        this.windowNode = node;
    }

    Chat.prototype.clone = function () {
        var c = new Chat(this.windowNode);
        return c;
    }

    Chat.prototype.clearMessages = function () {
        while (this.windowNode.lastChild) {
            this.windowNode.removeChild(this.windowNode.lastChild);
        }
        this.windowNode.style.display = "none";
    }

    Chat.prototype.showMessage = function (message) {
        if(message === true){
            message = $.i18n("msg_karel_true");
        }
        else if (message === false){
            message = $.i18n("msg_karel_false");
        }
        var bubble = document.createElement("div");
        bubble.innerHTML = '<img src = "..\\_static\\img\\karel-head.png"> <div class = "chat-bubble">' + message + '</div>';
        bubble.className = 'chat-message';
        this.windowNode.appendChild(bubble);
        this.windowNode.style.display = "block";
    }

    Chat.prototype.showUserMessage = function (message) {
    }

    Chat.prototype.disableSendingMessages = function () {
    }

    Chat.prototype.enableSendingMessages = function (src) {
       /* if(src==null) {
            src = "Default_Avatar.png";
        }
        document.getElementById("sendMessageBlock").style.display = "flex";
        document.querySelector('[data-type="template-right"]').querySelector("img").src = src;
        document.getElementById("userSendMessage").onclick = function() {
        var message = document.getElementById("newMessage").value;
        userMessage(message);
        }*/
    }

    return Chat;
})();

