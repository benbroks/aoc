def populate_dict(input_fp="input.txt"):
    numbers = {}
    # loading in
    with open(input_fp) as f:
        for line in f:
            num = int(line)
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
    return numbers


def pt1(numbers = None, to_sum=2020):
    if numbers is None:
        numbers = populate_dict()
    for num in numbers:
        if numbers[num] > 0:
            if to_sum - num == num and numbers[num] > 1:
                return num*num
            elif to_sum - num in numbers:
                return num * (to_sum-num)
    return 0

def pt2(numbers=None,to_sum=2020):
    if numbers is None:
        numbers = populate_dict()
    for num in numbers:
        numbers[num] -= 1
        intermediate = pt1(numbers,to_sum-num)
        if intermediate != 0:
            return intermediate * num
        else:
            numbers[num] += 1
    return 0

if __name__ == "__main__":
    print(pt2())

