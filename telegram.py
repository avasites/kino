import json

import requests
import vars

def getUrl(TOKEN, type):
    return "https://api.telegram.org/bot{0}/{1}".format(TOKEN, type)

def getPhoto(photo):
    p = requests.get(photo)
    fotoName = photo.split('/')
    name = "./photo/{}".format(fotoName[len(fotoName) - 1])
    out = open(name, "wb")
    out.write(p.content)
    out.close()
    return name

def sendPhoto(text, photo):
    photoPath = getPhoto(photo)
    url = getUrl(vars.TOKEN, 'sendPhoto')
    files = {'photo': open(photoPath, 'rb')}
    r = requests.post(url, data={'chat_id': '@zheevkino', 'caption': text}, files=files)
    out = open('data.txt', "wb")
    out.write(b'a')
    out.close()


def sendMessage(text):
    url = getUrl(vars.TOKEN, 'sendMessage')
    requests.post(url, data={'chat_id':'@zheevkino', 'text':text, 'parse_mode':'Markdown'})