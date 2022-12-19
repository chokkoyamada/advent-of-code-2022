def migihe(x1, y1):
    visible = 0
    for x in range(x1 + 1, cell_length, 1):
        visible += 1
        if table[x][y1] >= table[x1][y1]:
            return visible
    return visible


def hidarihe(x1, y1):
    visible = 0
    for x in range(x1 - 1, -1, -1):
        visible += 1
        if table[x][y1] >= table[x1][y1]:
            return visible
    return visible


def uehe(x1, y1):
    visible = 0
    for y in range(y1 + 1, cell_length, 1):
        visible += 1
        if table[x1][y] >= table[x1][y1]:
            return visible
    return visible


def sitahe(x1, y1):
    visible = 0
    for y in range(y1 - 1, -1, -1):
        visible += 1
        if table[x1][y] >= table[x1][y1]:
            return visible
    return visible


table = []

#with open("day8/demo_inputs.txt") as f:
with open("day8/inputs.txt") as f:
    for line in f:
        table.append([int(x) for x in list(line.strip())])
cell_length = len(table[0])

max_score = 0
for x1 in range(0, cell_length, 1):
    for y1 in range(0, cell_length, 1):
        score = uehe(x1, y1) * sitahe(x1, y1) * hidarihe(x1, y1) * migihe(x1, y1)
        print(score)
        if score > max_score:
            max_score = score

print(max_score)
