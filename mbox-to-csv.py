""" A script to convert a .mbox file to a .csv file which may (?) be useful! """
""" To-do:
- write most of the mailbox sorting into their own functions """

import mailbox
import email
import csv
from collections import Counter

addresses = []
date = []
messageArray = []
messageID = []

print("This will convert a Usenet .MBOX file into a .CSV file.")
mbox = mailbox.mbox(input("Which mailbox file do you want to use?: "))
csvFile = input("Enter output .csv file: ")

print ("Reading mailbox")

#Go through each message in the mailbox
for message in mbox: 
    #Set msg to a matching string "From"
    msgFrom = str(message.get("From", ""))
    msgDate = str(message.get("Date"))
    msgContent = str(message.get_payload())

    #Remove commas
    msgFrom = msgFrom.replace(",", "")
    msgDate = msgDate.replace(",", "")
    msgContent = msgContent.replace(",", "")

    msg_clean = msgContent.replace("\n", "").replace("\r", "").replace("\t", "")

    #Append to the corresponding array
    addresses.append(msgFrom)
    date.append(msgDate)
    messageArray.append(msg_clean.strip())

""" with open (csvFile, 'w') as fp:
    for item in addresses:
        fp.write("%s\n" % item) """

#Create CSV file, define boring stuff and then format it properly and export the data line by line :)
with open(csvFile, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                            quotechar=' ', skipinitialspace=False, escapechar='\\')
    
    count = Counter(addresses)
    writer.writerow(['Sender'] + ['Date'] + ['Message'])
    for i in range(len(date)):
        #Writes addr to .csv file
        writer.writerow([addresses[i], date[i], messageArray[i]])

# Getting there... I think. However msg content is now overflowing into address columns.
# Is this specific to numbers or is this how the data is outputted?
# Is get_payload() the correct function to call?
# TAB AND CARRIAGE RETURN!