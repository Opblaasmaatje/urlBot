from ResponseHandler import ResponseHandler
# pip install mysql-connector-python
from database import Database
expression = "[-a-zA-Z0-9@: % ._\+~  # =]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

db = Database()

responseHandler = ResponseHandler("./responses.json")
print(responseHandler.getResponse("hello"))
print(responseHandler.getResponse("oude"))
print(responseHandler.getResponse("dit is nog de oude van mijn telefoons"))