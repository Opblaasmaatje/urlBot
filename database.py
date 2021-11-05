import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        try:
            db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                                         user="root",         # your username
                                         passwd="",  # your password
                                         db="urlBot")        # name of the data base
            cur = db.cursor()
            cur.execute(
                "CREATE TABLE `urlbot`.`url` (`id` serial,`url` VARCHAR(255));")
        except:
            return
