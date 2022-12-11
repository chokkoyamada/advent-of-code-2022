def main():
    inputs = open("day4/inputs.txt", "r").readlines()
    count = 0
    for line in inputs:
        line = line.rstrip()
        x = line.split(",")
        a1, a2 = [int(i) for i in x[0].split("-")]
        b1, b2 = [int(i) for i in x[1].split("-")]
        if (a1 < b1 and a2 < b1) or (a1 > b2 and a2 > b2):
            count += 1

    return len(inputs) - count


if __name__ == "__main__":
    x = main()
    print(x)
