import json
import datetime
import re

data = []

def validIP(ip):
    match = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)
    if not match:
        return False
    ip = []
    for number in match.groups():
        ip.append(int(number))
    if ip[0] < 1:
        return False
    for number in ip:
        if number > 255 or number < 0:
            return False

def askUserForInput():
    userInputList = list()
    question = raw_input("Do you want to search by \"IP\" or \"Port\"? ")
    if question.lower() == "ip":
        while True:
            inputList = raw_input("Please Enter IP Address or Quit: ")
            if inputList.lower() == "quit":
                return True, userInputList
            elif not validIP(inputList):
                print "Not a valid IP Address"
            elif inputList in userInputList:
                print "You have already inputted that IP Address"
            else:
                userInputList.append(inputList)
    elif question.lower() == "port":
        while True:
            inputList = raw_input("Please Enter port or Quit: ")
            if inputList.lower() == "quit":
                return True, userInputList
            elif ('.' in inputList or int(inputList) < 1 or int(inputList) > 65536):
                print "Not a valid port"
            elif inputList in userInputList:
                print "You have already inputted that Port"
            else:
                userInputList.append(inputList)
    else:
        print "ERROR: No matching user input"
        return False, []

def printData(data):
    for key in data:
        if key == 'victimIP' or key == 'attackerIP' or key == 'connectionType' or key == 'victimPort' or key == 'attackerPort':
            print key + " : " + str(data[key])

def getInfomation(jsonData, userInput):
    obj = json.loads(jsonData['payload'])
    for uIn in userInput:
        for key in obj:
            if str(obj[key]) == uIn:
                printData(obj)
                time = re.split(r"[-T:.+]", jsonData['timestamp']['$date'])
                print str(datetime.date(int(time[0]), int(time[1]), int(time[2]))) + "\n"

while True:
    userInputs = askUserForInput()
    if userInputs[0]:
        break

with open("honeypot.json") as f:
    for line in f:
        data.append(json.loads(line))
for jsonData in data:
    getInfomation(jsonData, userInputs[1])
