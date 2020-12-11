def valid_num(prev,num):
    for item in prev:
        if prev[item] > 0:
            to_find = num - item
            if to_find == item:
                if prev[item] >= 2:
                    return True
            else:
                if to_find in prev and prev[to_find] > 0:
                    return True
    return False


def pt1(input_fp='input.txt', preamble=25):
    prev = {}
    last_ = []
    with open(input_fp) as f:
        examined = 0
        for line in f:
            if examined < preamble:
                # Instantiating Preamble
                num = int(line)
                last_.append(num)
                if num in prev:
                    prev[num] += 1
                else:
                    prev[num] = 1
            else:
                num = int(line)
                if not valid_num(prev,num):
                    return num     
                # Cleaning Up
                prev[last_[0]] -= 1
                if num in prev:
                    prev[num] += 1
                else:
                    prev[num] = 1
                last_.append(num)
                last_ = last_[1:]
            examined += 1
    return 'fail'

def pt2(invalid_num, input_fp='input.txt'):
    sequence = []
    sequence_sum = 0
    with open(input_fp) as f:
        for line in f:
            num = int(line)
            sequence.append(num)
            sequence_sum += num
            while sequence_sum > invalid_num:
                sequence_sum -= sequence[0]
                sequence = sequence[1:]
            if sequence_sum == invalid_num:
                return min(sequence) + max(sequence)
    return 'fail'
                
if __name__ == '__main__':
    invalid_number = pt1()
    print(pt2(invalid_num=invalid_number))