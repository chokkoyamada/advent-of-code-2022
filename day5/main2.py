# inputs1.txt をdequeでスタックにする

from collections import deque


if __name__ == "__main__":
    q = [[] for _ in range(9)]
    inputs = open("day5/inputs1.txt", "r").readlines()
    for index, line in enumerate(inputs):
        if index > 7:
            break
        for i in range(9):
            j = (i * 4) + 1
            if line[j] != " ":
                q[i].append(line[j])
    [x.append("*") for x in q]
    [x.reverse() for x in q]
    q2 = [deque(x) for x in q]
    print(q2)

    with open("day5/inputs2.txt", "r") as f:
        for line in f:
            line = line.strip()
            _move, count, _frm, frm, _to, to = line.split(" ")
            count = int(count)
            frm = int(frm)
            to = int(to)
            l = []
            for _ in range(count):
                l.append(q2[frm - 1].pop())
            l.reverse()
            q2[to - 1].extend(l)
    result = ""
    for i in range(9):
        result += q2[i].pop()
    print(result)
