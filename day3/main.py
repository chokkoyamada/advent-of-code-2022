chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    inputs = open("day3/inputs.txt", "r").readlines()
    score = 0
    for line in inputs:
        line = line.rstrip()
        line_length = len(line)
        first_pack = line[0 : line_length // 2]
        second_pack = line[line_length // 2 : line_length]
        already_scored_char= []
        for char in first_pack:
            for char2 in second_pack:
                if char == char2 and char not in already_scored_char:
                    score += chars.index(char) + 1
                    already_scored_char += char

    return score


if __name__ == "__main__":
    x = main()
    print(x)
