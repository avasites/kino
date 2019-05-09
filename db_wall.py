import os


def getLastIdWall():
    id = 0
    if os.path.exists('./id.txt'):
        f = open('./id.txt')
        id = f.read()
        f.close()

    return int(id)


def insertIdWall(id):
    f = open('./id.txt', 'w')
    f.write(str(id))
    f.close()
