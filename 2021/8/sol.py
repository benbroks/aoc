def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def pt1():
    input_lines = read_input()
    num_uniques = 0
    for l in input_lines:
        to_split = l.split('|')
        nums = to_split[-1].split()
        for n in nums:
            if len(n) == 2 or len(n) == 3 or len(n) == 4 or len(n) == 7:
                num_uniques += 1
    return num_uniques    

def build_assignments(assignments, nums):
    # Numbers with Unique Segment Counts
    assignments[1] = nums[0]
    assignments[7] = nums[1]
    assignments[4] = nums[2]
    assignments[8] = nums[9]
    nums = nums[3:9]
    # Find 3
    if len(assignments[1].intersection(nums[0])) == 2:
        assignments[3] = nums[0]
        nums.pop(0)
    elif len(assignments[1].intersection(nums[1])) == 2:
        assignments[3] = nums[1]
        nums.pop(1)
    else:
        assignments[3] = nums[2]
        nums.pop(2)
    # Find 9
    if len(assignments[3].intersection(nums[2])) == 5:
        assignments[9] = nums[2]
        nums.pop(2)
    elif len(assignments[3].intersection(nums[3])) == 5:
        assignments[9] = nums[3]
        nums.pop(3)
    else:
        assignments[9] = nums[4]
        nums.pop(4)
    # Find 0
    if len(assignments[1].intersection(nums[2])) == 2:
        assignments[0] = nums[2]
        nums.pop(2)
    else:
        assignments[0] = nums[3]
        nums.pop(3)
    # Find 5
    if len(assignments[9].intersection(nums[0])) == 5:
        assignments[5] = nums[0]
        nums.pop(0)
    else:
        assignments[5] = nums[1]
        nums.pop(1)
    assignments[2] = nums[0]
    assignments[6] = nums[1]
    return assignments
    
def pt2():
    input_lines = read_input()
    all_values_summed = 0
    for l in input_lines:
        to_split = l.split('|')
        clues = [set(n) for n in to_split[0].split()]
        clues.sort(key=lambda x:len(x))
        assignments = [0]*10
        assignments = build_assignments(assignments, clues)
        to_calc = [set(n) for n in to_split[1].split()]
        current_num = ""
        for v in to_calc:
            for i,a in enumerate(assignments):
                if v == a:
                    current_num += str(i)
        all_values_summed += int(current_num)
    return all_values_summed
        

if __name__ == '__main__':
    print(pt2())