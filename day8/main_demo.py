table = []

# 99x99のマス目にday8/inputs.txtの内容を代入する
# with open("day8/inputs.txt") as f:
with open("day8/demo_inputs.txt") as f:
    for line in f:
        table.append(list(line.strip()))

score = 0
for x1 in range(0, 5, 1):
    for y1 in range(0, 5, 1):

        passed = True
        for x in range(0, x1, 1):
            if table[x][y1] > table[x1][y1]:
                passed = False
        for x in range(5 - 1, x1, -1):
            if table[x][y1] > table[x1][y1]:
                passed = False
        for y in range(0, y1, 1):
            if table[x1][y] > table[x1][y1]:
                passed = False
        for y in range(5 - 1, y1, -1):
            if table[x1][y] > table[x1][y1]:
                passed = False
        if passed == True:
            score += 1

print(score + 5 + 5 + 3 + 3)
