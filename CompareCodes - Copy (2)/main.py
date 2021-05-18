# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filecmp
import os

file1=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code1.txt","r")
file2=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code2.txt","r")
oldCode=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code1.txt","r")
newCode=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code2.txt","r")

i=0
changedNew=0
changedOld=0
existing=0
percentChanged=0.0


def movedInNew(l1):
    global changedOld
    global existing
    j=0
    for line1 in newCode:
        j+=1
        if line1 == l1:
            print(line1)
            print("Line ",i, "moved to line: ", j)
            existing+=1
        else:
            print(line1)
            print("line ", i, "removed from old code")
            changedOld += 1
        break
    return

def addedToNew(l2):
    k = 0
    global changedNew
    global existing
    for line1 in oldCode:
        k += 1
        if line1 == l2:
            print("Line ", i, "moved to line:", k)
            existing+=1
        else:
            print("line ", i, "is new to the new code")
            changedNew += 1
        break
    return


for l1 in file1:
    i+=1
    for l2 in file2:
        if l1 == l2:
            print("Line ", i, ": ")
            print("Both the lines are same")
            existing+=1
        else:
            print("Line ", i, ": ")
            print("Code 1: ", l1)
            print("Code 2: ", l2)
            movedInNew(l1)
            addedToNew(l2)
        break

file1.close()
file2.close()

print(changedOld, "line(s) were removed")
print(changedNew, "line(s) were added")
percentChanged=(changedOld+changedNew)/i
print(i, "total lines exist")
print("percent changed", percentChanged*100)

