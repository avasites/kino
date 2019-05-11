import os
from vars import PATH

filePath = '{}/id.txt'.format(PATH)


def getLastIdWall():
    id = 0
    if os.path.exists(filePath):
        f = open(filePath)
        id = f.read()
        f.close()

    return int(id)


def insertIdWall(id):
    f = open(filePath, 'w')
    f.write(str(id))
    f.close()
