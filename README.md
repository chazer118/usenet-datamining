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


