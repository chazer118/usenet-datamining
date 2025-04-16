#2 problems:
# 1. It creates end of line chars at the end of each key which is not good, but easily human fixable if I can't sort it
# 2. I need to integrate text formatting. So new lines, etc work. If this doesnt work then this script is pointless.

import csv
import json
import time
import mailbox
from collections import Counter

jsonArray = []
senderArray = []
dateArray = []
msgArray = []

senderData = {}
dateData = {}
msgData = {}

addresses = []
date = []
messageArray = []
messageID = []

print("This will convert a Usenet .MBOX file into a .JSON file.")
mbox = mailbox.mbox(input("Enter input .mbox file: "))
jsonFile = input("Enter output .json file: ")

print ("Reading mailbox")

def mboxToJson(mbox, jsonFile):
    for message in mbox: 
        #Set msg to a matching string "From"
        msgFrom = str(message.get("From", ""))
        msgDate = str(message.get("Date"))
        msgContent = str(message.get_payload())

        #Remove commas
        #msgFrom = msgFrom.replace(",", "")
        #msgDate = msgDate.replace(",", "")
        #msgContent = msgContent.replace(",", "")

        #Append to the corresponding array
        addresses.append(msgFrom)
        date.append(msgDate)
        messageArray.append(msgContent.replace(" \n", "\n").replace(" \n\n", "\n\n"))

        #\n is added once it has been appended to an array so we need to work here
        #msg_clean = msgContent.replace(" \n", "\n")
        
    with open (jsonFile, 'w') as json_file:
        
        senderData['Sender'] = addresses
        dateData['Date'] = date
        msgData['Message'] = messageArray

        jsonSender = json.dumps(senderData, indent=4)
        jsonDate = json.dumps(dateData, indent=4)
        jsonMsg = json.dumps(msgData, indent=4)
        
        json_file.write(jsonSender)
        json_file.write(jsonDate)
        json_file.write(jsonMsg)
    
start = time.perf_counter()
mboxToJson(mbox, jsonFile)
finish = time.perf_counter()

print(f"Converted successfully in {finish-start:0.4f} seconds")