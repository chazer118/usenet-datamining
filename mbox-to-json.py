# 1. It creates end of line chars at the end of each key which is not good, but easily human fixable if I can't sort it

import json
import time
import mailbox
from collections import Counter
import re

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

maskedAddresses = []

print("This will convert a Usenet .MBOX file into a .JSON file.")
mbox = mailbox.mbox(input("Enter input .mbox file: "))
jsonFile = input("Enter output .json file: ")
limit = 400

pattern1 = '\S+@\S+\.\S+'
pattern2 = r"(?:<)?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:>)?"

print ("Reading mailbox")

def parseMBOX(mbox, limit):
        count = 0

        for message in mbox: 
                if count >= limit:
                        print(f"Output has been limited to {limit} messages.")
                        break

                #Set msg to a matching string "From"
                msgFrom = str(message.get("From", ""))
                msgDate = str(message.get("Date"))
                msgSubject = str(message.get("Subject"))
                msgContent = str(message.get_payload())

                #Remove commas
                #msgFrom = msgFrom.replace(",", "")
                #msgDate = msgDate.replace(",", "")
                #msgContent = msgContent.replace(",", "")

                mailAddresses = re.findall(pattern2, msgContent)

                try:
                        for i in range(len(mailAddresses)):
                                split = mailAddresses[i].split('@')
                                usernameMasked = 'x'*(len(split[0]))
                                maskedEmail = (usernameMasked + "@" + split[1])
                                maskedAddresses.append(maskedEmail)

                                msgContent = msgContent.replace(mailAddresses[i], maskedEmail)
                except:
                        print("An error occurred whilst trying to mask email addresses")
                        pass
        
                #Append all to the corresponding array
                addresses.append(msgFrom)
                date.append(msgDate)
                subjectArray.append(msgSubject)
                messageArray.append(msgContent.replace(" \n", "\n").replace(" \n\n", "\n\n"))

                count += 1

                #Debugging stuff
                print(msgContent)
                print("Found: " + str(mailAddresses))
                print("Masked: " + str(maskedAddresses))
                input("Press enter to continue...")

        #\n is added once it has been appended to an array so we need to work here
        #msg_clean = msgContent.replace(" \n", "\n")
        
def writeToJson(jsonFile):
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
parseMBOX(mbox, limit)
#writeToJson(jsonFile)
finish = time.perf_counter()

print(f"Converted successfully in {finish-start:0.4f} seconds")