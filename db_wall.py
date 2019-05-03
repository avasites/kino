
def getLastIdWall():
    conn = sqlite3.connect("walls.db")
    cursor = conn.cursor()

    sql = "SELECT `id_wall` FROM `list` LIMIT 1"

    cursor.execute(sql)

    return cursor.fetchone()

def insertIdWall(id):
    conn = sqlite3.connect("walls.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM 'list' WHERE rowid = (SELECT rowid FROM 'list' LIMIT 1)")

    conn.commit()

    cursor.execute("INSERT INTO `list` (`id_wall`) VALUES (?)", int(id))

    conn.commit()

    conn.close()
