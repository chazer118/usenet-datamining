#2 problems:
# 1. It creates end of line chars at the end of each key which is not good, but easily human fixable if I can't sort it
# 2. I need to integrate text formatting. So new lines, etc work. If this doesnt work then this script is pointless.

import csv
import json
import time
import sys
import ctypes as ct

jsonArray = []
senderArray = []
dateArray = []
msgArray = []

senderData = {}
dateData = {}
msgData = {}

csvFile = input("Enter input .csv file: ")
jsonFile = input("Enter output .json file: ")
csv.field_size_limit(int(ct.c_ulong(-1).value // 2))
limit1 = csv.field_size_limit()

def csvToJson(csvFile, jsonFile):
    with open(csvFile) as csv_file:
        csvReader = csv.DictReader(csv_file)

        for col in csvReader:
            #add to our json array
            senderArray.append(col['Sender'])
            dateArray.append(col['Date'])
            msgArray.append(col['Message'])

        with open (jsonFile, 'w') as json_file:
            #
            """ print(senderArray)
            print(dateArray)
            print(msgArray) """
            #json_file.write(jsonString)

            senderData['Sender'] = senderArray
            dateData['Date'] = dateArray
            msgData['Message'] = msgArray

            jsonSender = json.dumps(senderData, indent=4)
            jsonDate = json.dumps(dateData, indent=4)
            jsonMsg = json.dumps(msgData, indent=4)
            
            json_file.write(jsonSender)

start = time.perf_counter()
csvToJson(csvFile, jsonFile)
finish = time.perf_counter()

print(f"Converted successfully in {finish-start:0.4f} seconds")