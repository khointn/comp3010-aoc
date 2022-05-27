import numpy as np 

grid = np.zeros((1000, 1000))

instructions = """"""

instructions = instructions.split("\n")

def convert(x, action):
    if action == "on":
        return x+1
    if action == "off":
        return max(0, x-1)
    return x+2

convert_vect = np.vectorize(convert)

for instruction in instructions:
    temp = instruction.split(" through ")[1]
    x2, y2 = temp.split(",")
    x2 = int(x2)
    y2 = int(y2)

    temp = instruction.split(" ")[-3]
    x1, y1 = temp.split(",")
    x1 = int(x1)
    y1 = int(y1)

    if len(instruction.split(" ")) ==  5:
        action = instruction.split(" ")[1]
    else:
        action = instruction.split(" ")[0]

    if action == "on":
        grid[x1:x2+1,y1:y2+1] = convert_vect(grid[x1:x2+1,y1:y2+1], "on")

    if action == "off":
        grid[x1:x2+1,y1:y2+1] = convert_vect(grid[x1:x2+1,y1:y2+1], "off")

    if action == "toggle":
        grid[x1:x2+1,y1:y2+1] = convert_vect(grid[x1:x2+1,y1:y2+1], "toggle")

onesVector = np.ones((1000, 1))

print(np.dot(np.dot(grid, onesVector).T, onesVector))



 
