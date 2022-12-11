# A グー 1点
# B パー 2点
# C チョキ 3点
# X 負け
# Y 引き分け
# Z 勝ち

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
        [you, result] = i.split(" ")
        if you == "A" and result == "X":
            # Aは相手がグー,Xは負けなので自分はチョキを出す
            point += lost + tyoki
        elif you == "A" and result == "Y":
            # Aは相手がグー,Yは引き分けなので自分はグーを出す
            point += draw + gu
        elif you == "A" and result == "Z":
            # Aは相手がグー,Zは勝ちなので自分はパーを出す
            point += win + pa
        elif you == "B" and result == "X":
            # Bは相手がパー,Xは負けなので自分はグーを出す
            point += lost + gu
        elif you == "B" and result == "Y":
            # Bは相手がパー,Yは引き分けなので自分はパーを出す
            point += draw + pa
        elif you == "B" and result == "Z":
            # Bは相手がパー,Zは勝ちなので自分はチョキを出す
            point += win + tyoki
        elif you == "C" and result == "X":
            # Cは相手がチョキ,Xは負けなので自分はパーを出す
            point += lost + pa
        elif you == "C" and result == "Y":
            # Cは相手がチョキ,Yは引き分けなので自分はチョキを出す
            point += draw + tyoki
        elif you == "C" and result == "Z":
            # Cは相手がチョキ,Zは勝ちなので自分はグーを出す
            point += win + gu
        else:
            raise ValueError("Invalid input")

    return point


if __name__ == "__main__":
    x = main()
    print(x)
