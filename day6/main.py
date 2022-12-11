from collections import deque

if __name__ == "__main__":
    with open("day6/inputs.txt") as f:
        data = f.read()
    l = deque([], maxlen=4)
    for index, char in enumerate(data):
        l.append(char)
        if len(l) < 4:
            continue
        # lの要素がすべて異なる場合
        if len(set(l)) == 4:
            print(set(l))
            print(f"Found! {index+1} {char}")
            break
