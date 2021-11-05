import json

class ResponseHandler:
    def __init__(self, responsesFilename):
        self.responses = self.readResponses(responsesFilename)["responses"]

    def readResponses(self, responsesFilename):
        with open(responsesFilename, 'r') as responsesFile:
            responses = responsesFile.read()
        return json.loads(responses)

    def getResponse(self, message):
        for response in self.responses:
            for key in response["keys"]:
                keyWords = key.lower().split(";")
                if all(word in message.lower() for word in keyWords):
                    return response["response"]
        return "Ik weet niet wat je bedoeld."