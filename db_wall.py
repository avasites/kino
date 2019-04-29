import sqlite3


def getLastIdWall():
    conn = sqlite3.connect("walls.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS `list` (`id_wall` INT)""")

    conn.commit()

    sql = "SELECT `id_wall` FROM `list` ORDER BY rowid DESC LIMIT 1"

    cursor.execute(sql)

    return cursor.fetchone()

def insertIdWall(id):
    conn = sqlite3.connect("walls.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS `list` (`id_wall` INT)""")

    cursor.execute("DELETE FROM 'list' WHERE rowid = (SELECT rowid FROM 'list' LIMIT 1)")

    cursor.execute("INSERT INTO `list` (`id_wall`) VALUES (?)", int(id))

    conn.commit()

    conn.close()
