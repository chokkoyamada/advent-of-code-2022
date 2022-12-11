chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    inputs = open("day3/inputs.txt", "r").readlines()
    score = 0
    while True:
        if len(inputs) == 0:
            break
        first_pack = inputs.pop(0).rstrip()
        second_pack = inputs.pop(0).rstrip()
        third_pack = inputs.pop(0).rstrip()
        already_scored_char = []
        for char in first_pack:
            for char2 in second_pack:
                for char3 in third_pack:
                    if char == char2 and char2 == char3 and char not in already_scored_char:
                        score += chars.index(char) + 1
                        already_scored_char += char

    return score


if __name__ == "__main__":
    x = main()
    print(x)
