# A グー 1点
# B パー 2点
# C チョキ 3点
# X グー
# Y パー
# Z チョキ

gu = 1
pa = 2
tyoki = 3
lost = 0
draw = 3
win = 6


def main():
    with open("day2/inputs.txt", "r") as f:
        inputs = f.readlines()
        inputs_t = [x.replace("\n", "") for x in inputs]

    point = 0
    for i in inputs_t:
        [you, me] = i.split(" ")
        if you == "A" and me == "X":
            point += draw + gu
        elif you == "A" and me == "Y":
            point += win + pa
        elif you == "A" and me == "Z":
            point += lost + tyoki
        elif you == "B" and me == "X":
            point += lost + gu
        elif you == "B" and me == "Y":
            point += draw + pa
        elif you == "B" and me == "Z":
            point += win + tyoki
        elif you == "C" and me == "X":
            point += win + gu
        elif you == "C" and me == "Y":
            point += lost + pa
        elif you == "C" and me == "Z":
            point += draw + tyoki
        else:
            raise ValueError("Invalid input")
    return point


if __name__ == "__main__":
    x = main()
    print(x)
