def uekara(x1, y1):
    passed = True
    for x in range(0, x1, 1):
        if table[x][y1] >= table[x1][y1]:
            return False
    return passed


def sitakara(x1, y1):
    passed = True
    for x in range(cell_length - 1, x1, -1):
        if table[x][y1] >= table[x1][y1]:
            return False
    return passed


def hidarikara(x1, y1):
    passed = True
    for y in range(0, y1, 1):
        if table[x1][y] >= table[x1][y1]:
            return False
    return passed


def migikara(x1, y1):
    passed = True
    for y in range(cell_length - 1, y1, -1):
        if table[x1][y] >= table[x1][y1]:
            return False
    return passed


table = []

with open("day8/inputs.txt") as f:
    for line in f:
        table.append([int(x) for x in list(line.strip())])
cell_length = len(table[0])

score = 0
for x1 in range(0, cell_length, 1):
    for y1 in range(0, cell_length, 1):
        print(table[x1][y1])
        if (
            uekara(x1, y1) == True
            or sitakara(x1, y1) == True
            or hidarikara(x1, y1) == True
            or migikara(x1, y1) == True
        ):
            score += 1

print(score)
