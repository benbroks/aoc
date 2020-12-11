def construct_adapters(input_fp='input.txt'):
    adapters = []
    with open(input_fp) as f:
        for line in f:
            adapters.append(int(line))
    adapters.sort()
    return adapters

def pt1():
    adapters = construct_adapters()
    # Count Diffs
    one_diff = 0
    three_diff = 1
    if adapters[0] == 1:
        one_diff += 1
    if adapters[0] == 3:
        three_diff += 1
    for i in range(1,len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            one_diff += 1
        if adapters[i] - adapters[i-1] == 3:
            three_diff += 1
    return three_diff*one_diff

def pt2():
    adapters = construct_adapters()
    solution = [1]
    for i in range(len(adapters)-1,-1,-1):
        temp = 0
        current = adapters[i]
        for j in range(3):
            if i+j+1 < len(adapters):
                if adapters[i+j+1] <= current + 3:
                    temp += solution[j]
        solution = [max(temp,1)] + solution
    total = 0
    for i in range(3):
        if adapters[i] <= 3:
            total += solution[i]
    return total
        
if __name__ == "__main__":
    print(pt2())
