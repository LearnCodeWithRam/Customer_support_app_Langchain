css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #ADFF2F
}

.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar1 {
  width: 20%;
}
.chat-message .avatar2 {
  width: 20%;
}
.chat-message .avatar1 img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .avatar2 img {
  max-width: 78px;
  max-height: 75px;
  border-radius: 50%;
  object-fit: cover;
}
div.avatar2 {
  position: absolute;
  top:0;
  right: 0;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.chat-message .message1 {
  width: 80%;
  padding: 0 1.5rem;
  color: #000000;
}


'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar1">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar2">
        <img src="https://i.ibb.co/8xrqNY6/human.png" alt="human" border="0">
    </div>    
    <div class="message1">{{MSG}}</div>
</div>
'''
