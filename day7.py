# Note that in this problem, for part 1, we use the original input but in part 2, we use the value of a to replace the value in the 5th line 
# from the bottom that is assigned to b and then rerun the whole program

instructions = """bn RSHIFT 2 -> bo
lf RSHIFT 1 -> ly
fo RSHIFT 3 -> fq
cj OR cp -> cq
fo OR fz -> ga
t OR s -> u
lx -> a
NOT ax -> ay
he RSHIFT 2 -> hf
lf OR lq -> lr
lr AND lt -> lu
dy OR ej -> ek
1 AND cx -> cy
hb LSHIFT 1 -> hv
1 AND bh -> bi
ih AND ij -> ik
c LSHIFT 1 -> t
ea AND eb -> ed
km OR kn -> ko
NOT bw -> bx
ci OR ct -> cu
NOT p -> q
lw OR lv -> lx
NOT lo -> lp
fp OR fv -> fw
o AND q -> r
dh AND dj -> dk
ap LSHIFT 1 -> bj
bk LSHIFT 1 -> ce
NOT ii -> ij
gh OR gi -> gj
kk RSHIFT 1 -> ld
lc LSHIFT 1 -> lw
lb OR la -> lc
1 AND am -> an
gn AND gp -> gq
lf RSHIFT 3 -> lh
e OR f -> g
lg AND lm -> lo
ci RSHIFT 1 -> db
cf LSHIFT 1 -> cz
bn RSHIFT 1 -> cg
et AND fe -> fg
is OR it -> iu
kw AND ky -> kz
ck AND cl -> cn
bj OR bi -> bk
gj RSHIFT 1 -> hc
iu AND jf -> jh
NOT bs -> bt
kk OR kv -> kw
ks AND ku -> kv
hz OR ik -> il
b RSHIFT 1 -> v
iu RSHIFT 1 -> jn
fo RSHIFT 5 -> fr
be AND bg -> bh
ga AND gc -> gd
hf OR hl -> hm
ld OR le -> lf
as RSHIFT 5 -> av
fm OR fn -> fo
hm AND ho -> hp
lg OR lm -> ln
NOT kx -> ky
kk RSHIFT 3 -> km
ek AND em -> en
NOT ft -> fu
NOT jh -> ji
jn OR jo -> jp
gj AND gu -> gw
d AND j -> l
et RSHIFT 1 -> fm
jq OR jw -> jx
ep OR eo -> eq
lv LSHIFT 15 -> lz
NOT ey -> ez
jp RSHIFT 2 -> jq
eg AND ei -> ej
NOT dm -> dn
jp AND ka -> kc
as AND bd -> bf
fk OR fj -> fl
dw OR dx -> dy
lj AND ll -> lm
ec AND ee -> ef
fq AND fr -> ft
NOT kp -> kq
ki OR kj -> kk
cz OR cy -> da
as RSHIFT 3 -> au
an LSHIFT 15 -> ar
fj LSHIFT 15 -> fn
1 AND fi -> fj
he RSHIFT 1 -> hx
lf RSHIFT 2 -> lg
kf LSHIFT 15 -> kj
dz AND ef -> eh
ib OR ic -> id
lf RSHIFT 5 -> li
bp OR bq -> br
NOT gs -> gt
fo RSHIFT 1 -> gh
bz AND cb -> cc
ea OR eb -> ec
lf AND lq -> ls
NOT l -> m
hz RSHIFT 3 -> ib
NOT di -> dj
NOT lk -> ll
jp RSHIFT 3 -> jr
jp RSHIFT 5 -> js
NOT bf -> bg
s LSHIFT 15 -> w
eq LSHIFT 1 -> fk
jl OR jk -> jm
hz AND ik -> im
dz OR ef -> eg
1 AND gy -> gz
la LSHIFT 15 -> le
br AND bt -> bu
NOT cn -> co
v OR w -> x
d OR j -> k
1 AND gd -> ge
ia OR ig -> ih
NOT go -> gp
NOT ed -> ee
jq AND jw -> jy
et OR fe -> ff
aw AND ay -> az
ff AND fh -> fi
ir LSHIFT 1 -> jl
gg LSHIFT 1 -> ha
x RSHIFT 2 -> y
db OR dc -> dd
bl OR bm -> bn
ib AND ic -> ie
x RSHIFT 3 -> z
lh AND li -> lk
ce OR cd -> cf
NOT bb -> bc
hi AND hk -> hl
NOT gb -> gc
1 AND r -> s
fw AND fy -> fz
fb AND fd -> fe
1 AND en -> eo
z OR aa -> ab
bi LSHIFT 15 -> bm
hg OR hh -> hi
kh LSHIFT 1 -> lb
cg OR ch -> ci
1 AND kz -> la
gf OR ge -> gg
gj RSHIFT 2 -> gk
dd RSHIFT 2 -> de
NOT ls -> lt
lh OR li -> lj
jr OR js -> jt
au AND av -> ax
0 -> c
he AND hp -> hr
id AND if -> ig
et RSHIFT 5 -> ew
bp AND bq -> bs
e AND f -> h
ly OR lz -> ma
1 AND lu -> lv
NOT jd -> je
ha OR gz -> hb
dy RSHIFT 1 -> er
iu RSHIFT 2 -> iv
NOT hr -> hs
as RSHIFT 1 -> bl
kk RSHIFT 2 -> kl
b AND n -> p
ln AND lp -> lq
cj AND cp -> cr
dl AND dn -> do
ci RSHIFT 2 -> cj
as OR bd -> be
ge LSHIFT 15 -> gi
hz RSHIFT 5 -> ic
dv LSHIFT 1 -> ep
kl OR kr -> ks
gj OR gu -> gv
he RSHIFT 5 -> hh
NOT fg -> fh
hg AND hh -> hj
b OR n -> o
jk LSHIFT 15 -> jo
gz LSHIFT 15 -> hd
cy LSHIFT 15 -> dc
kk RSHIFT 5 -> kn
ci RSHIFT 3 -> ck
at OR az -> ba
iu RSHIFT 3 -> iw
ko AND kq -> kr
NOT eh -> ei
aq OR ar -> as
iy AND ja -> jb
dd RSHIFT 3 -> df
bn RSHIFT 3 -> bp
1 AND cc -> cd
at AND az -> bb
x OR ai -> aj
kk AND kv -> kx
ao OR an -> ap
dy RSHIFT 3 -> ea
x RSHIFT 1 -> aq
eu AND fa -> fc
kl AND kr -> kt
ia AND ig -> ii
df AND dg -> di
NOT fx -> fy
k AND m -> n
bn RSHIFT 5 -> bq
km AND kn -> kp
dt LSHIFT 15 -> dx
hz RSHIFT 2 -> ia
aj AND al -> am
cd LSHIFT 15 -> ch
hc OR hd -> he
he RSHIFT 3 -> hg
bn OR by -> bz
NOT kt -> ku
z AND aa -> ac
NOT ak -> al
cu AND cw -> cx
NOT ie -> if
dy RSHIFT 2 -> dz
ip LSHIFT 15 -> it
de OR dk -> dl
au OR av -> aw
jg AND ji -> jj
ci AND ct -> cv
dy RSHIFT 5 -> eb
hx OR hy -> hz
eu OR fa -> fb
gj RSHIFT 3 -> gl
fo AND fz -> gb
1 AND jj -> jk
jp OR ka -> kb
de AND dk -> dm
ex AND ez -> fa
df OR dg -> dh
iv OR jb -> jc
x RSHIFT 5 -> aa
NOT hj -> hk
NOT im -> in
fl LSHIFT 1 -> gf
hu LSHIFT 15 -> hy
iq OR ip -> ir
iu RSHIFT 5 -> ix
NOT fc -> fd
NOT el -> em
ck OR cl -> cm
et RSHIFT 3 -> ev
hw LSHIFT 1 -> iq
ci RSHIFT 5 -> cl
iv AND jb -> jd
dd RSHIFT 5 -> dg
as RSHIFT 2 -> at
NOT jy -> jz
af AND ah -> ai
1 AND ds -> dt
jx AND jz -> ka
da LSHIFT 1 -> du
fs AND fu -> fv
jp RSHIFT 1 -> ki
iw AND ix -> iz
iw OR ix -> iy
eo LSHIFT 15 -> es
ev AND ew -> ey
ba AND bc -> bd
fp AND fv -> fx
jc AND je -> jf
et RSHIFT 2 -> eu
kg OR kf -> kh
iu OR jf -> jg
er OR es -> et
fo RSHIFT 2 -> fp
NOT ca -> cb
bv AND bx -> by
u LSHIFT 1 -> ao
cm AND co -> cp
y OR ae -> af
bn AND by -> ca
1 AND ke -> kf
jt AND jv -> jw
fq OR fr -> fs
dy AND ej -> el
NOT kc -> kd
ev OR ew -> ex
dd OR do -> dp
NOT cv -> cw
gr AND gt -> gu
dd RSHIFT 1 -> dw
NOT gw -> gx
NOT iz -> ja
1 AND io -> ip
NOT ag -> ah
b RSHIFT 5 -> f
NOT cr -> cs
kb AND kd -> ke
jr AND js -> ju
cq AND cs -> ct
il AND in -> io
NOT ju -> jv
du OR dt -> dv
dd AND do -> dq
b RSHIFT 2 -> d
jm LSHIFT 1 -> kg
NOT dq -> dr
bo OR bu -> bv
gk OR gq -> gr
he OR hp -> hq
NOT h -> i
hf AND hl -> hn
gv AND gx -> gy
x AND ai -> ak
bo AND bu -> bw
hq AND hs -> ht
hz RSHIFT 1 -> is
gj RSHIFT 5 -> gm
g AND i -> j
gk AND gq -> gs
dp AND dr -> ds
b RSHIFT 3 -> e
gl AND gm -> go
gl OR gm -> gn
y AND ae -> ag
hv OR hu -> hw
46065 -> b
ab AND ad -> ae
NOT ac -> ad
1 AND ht -> hu
NOT hn -> ho"""

