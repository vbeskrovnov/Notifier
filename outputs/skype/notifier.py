from skpy import Skype

chat_bot_login = ""
chat_bot_password = ""
chat_url = ""

skype = Skype(chat_bot_login, chat_bot_password)


def notify(message):
    chat = skype.chats.chat(skype.chats.urlToIds(chat_url)['id'])
    chat.sendMsg(message)
