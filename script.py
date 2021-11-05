from ResponseHandler import ResponseHandler
from database import Database
import re
expression = r"[-a-zA-Z0-9@: % ._\+~  # =]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)"

db = Database()
responseHandler = ResponseHandler("./responses.json")

url = None
while url is None:
    scammingMessage = input("Enter a scamming message: ")
    url = re.search(expression, scammingMessage)
    if url is None:
        print(responseHandler.getResponse(scammingMessage))

db.addEntry(url.group(0))
