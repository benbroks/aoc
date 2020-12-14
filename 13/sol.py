from functools import reduce

def pt1(input_fp='input.txt'):
    with open(input_fp) as f:
        lines = []
        for line in f:
            lines.append(line)
    og_time = int(lines[0])
    denoms = []
    for i in lines[1].split(','):
        try:
            bus_id = int(i)
            denoms.append(bus_id)
        except:
            pass
    min_possible_time = denoms[0] - (og_time%denoms[0])
    for d in denoms:
        if d - (og_time%d) <= min_possible_time:
            min_possible_time = d - (og_time%d)
            result = min_possible_time * d
    return result

def chinese_remainder_thm(remainders, factors):
    big_n = reduce((lambda x, y: x * y), factors)
    sum_ = 0
    for i in range(len(factors)):
        product = int(big_n/factors[i])
        cur_remainder = remainders[i]
        inverse_result = euclid_alg(product, factors[i])
        if inverse_result[0] < 0:
            inverse = inverse_result[0] % factors[i]
        else:
            inverse = inverse_result[0]
        sum_ += cur_remainder * product * inverse
    return sum_ % big_n

def euclid_alg(big,small):
    remainder = big % small
    factor = int((big-remainder)/small)*-1
    if remainder == 1:
        return 1, factor
    else:
        b_factor, s_factor = euclid_alg(small, remainder)
        first_factor = s_factor
        sec_factor = factor * s_factor + b_factor
    return first_factor, sec_factor

def pt2(input_fp='input.txt'):
    factors = []
    remainders = []
    with open(input_fp) as f:
        lines = []
        for line in f:
            lines.append(line)
    bus_ids = lines[1].split(',')
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            bus_id = int(bus_ids[i])
            factors.append(bus_id)
            remainder = -1*i % bus_id
            remainders.append(remainder)
    return chinese_remainder_thm(remainders, factors)

if __name__ == '__main__':
    print(pt2())




