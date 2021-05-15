# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filecmp
import os

file1=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code1.txt","r")
file2=open("C:\\USERS\\Jordan Bavlnka\\PycharmProjects\\CompareCodes\\Codes\\Code2.txt","r")

i=0

for l1 in file1:
    i+=1
    for l2 in file2:
        if l1 == l2:
            print("Line ", i, ": ")
            print("Both the lines are same")
        else:
            print("Line ", i, ": ")
            print("Code 1: ", l1)
            print("Code 2: ", l2)
        break

file1.close()
file2.close()