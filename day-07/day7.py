### day 7
## edit line 4

f = open(r'C:\Users\nguye\Downloads\day7input.txt', "r")

instructions = f.read().split('\n')

instructions = [instruction.split(" ") for instruction in instructions]

class Wire:

    def __init__(self, name) -> None:
        self.name = name
        self.input = []
        self.operator = ""
        self.value = None
        self.calculated = False

class Operation:
     
     def __init__(self, name) -> None:
        self.name = name

setOfWires = {}
setOfAction = [Operation("ASSIGN"), Operation("NOT"), Operation("AND"), Operation("OR"), Operation("LSHIFT"), Operation("RSHIFT")]

def buildGraph(instruction):

    if len(instruction) == 3:
        val = instruction[0]
        des = instruction[-1]
        des.input.append(val)
        des.operator = setOfAction[0]


    if len(instruction) == 4:
        source = instruction[1]
        des = instruction[-1]
        des.input.append(source)
        des.operator = setOfAction[1]

    if len(instruction) == 5:
        if instruction[1] == "AND":
            wire1 = instruction[0]
            wire2 = instruction[2]
            des = instruction[-1]
            des.input.append(wire1)
            des.input.append(wire2)
            des.operator = setOfAction[2]

        if instruction[1] == "OR":
            wire1 = instruction[0]
            wire2 = instruction[2]
            des = instruction[-1]
            des.input.append(wire1)
            des.input.append(wire2)
            des.operator = setOfAction[3]

        if instruction[1] == "LSHIFT":
            wire1 = instruction[0]
            shiftBits = instruction[2]
            des = instruction[-1]
            des.input.append(wire1)
            des.input.append(shiftBits)
            des.operator = setOfAction[4]

        if instruction[1] == "RSHIFT":
            wire1 = instruction[0]
            shiftBits = instruction[2]
            des = instruction[-1]
            des.input.append(wire1)
            des.input.append(shiftBits)
            des.operator = setOfAction[5]


for instruction in instructions:
    currentInstruction = instruction
    if len(instruction) == 3:
        val = currentInstruction[0]
        des = currentInstruction[-1]

        if val.isnumeric():
            instruction[0] = int(val)
        else:
            if val not in setOfWires:
                setOfWires[val] = Wire(val)
            instruction[0] = setOfWires[val]

        if des not in setOfWires:
            setOfWires[des] = Wire(des)

        instruction[-1] = setOfWires[des]

    if len(currentInstruction) == 4:
        source = currentInstruction[1]
        des = currentInstruction[-1]

        if source not in setOfWires:
            setOfWires[source] = Wire(source)
        if des not in setOfWires:
            setOfWires[des] = Wire(des)

        instruction[1] = setOfWires[source]
        instruction[-1] = setOfWires[des]
        
    if len(currentInstruction) == 5:
        if currentInstruction[1] == "AND":
            wire1 = currentInstruction[0]
            wire2 = currentInstruction[2]
            des = currentInstruction[-1]

            if wire1.isnumeric():
                instruction[0] = int(wire1)
            else:
                if wire1 not in setOfWires:
                    setOfWires[wire1] = Wire(wire1)
                instruction[0] = setOfWires[wire1]

            if wire2.isnumeric():
                instruction[2] = int(wire2)
            else:
                if wire2 not in setOfWires:
                    setOfWires[wire2] = Wire(wire2)
                instruction[2] = setOfWires[wire2]

            if des not in setOfWires:
                setOfWires[des] = Wire(des)
            instruction[-1] = setOfWires[des]

        if currentInstruction[1] == "OR":
            wire1 = currentInstruction[0]
            wire2 = currentInstruction[2]
            des = currentInstruction[-1]

            if wire1.isnumeric():
                instruction[0] = int(wire1)
            else:
                if wire1 not in setOfWires:
                    setOfWires[wire1] = Wire(wire1)
                instruction[0] = setOfWires[wire1]

            if wire2.isnumeric():
                instruction[2] = int(wire2)
            else:
                if wire2 not in setOfWires:
                    setOfWires[wire2] = Wire(wire2)
                instruction[2] = setOfWires[wire2]

            if des not in setOfWires:
                setOfWires[des] = Wire(des)
            instruction[-1] = setOfWires[des]

        if currentInstruction[1] == "LSHIFT":
            wire1 = currentInstruction[0]
            shiftBits = int(currentInstruction[2])
            des = currentInstruction[-1]

            if wire1 not in setOfWires:
                setOfWires[wire1] = Wire(wire1)

            if des not in setOfWires:
                setOfWires[des] = Wire(des)

            instruction[0] = setOfWires[wire1]
            instruction[2] = shiftBits
            instruction[-1] = setOfWires[des]

        if currentInstruction[1] == "RSHIFT":
            wire1 = currentInstruction[0]
            shiftBits = int(currentInstruction[2])
            des = currentInstruction[-1]

            if wire1 not in setOfWires:
                setOfWires[wire1] = Wire(wire1)

            if des not in setOfWires:
                setOfWires[des] = Wire(des)

            instruction[0] = setOfWires[wire1]
            instruction[2] = shiftBits
            instruction[-1] = setOfWires[des]

for instruction in instructions:
    buildGraph(instruction)

def findValue(value) -> int:
    if type(value) == Wire:
        return calculateValue(value)
    return int(value)

def calculateValue(currentWire: Wire):
    if currentWire.calculated == False:
        if len(currentWire.input) == 1:
            if currentWire.operator == setOfAction[0]:
                currentWire.value = findValue(currentWire.input[0])
                currentWire.calculated = True
            elif currentWire.operator == setOfAction[1]:
                currentWire.value = ~findValue(currentWire.input[0])
                currentWire.calculated = True

        if len(currentWire.input) == 2:
            if currentWire.operator == setOfAction[2]:
                currentWire.value = findValue(currentWire.input[0]) & findValue(currentWire.input[1])
                currentWire.calculated = True
            
            if currentWire.operator == setOfAction[3]:
                currentWire.value = findValue(currentWire.input[0]) | findValue(currentWire.input[1])
                currentWire.calculated = True

            if currentWire.operator == setOfAction[4]:
                currentWire.value = findValue(currentWire.input[0]) << findValue(currentWire.input[1])
                currentWire.calculated = True

            if currentWire.operator == setOfAction[5]:
                currentWire.value = findValue(currentWire.input[0]) >> findValue(currentWire.input[1])
                currentWire.calculated = True

    return currentWire.value

print(calculateValue(setOfWires["a"]))