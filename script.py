from ResponseHandler import ResponseHandler

responseHandler = ResponseHandler("./responses.json")
print(responseHandler.getResponse("hello"))
print(responseHandler.getResponse("oude"))
print(responseHandler.getResponse("dit is nog de oude van mijn telefoons"))