instructions = instructions.split("\n")

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



# stackGraph = []

# def spanGraph(finalNode : Wire):
#     queue = []
#     visitedNode  = {}
#     visitedNode[finalNode.name] = True
#     queue.append(finalNode)

#     while len(queue) > 0:
#         currentNode = queue.pop(0)
#         print("currentNode is: ", currentNode.name)
#         stackGraph.append(currentNode)
#         for _ in currentNode.input:
#             stackGraph.append(_)
#             if type(_) == Wire:
#                 if _.name not in visitedNode:
#                     queue.append(_)
#                     visitedNode[_.name] = True
#         stackGraph.append(currentNode.operator)

#         # for _ in stackGraph:
#         #     if type(_) == Wire:
#         #         print(_.name)
#         #     else:
#         #         print(_)

# spanGraph(setOfWires["a"])

# # for _ in stackGraph:
# #     if type(_) == Wire:
# #         print(_.name)
# #     elif type(_) == Operation:
# #         print(_.name)
# #     else:
# #         print(_)



# while len(stackGraph) > 0:
#     frontElement = stackGraph.pop()
#     if type(frontElement) == Operation:
#         if frontElement.name == "ASSIGN":
#             source = stackGraph.pop()
#             des = stackGraph.pop()

#             if type(source) == Wire:
#                 des.value = source.value
#             else:
#                 des.value = source
            
