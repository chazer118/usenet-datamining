# usenet-datamining
Datamining tools in Python targeted at exploring archival data from the USENET

**fromedit2.py** is needed to workaround an issue with Python mailbox module mis-reading Usenet
Historical Collection mbox files. Identifies all instances of "from"
that are *not* in the header, changes them to "xFrom," and writes
them to a new mailbox file. (Python2) - by Dame Avery-Griff

**mbox-countaddresses.py** is a simple script to read from 
a local usenet database stored in MBOX format and count the
amount of unique addresses. Prints out to .csv file.

**mbox-crosspost.py** reads an MBOX file and then prints out a list of each sender
and their respective Newsgroups into a .csv file - retrieved from the MBOX header info.

**mbox-to-csv.py** takes a MBOX file as an input, reads the email address, date and content
of each message and outputs it to a .csv file (handy for data analysis!)

**csv-to-json.py** quick way to convert csv data to .json format. not great for my application 
but this does work

**csv-to-json2.py** THIS script does what I need it to do. Converts .csv data to .json format
and gets Max's dict function to accept the data. nerds i dont even know if json is the best
way to store and retrieve this data, but i'm down a rabbit hole and this works best for me.



