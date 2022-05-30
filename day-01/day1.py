user = input()
#part 1
level = 0
for char in user:
    if char == "(":
        level+=1
    elif char == ")":
        level-=1
print(level)

#part2
level=0
for char in range(len(user)):
    if user[char] == "(":
        level+=1
    elif user[char] == ")":
        level-=1
    if(level == -1):
      print(char+1)
      break