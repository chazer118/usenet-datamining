# 1. It creates end of line chars at the end of each key which is not good, but easily human fixable if I can't sort it
# 2. Could be two separate functions really to make the code easier to read and more modular

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
subjectData = {}

addresses = []
date = []
messageArray = []
messageID = []
subjectArray = []

print("This will convert a Usenet .MBOX file into a .JSON file.")
mbox = mailbox.mbox(input("Enter input .mbox file: "))
jsonFile = input("Enter output .json file: ")

print ("Reading mailbox")

def mboxToJson(mbox, jsonFile):
    for message in mbox: 
        #Set msg to a matching string "From"
        msgFrom = str(message.get("From", ""))
        msgDate = str(message.get("Date"))
        msgSubject = str(message.get("Subject"))
        msgContent = str(message.get_payload())

        #Remove commas
        #msgFrom = msgFrom.replace(",", "")
        #msgDate = msgDate.replace(",", "")
        #msgContent = msgContent.replace(",", "")

        #Hides the username from the email addresses
        try:
            
                emailSplit = msgFrom.split('@')
                usernameMasked = 'x'*(len(emailSplit[0]))
                emailMasked = (usernameMasked + '@' + emailSplit[1])
                #print(emailMasked)
        except:
             print("An error occurred trying to mask this address: " + msgFrom)
             pass


        #Append to the corresponding array
        addresses.append(emailMasked)
        date.append(msgDate)
        subjectArray.append(msgSubject)
        messageArray.append(msgContent.replace(" \n", "\n").replace(" \n\n", "\n\n"))

        #\n is added once it has been appended to an array so we need to work here
        #msg_clean = msgContent.replace(" \n", "\n")
        
        with open (jsonFile, 'w') as json_file:
                
                senderData['Sender'] = addresses
                dateData['Date'] = date
                subjectData['Subject'] = subjectArray
                msgData['Message'] = messageArray

                jsonSender = json.dumps(senderData, indent=4)
                jsonDate = json.dumps(dateData, indent=4)
                jsonSubject = json.dumps(subjectData, indent=4)
                jsonMsg = json.dumps(msgData, indent=4)
                
                json_file.write(jsonSender)
                json_file.write(jsonDate)
                json_file.write(jsonSubject)
                json_file.write(jsonMsg)
    
start = time.perf_counter()
mboxToJson(mbox, jsonFile)
finish = time.perf_counter()

print(f"Converted successfully in {finish-start:0.4f} seconds")