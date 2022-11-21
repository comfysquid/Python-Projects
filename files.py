# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:


# python files.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
# BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
# SAT, 05 JAN 2008 09:14:16 -0500

# i = input("Enter your filename: ")
# fhand = open(i)
# for line in fhand:
#     line = line.rstrip()
#     print(line.upper())

# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475

error = "Error encountered"


def loop():
    count = 0
    total = 0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence: "):
            count = count + 1
            colpos = line.find(":")
            number = line[colpos+1:].strip()
            SPAM_C = float(number)
            total = total + SPAM_C
    average = total/count
    print("Average spam confidence", average)


fname = input('Enter the file name: ')
try:
    if fname == "na na boo boo":
        print("You idiot!")
    else:
        fhand = open(fname)
        loop()
except:
    print(error)
    quit()
