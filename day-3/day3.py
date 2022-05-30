user = input()
n = len(user)

#part1
seen = [[0 for x in range(n)] for y in range(n)] 
r,c=0,0
for char in user:
  if char == ">":
    c+=1
  elif char == "<":
    c-=1
  elif char == "^":
    r+=1
  elif char == "v":
    r-=1
  seen[r][c]+=1
house = 0

for r in range(n):
  for c in range(n):
    if seen[r][c]!=0:
      house+=1
  
print(house)

#part2
seen1 = [[0 for x in range(n)] for y in range(n)] 
seen2 = [[0 for x in range(n)] for y in range(n)]

r1,c1=0,0
r2,c2=0,0
for i in range(n):
  #copy paste not good but i'm lazy
  if i % 2==0:
    if user[i] == ">":
      c1+=1
    elif user[i] == "<":
      c1-=1
    elif user[i] == "^":
      r1+=1
    elif user[i] == "v":
      r1-=1
    seen1[r1][c1]+=1
  else:
    if user[i] == ">":
      c2+=1
    elif user[i]== "<":
      c2-=1
    elif user[i] == "^":
      r2+=1
    elif user[i] == "v":
      r2-=1
    seen2[r2][c2]+=1

house = 0

for r in range(n):
  for c in range(n):
    if seen1[r][c]!=0 or seen2[r][c]!=0:
      house+=1
  
print(house)