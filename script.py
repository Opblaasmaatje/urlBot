# pip install mysql-connector-python
from database import Database
expression = "[-a-zA-Z0-9@: % ._\+~  # =]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

link = "test"

db = Database()
# db.addEntry(link)
