import pymysql


def open_database_mc_skin():
    try:
        db = pymysql.connect(host='localhost', user='varus', password='', port=3306, database='mc_skin', autocommit=True)
        print('Database mc_skin open successfully')
    except pymysql.Error as err:
        print(err)
        return None
    return db


def close_database(db):
    db.close()


def select_skin_url_from_skin(db):
    cur = db.cursor()
    cur.execute("SELECT `skin_url` from `skin`")
    res = cur.fetchall()
    cur.close()
    return res


def select_skin_preview_url_from_skin(db):
    cur = db.cursor()
    cur.execute("SELECT `skin_preview` from `skin`")
    res = cur.fetchall()
    cur.close()
    return res

