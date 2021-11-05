import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                                              user="root",         # your username
                                              passwd="",  # your password
                                              db="urlbot")        # name of the data base
            self.cur = self.db.cursor()
            self.cur.execute(
                "CREATE TABLE `urlbot`.`url` ( `id` INT NOT NULL AUTO_INCREMENT , `url` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`))")
        except:
            return

    def addEntry(self, url):
        self.cur.execute(
            "INSERT INTO `url` (`url`) VALUES ('" + str(url) + "');")
        self.db.commit()
