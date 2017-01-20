# You can write any code you like in the window below. There are three files loaded and ready for you to open if you want to do file processing: "mbox-short.txt", "romeo.txt", and "words.txt".

fh = open("romeo.txt", "r")

fh2 = open("mbox-short.txt", "r")

fh3 = open("words.txt", "r")

count = 0
for line in fh:
    print line.strip()
    count = count + 1

print count,"Lines"


count1 = 0
for line in fh2:
    print line.strip()
    count1 = count1 + 1

print count1,"Lines"


count2 = 0
for line in fh3:
    print line.strip()
    count2 = count2 + 1

print count2,"Lines"