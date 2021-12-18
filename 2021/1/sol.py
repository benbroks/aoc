def populate_dict(input_fp="input.txt"):
    numbers = {}
    # loading in
    with open(input_fp) as f:
        numbers = [int(line) for line in f]
    return numbers


def pt1(numbers = None):
    if numbers is None:
        numbers = populate_dict()
    num_increased = 0
    for i in range(len(numbers)):
        if i > 0 and numbers[i] > numbers[i-1]:
            num_increased += 1
    return num_increased

def pt2(numbers = None):
    if numbers is None:
        numbers = populate_dict()
    num_sliding_windows_increased = 0
    for i in range(len(numbers)):
        if i > 2 and numbers[i] > numbers[i-3]:
            num_sliding_windows_increased += 1
    return num_sliding_windows_increased

if __name__ == "__main__":
    print(pt2())

