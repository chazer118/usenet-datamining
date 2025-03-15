""" Locate all addresses and their respective newsgroups from an mbox file. 

To-Do:
- write down the newsgroups of each address, ensure there is no difference if it is a duplicate?

"""

import mailbox
import email
import csv
from collections import Counter
from string import whitespace

addresses = []
crosspost = {}

def ngParser(message):

    msg = str(message["From"])

    #Before we append this to our array, let's remove any pesky commas!
    msg = msg.replace(",", "")
    
    #Newline, return and tab characters are fucking annoying
    header_clean = msg.replace("\n", "").replace("\r", "").replace("\t", "")

    #Append this msg var to the addresses array
    addresses.append(header_clean.strip())

    ng = str(message["Newsgroups"]).split(",")

    ngSorted = sorted(ng)

    ngList = ";".join(ngSorted)

    crosspost[msg] = ngList

def main():
    mbox = mailbox.mbox(input("Which mailbox file do you want to use?: "))
    csvFile = input("Enter output file 1: ")
    csvFile2 = input("Enter output file 2: ")

    print ("Reading mailbox")

    for message in mbox: 
        #Set msg to a matching string "From"
        ngParser(message)
        
    print("Writing to .csv file")

    #Create CSV file, define boring stuff and then format it properly and export the data line by line :)
    with open(csvFile, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                                quotechar=' ', skipinitialspace=False, escapechar='\\')

        writer.writerow(['Address'] + ['Newsgroups'])
        for key, value in crosspost.items():
            #Writes only the address to .csv file
            writer.writerow([str(key)] + [str(value)])


    #SHOULD create a second csv file that counts the occurance of each newsgroup in this mbox so we know which groups were often crossposted.
    with open(csvFile2, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                                quotechar=' ', skipinitialspace=False, escapechar='\\')

        #Identify unique NGs 
        duplicates = Counter(crosspost)
        writer.writerow(['Newsgroups'] + ['Count'])
        for key, value in duplicates.items():
            #Writes only the address to .csv file
            writer.writerow([str(key)] + [str(value)])

main()