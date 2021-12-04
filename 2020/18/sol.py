def line_to_seq(line):
    result = []
    i = 0
    while i < len(line):
        if line[i] != ' ':
            result.append(line[i])
        i += 1
    return result

def subseq(seq):
    j = 1
    num_right_p = 0
    num_left_p = 0
    print(seq)
    if seq[0] == '(':
        num_left_p += 1
    while num_left_p != num_right_p:
        if seq[j] == '(':
            num_left_p += 1
        if seq[j] == ')':
            num_right_p += 1
        j += 1
    if j != 1:
        return seq[1:j-1], j
    return seq[:j], j

def solve_seq_pt1(seq):
    if len(seq) == 0:
        return 0
    if len(seq) == 1:
        return int(seq[0])
    # Left Value
    left,j = subseq(seq)
    left_val = solve_seq_pt1(left)
    if j == len(seq):
        return left_val
    seq = [left_val] + seq[j:]
    # Operator
    operator = seq[1]
    right,j = subseq(seq[2:])
    right_val = solve_seq_pt1(right)
    if operator == '+':
        return solve_seq_pt1([left_val + right_val] + seq[j+2:])
    if operator == '*':
        return solve_seq_pt1([left_val * right_val] + seq[j+2:])

def pt1(input_fp='input.txt'):
    sum_ = 0
    with open(input_fp) as f:
        for line in f:
            line = line.rstrip()
            seq = line_to_seq(line)
            sum_ += solve_seq_pt1(seq)
    return sum_

if __name__ == '__main__':
    print(pt1())