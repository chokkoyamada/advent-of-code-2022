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
    return max(result)


if __name__ == "__main__":
    x = main()
    print(x)
