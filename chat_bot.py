import vk_api
import configparser
from vk_api.longpoll import VkLongPoll, VkEventType

config = configparser.ConfigParser()
config.read("token.ini")

vk_session = vk_api.VkApi(token=config["Token"]["token2"])
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

# ----------------------Класс бота который принимает токен сообщества где находится---------------
class Vk_bot():
    def __init__(self):
        self.list = []
        self.sex = ''
        self.city = ''
        self.age_from = ''
        self.age_to = ''

    def send_some_msg(self, id, some_text):
        vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": "0"})

    def start_chat_bot(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()
                    id = event.user_id
                    if msg == "hi":
                        self.send_some_msg(id, "Hi friend!")
                        self.send_some_msg(id, "Введите желаемый пол собеседника\n'М - Мужчина'/'Д - Девушка'")
                        self.sex_chat_bot()
                        break

    def sex_chat_bot(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()
                    id = event.user_id
                    if msg == "м":
                        self.send_some_msg(id, "Введите город\nМосква/Хабаровск/Владивосток")
                        self.sex = '2'
                        self.city_chat_bot()
                        break
                    elif msg == "д":
                        self.send_some_msg(id, "Введите город Москва/Хабаровск/'Владивосток")
                        self.sex = '1'
                        self.city_chat_bot()
                        break
                    else:
                        self.send_some_msg(id, "Таких людей не существует, введите коректно пол")
                        continue

    def city_chat_bot(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()
                    id = event.user_id
                    if msg == 'москва':
                        self.city = '1'
                        self.send_some_msg(id, "Введите возраст от")
                        self.age_from_chat_bot()
                        break
                    elif msg == 'хабаровск':
                        self.city = '153'
                        self.send_some_msg(id, "Введите возраст от")
                        self.age_from_chat_bot()
                        break
                    elif msg == 'владивосток':
                        self.city = '37'
                        self.send_some_msg(id, "Введите возраст от")
                        self.age_from_chat_bot()
                        break
                    else:
                        self.send_some_msg(id, "Таких городов я не знаю,\n введите Москва/Хабаровск/Владивосток")
                        continue

    def age_from_chat_bot(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()
                    id = event.user_id
                    if msg == msg:
                        self.age_from = str(msg)
                        self.send_some_msg(id, "Введите возраст до")
                        self.age_to_chat_bot()
                        break

    def age_to_chat_bot(self):
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msg = event.text.lower()
                    id = event.user_id
                    if msg == msg:
                        self.age_to = str(msg)
                        self.send_some_msg(id, "Спасибо что ввели данный ведется поиск")
                        break


if __name__ == '__main__':
    bot = Vk_bot()
    bot.start_chat_bot()


