import requests
import vars
import json


def getUrl(TOKEN, type):
    return "https://api.telegram.org/bot{0}/{1}".format(TOKEN, type)


def getPhoto(photo):
    p = requests.get(photo)
    fotoName = photo.split('/')
    name = "{0}/photo/{1}".format(vars.PATH, fotoName[len(fotoName) - 1])
    out = open(name, "wb")
    out.write(p.content)
    out.close()
    return name


def sendPhoto(text, photo):
    photoPath = getPhoto(photo)
    url = getUrl(vars.TOKEN, 'sendPhoto')
    files = {'photo': open(photoPath, 'rb')}
    r = requests.post(url,
                      data={'chat_id': '@zheevkino', 'caption': text[:199]},
                      files=files)
    with open("{}/data_file.json".format(vars.PATH), "w") as write_file:
        json.dump(r.json(), write_file)


def sendMessage(text):
    url = getUrl(vars.TOKEN, 'sendMessage')
    requests.post(url, data={'chat_id': '@zheevkino', 'text': text,
                             'parse_mode': 'Markdown'})
