import hashlib
  
# initializing string
str2hash = input()

outputString = "1111111"

i = 0

while True:
    # encoding GeeksforGeeks using encode()
    # then sending to md5()
    outputString = str(hashlib.md5((str2hash + str(i)).encode()).hexdigest())
    if outputString[0:6] == "000000":
        print(i)
        break
    i+=1

