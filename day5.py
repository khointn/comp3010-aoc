from itertools import count
from tokenize import String
from turtle import Turtle


inputStrings = input()


vowels = {}
vowels["a"] = 0
vowels["u"] = 0
vowels["e"] = 0
vowels["i"] = 0
vowels["o"] = 0



def countVowels(string):

    counter = 0

    for index in range(len(string)):
        if string[index] in vowels:
            counter+=1

        if index <= len(string) - 2:
            if string[index] == "a" and string[index+1] == "b":
                return False
            
            if string[index] == "c" and string[index+1] == "d":
                return False

            if string[index] == "p" and string[index+1] == "q":
                return False

            if string[index] == "x" and string[index+1] == "y":
                return False
    
    if counter < 3:
        return False

    return True
         
def check2SequenceChar(string):
    for index in range(len(string)):
        if index <= len(string)-2:
            if string[index] == string[index+1]:
                return True

    return False


strings = inputStrings.split("\n")

counter = 0

for string in strings:
    if countVowels(string) and check2SequenceChar(string):
        counter+=1

print(counter)

#---Part 2---#

def checkDuplicate2Strings(string):
    StringsOf2 = {}

    hasDuplicate2Strings  = False
    hasInterleaveStrings  = False

    for i in range(len(string)-1):
        currentString = (string[i] + string[i+1]) 

        if (string[i] + string[i+1]) in StringsOf2 and (i >= StringsOf2[string[i:i+2]]+2):
            hasDuplicate2Strings = True
 
        elif (string[i] + string[i+1]) not in StringsOf2:
            StringsOf2[string[i:i+2]] = i
        
        if i <= len(string)-3:
            if string[i] == string[i+2]:
                hasInterleaveStrings = True

    return hasDuplicate2Strings and hasInterleaveStrings

counter = 0
for string in strings:
    if checkDuplicate2Strings(string):
        counter += 1

print(counter)

checkDuplicate2Strings("uurcxstgmygtbstg")