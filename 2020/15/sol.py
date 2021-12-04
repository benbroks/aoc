def build_dict(input_fp='input.txt'):
    with open(input_fp) as f:
        for line in f:
            return line.split(',')

def pt1():
    # Populating Starter Dictionary
    starter = build_dict()
    to_populate = starter[:-1]
    time_dict = {}
    num_spoken = 1
    for num in to_populate:
        time_dict[int(num)] = num_spoken
        num_spoken += 1
    # Actual Recitations
    current_num = int(starter[-1])
    former_num = 0
    while num_spoken <= 30000000:
        # Return 2020th Number
        if num_spoken == 30000000:
            return current_num
        # Update Former+Current
        former_num = current_num
        # Define Current Num
        if former_num not in time_dict:
            current_num = 0
        else:
            current_num = num_spoken - time_dict[former_num]
        # Update Dictionary
        time_dict[former_num] = num_spoken
        num_spoken += 1

if __name__ == '__main__':
    print(pt1())