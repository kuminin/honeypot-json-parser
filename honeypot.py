import json
import datetime
import re

data = []

def askUserForInput():
    userInputList = list()
    question = raw_input("Do you want to search by IP or port? ")
    if question.lower() == "victimip":
        while True:
            inputList = raw_input("Please Enter IP or Quit: ")
            if inputList.lower() == "quit":
                return userInputList
            userInputList.append(inputList)
    elif question.lower() == "port":
        while True:
            inputList = raw_input("Please Enter port or Quit: ")
            if inputList.lower() == "quit":
                return userInputList
            userInputList.append(inputList)
    else:
        print "ERROR: No matching user input"
        return

def printData(data):
    for key in data:
        if key == 'victimIP' or key == 'attackerIP' or key == 'connectionType' or key == 'victimPort' or key == 'attackerPort':
            print key + " : " + str(data[key])

def getInfomation(jsonData, userInput):
    for key in jsonData:
        if key == 'payload':
            obj = json.loads(jsonData['payload'])
            for uIn in userInput:
                for key in obj:
                    if str(obj[key]) == uIn:
                        printData(obj)
                        time = re.split(r"[-T:.+]", jsonData['timestamp']['$date'])
                        print str(datetime.date(int(time[0]), int(time[1]), int(time[2]))) + "\n"


with open("honeypot.json") as f:
        for line in f:
            data.append(json.loads(line))

userInputs = askUserForInput()

for jsonData in data:
    getInfomation(jsonData, userInputs)
