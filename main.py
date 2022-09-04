import requests
import configparser
from pprint import pprint
from chat_bot import Vk_bot

config = configparser.ConfigParser()
config.read("token.ini")

# -----------Класс который ищет по параметрам полученных с бота, так же принимает в себя токен api vk для поиска--------
class VK_users():
    # def __init__(self, token, sex, city, age_from, age_to):
    #     self.token = token
    #     self.sex = sex
    #     self.city = city
    #     self.age_from = age_from
    #     self.age_to = age_to

    def __init__(self, token):
        self.token = token
        self.sex = '1'
        self.city = '1'
        self.age_from = '20'
        self.age_to = '25'

    def info_vk_profiles(self):
        url = "https://api.vk.com/method/users.search"
        params = {
            'count': '2',
            'access_token': self.token,
            'v': '5.131',
            'id': '1',
            'city': '153',
            'sex': self.sex,
            'age_from': self.age_from,
            'age_to': self.age_to
        }
        new_url = requests.get(url, params=params)
        users = new_url.json()
        pprint(len(users['response']['items']))
        # pprint(users)
        return users

    def get_user(self):
        url_photos = []
        users_json = []
        user_json = {}
        like = []
        user = self.info_vk_profiles()
        for i in user['response']['items']:
            id_user = i['id']
            url = "https://api.vk.com/method/photos.get"
            params = {
                'access_token': self.token,
                'v': '5.131',
                'owner_id': id_user,
                'album_id': 'profile',
                'extended': '1'
            }
            new_url = requests.get(url, params=params)
            users = new_url.json()

            for like_photo in users['response']['items']:
                like.append(like_photo['likes']['count'])
            max_like = sorted(like, reverse=True)
            for max_size in users['response']['items']:
                if max_size['likes']['count'] in max_like[:3]:
                    max_height = 0
                    url = ''
                    for b in max_size['sizes']:
                        if int(b['height'] + b['width']) > max_height:
                            max_height += b['height'] + b['width']
                            url = b['url']
                    url_photos.append(url)
            user_json = {'id_user': id_user, 'url': url_photos}
        users_json.append(user_json)
        pprint(users_json)



if __name__ == '__main__':
    # bot = Vk_bot()
    # bot.start_chat_bot()
    # lol = VK_users(config["Token"]["token1"], bot.sex, bot.city, bot.age_from, bot.age_to)
    lol = VK_users(config["Token"]["token1"])
    lol.get_user()