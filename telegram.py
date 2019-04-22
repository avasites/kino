import requests


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
    url = getUrl(TOKEN, 'sendPhoto')
    files = {'photo': open(photoPath, 'rb')}
    r = requests.post(url, data={'chat_id': '@zheevkino', 'caption': text}, files=files)
    print(r.json())


def sendMessage(text):
    url = getUrl(TOKEN, 'sendMessage')
    requests.post(url, data={'chat_id':'@zheevkino', 'text':text, 'parse_mode':'Markdown'})