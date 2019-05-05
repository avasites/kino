import requests
import db_wall
import telegram
from vars import A_T as ACCESS_TOKEN

from urllib.parse import urlencode
domain = 'https://api.vk.com/method/wall.get?'


def getWalls(**kwargs):
    r = requests.get(domain+urlencode(kwargs))
    return r.json()


if __name__ == '__main__':
    request = getWalls(domain='kino_mania', count=5, offset=1,
                       access_token=ACCESS_TOKEN,
                       v='5.95')

    walls = request['response']['items']

    maxId = db_wall.getLastIdWall()

    for wall in walls:
        if wall['attachments']:
            if wall['attachments'][0]['photo']:
                photos = wall['attachments'][0]['photo']['sizes']
                photo_for_send = photos[len(photos)-1]
                if maxId:
                    if int(maxId[0]) < int(wall['id']):
                        telegram.sendPhoto(wall['text'], photo_for_send['url'])
                else:
                    telegram.sendPhoto(wall['text'], photo_for_send['url'])

    db_wall.insertIdWall(walls[0]['id'])
