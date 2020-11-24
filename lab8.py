
###dylan wong
##lab 8


##ask for input
text = input("enter a file name")
file = open(text,"r")
##loop numbering format using readlines
###ask what number to start example 0,1,2,3 or 1,2,3,4
count = int(input("enter a number to start at a certain line number"))
for line in file.readlines():
    print(str(count) + ": " + line)
    count = count + 1

