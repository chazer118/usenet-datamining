'''A simple test script to attempt to read from 
a local usenet database in MBOX format and count
unique addresses.
Lily Mumby
2025'''


import mailbox
import email
import csv
from collections import Counter

addresses = []

mbox = mailbox.mbox(input("Which mailbox file do you want to use?: "))
csvFile = input("Enter output file: ")

print ("Reading mailbox")

#Go through each message in the mailbox
for message in mbox: 
    #Set msg to a matching string "From"
    msg = str(message["From"])

    #Before we append this to our array, let's remove any pesky commas!
    msg = msg.replace(",", "")
    
    #Newline, return and tab characters are fucking annoying
    header_clean = msg.replace("\n", "").replace("\r", "").replace("\t", "")

    #Append this msg var to the addresses array
    addresses.append(header_clean.strip())

#This was just here to debug another function - just prints all data to a text file separated by a new line for each item.
""" with open (csvFile, 'w') as fp:
    for item in addresses:
        fp.write("%s\n" % item) 
 """
print("Writing to .csv file")

#Create CSV file, define boring stuff and then format it properly and export the data line by line :)
with open(csvFile, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                            quotechar=' ', skipinitialspace=False, escapechar='\\')
    
    #Identifies unique addresses within the mbox
    duplicates = Counter(addresses)
    writer.writerow(['Address'] + ['Count'])
    for key, value in duplicates.items():
        #Writes addr to .csv file
        writer.writerow([str(key)] + [str(value)])