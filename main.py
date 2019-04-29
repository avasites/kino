import requests
import db_wall
import telegram
from vars import ACCESS_TOKEN

from urllib.parse import urlencode
domain = 'https://api.vk.com/method/wall.get?'

def getWall(**kwargs):
    r = requests.get(domain+urlencode(kwargs))
    return r.json()

if __name__ == '__main__':
    list = getWall(domain='kino_mania', count=5, offset=1,
                    access_token= ACCESS_TOKEN,
                    v='5.95')['response']['items']

    maxId = db_wall.getLastIdWall()

    for wall in list:
        if wall['attachments']:
            photos  = wall['attachments'][0]['photo']['sizes']
            photoSend = photos[len(photos)-1]
            if maxId:
                if int(maxId[0]) < int(wall['id']):
                    telegram.sendPhoto(wall['text'], photoSend['url'])
            else:
                telegram.sendPhoto(wall['text'], photoSend['url'])

    db_wall.insertIdWall(list[0]['id'])
