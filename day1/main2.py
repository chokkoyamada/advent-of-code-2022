def main():
    with open("day1/inputs.txt", "r") as f:
        inputs = f.readlines()
        inputs_t = [x.replace("\n", "") for x in inputs]

    result = []
    tmp = 0
    for x in inputs_t:
        if x != "":
            tmp += int(x)
        else:
            result.append(tmp)
            tmp = 0
    x = sorted(result, reverse=True)
    return x[0] + x[1] + x[2]


if __name__ == "__main__":
    x = main()
    print(x)
