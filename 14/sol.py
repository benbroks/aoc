def value_to_bit_str(value):
    i = 35
    output_str = ""
    while i >= 0:
        if value >= 2**i:
            output_str += '1'
            value -= 2**i
        else:
            output_str += '0'
        i -= 1
    return output_str

def bit_str_to_value(bit_str):
    i = 35
    value = 0
    for j in range(len(bit_str)):
        if bit_str[j] == '1':
            value += 2**(i-j)
    return value

def merge_strings(mask,bit_str):
    output_str = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            output_str += bit_str[i]
        else:
            output_str += mask[i]
    return output_str

def get_address_and_value(line):
    begin = line.find('[') + 1
    end = line.find(']')
    return int(line[begin:end]), int(line[end+4:].rstrip())

def pt1(input_fp='input.txt'):
    mask = ''
    memory_locs = {}
    with open(input_fp) as f:
        for line in f:
            if line[:2] == 'ma':
                mask = line[7:].rstrip()
            else:
                address,value = get_address_and_value(line)
                bit_str = value_to_bit_str(value)
                new_bit_str = merge_strings(mask,bit_str)
                new_value = bit_str_to_value(new_bit_str)
                memory_locs[address] = new_value
    sum_ = 0
    for loc in memory_locs:
        sum_ += memory_locs[loc]
    return sum_

def mask_to_value_set(mask):
    i = 35
    value_set = set([0])
    for j in range(len(mask)):
        if mask[j] != '0':
            if mask[j] == '1':
                temp_value_set = set()
            elif mask[j] == 'X':
                temp_value_set = set(value_set)
            for item in value_set:
                temp_value_set.add(item+2**i)
            value_set = temp_value_set
        i -= 1
    return value_set

def merge_strings_pt2(mask,bit_str):
    i = 35
    output_value = 0
    for j in range(len(mask)):
        if mask[j] == '0' and bit_str[j] == '1':
            output_value += 2**i
        i -= 1
    return output_value

def pt2(input_fp='input.txt'):
    mask = ''
    memory_locs = {}
    with open(input_fp) as f:
        for line in f:
            if line[:2] == 'ma':
                mask = line[7:].rstrip()
                mask_value_set = mask_to_value_set(mask)
            else:
                address,value = get_address_and_value(line)
                bit_str = value_to_bit_str(address)
                to_append = merge_strings_pt2(mask,bit_str)
                for item in mask_value_set:
                    memory_locs[item+to_append] = value 
    final_sum = 0
    for mem in memory_locs:
        final_sum += memory_locs[mem]
    return final_sum
                
if __name__ == '__main__':
    print(pt2())