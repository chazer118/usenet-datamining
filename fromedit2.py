'''
Workaround for issue with Python mailbox module mis-reading Usenet
Historical Collection mbox files. Identifies all instances of "from"
that are *not* in the header, changes them to "xFrom," and writes
them to a new mailbox.

Originally by Avery Dame Griff (2016)
'''

batch = []

box = raw_input("What is the mailbox you want to work with? ")
newbox = raw_input("What is the name of the file it should output to? ")

i = 0

with open(box, 'rb') as original, open(newbox, 'wb') as new:
    for line in original:
        i+=1
        if line.startswith("From "):
            print ("%s: %s" % (i, line))
            if len(line) > 6:
                num = line[6]
                if num.isdigit():
                    #If the char at index 6 of the string IS a number, then it must be part of a header to add this to our file without any changes
                    batch.append(line)
                else:
                    #If the char ISNT a number then it must be changed to xFrom to avoid confusing our other scripts.
                    x = line.replace("From ", "xFrom ")
                    batch.append(x)
            else:
                x = line.replace("From ", "xFrom ")
                batch.append(x)
        else:
            batch.append(line)

    for line in batch:
        #Writes edited mailbox to new file
        new.writelines(line)

print "Editing complete!"