#         if frontElement.name == "NOT":
#             source = stackGraph.pop()
#             des = stack.pop()

#             if type(source) == Wire:
#                 des.value = ~source.value
#             else:
#                 des.value = ~source
            
#         if frontElement.name == "AND":
#             source1 = stackGraph.pop()
#             source2 = stackGraph.pop()
#             des = stackGraph.pop()

#             if type(source1) == Wire:
#                 val1 = source1.value
#             else:
#                 val1 = source1

#             if type(source2) == Wire:
#                 val2 = source2.value
#             else:
#                 val2 = source2

#             des.value = val1 & val2

#         if frontElement.name == "OR":
#             source1 = stackGraph.pop()
#             source2 = stackGraph.pop()
#             des = stackGraph.pop()

#             if type(source1) == Wire:
#                 val1 = source1.value
#             else:
#                 val1 = source1

#             if type(source2) == Wire:
#                 val2 = source2.value
#             else:
#                 val2 = source2

#             des.value = val1 & val2

#         if frontElement.name == "LSHIFT":
#             source1 = stackGraph.pop()
#             source2 = stackGraph.pop()
#             des = stackGraph.pop()

#             if type(source1) == Wire:
#                 val1 = source1.value
#             else:
#                 val1 = source1

#             if type(source2) == Wire:
#                 val2 = source2.value
#             else:
#                 val2 = source2

#             des.value = val1 << val2

#         if frontElement.name == "RSHIFT":
#             source1 = stackGraph.pop()
#             source2 = stackGraph.pop()
#             des = stackGraph.pop()

#             if type(source1) == Wire:
#                 val1 = source1.value
#             else:
#                 val1 = source1

#             if type(source2) == Wire:
#                 val2 = source2.value
#             else:
#                 val2 = source2

#             des.value = val1 >> val2
