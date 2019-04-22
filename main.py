import requests
import db_wall
import telegram

from urllib.parse import urlencode
domain = 'https://api.vk.com/method/wall.get?'

def getWall(**kwargs):
    r = requests.get(domain+urlencode(kwargs))
    return r.json()

if __name__ == '__main__':
    list = getWall(domain='kino_mania', count=5, offset=1,
                    access_token='017d1e79017d1e79017d1e79f301173f3f0017d017d1e795dc1a1d713d84d403724c3a5',
                    v='5.95')['response']['items']

    maxId = db_wall.getLastIdWall()

    for wall in list:
        if wall['attachments']:
            photos  = wall['attachments'][0]['photo']['sizes']
            photoSend = photos[len(photos)-1]
            if maxId:
                if maxId[0] < wall['id']:
                    telegram.sendPhoto(wall['text'], photoSend['url'])
            else:
                telegram.sendPhoto(wall['text'], photoSend['url'])

    db_wall.insertIdWall(list[0]['id'])
