from ast import literal_eval
f = open("/Users/hknguyen20/OneDrive - VINACADEMY LLC/COLLEGE/A A VinUni/YEAR 2/Spring 2022/Algo Design/aoc2015/Day8.txt", "r")
lines = f.read().split('\n')
f.close()
diff1 = diff2 = 0
for l in lines:
    diff1 += len(l) - len(literal_eval(l))
    diff2 += 2 + l.count('"') + l.count('\\')
#p1
print(diff1)
#p2
print(diff2)