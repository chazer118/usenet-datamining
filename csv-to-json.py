#FIELD LIMIT????

import csv
import json
import time
import sys
import ctypes as ct

jsonArray = []
csvFile = input("Enter input .csv file: ")
jsonFile = input("Enter output .json file: ")
csv.field_size_limit(int(ct.c_ulong(-1).value // 2))
limit1 = csv.field_size_limit()

def csvToJson(csvFile, jsonFile):
    with open(csvFile) as csv_file:
        csvReader = csv.DictReader(csv_file)

        for row in csvReader:
            #add to our json array
            jsonArray.append(row)

        with open (jsonFile, 'w') as json_file:
            jsonString = json.dumps(jsonArray, indent=4)
            json_file.write(jsonString)

start = time.perf_counter()
csvToJson(csvFile, jsonFile)
finish = time.perf_counter()

print(f"Converted successfully in {finish-start:0.4f} seconds")