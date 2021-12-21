def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def hex_to_bin(h_str):
    mapping = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
    }
    return "".join([mapping[i] for i in h_str])

def bin_to_dec(b_str):
    n = len(b_str)
    total_val = 0
    for i in range(n):
        total_val += int(b_str[i])*2**(n-i-1)
    return total_val

def read_single_packet(idx,p_str):
    if len(p_str) - idx <= 4:
        return len(p_str), '0'
    print(p_str[idx:])
    packet_version = p_str[idx:idx+3]
    type_id = p_str[idx+3:idx+6]
    print(packet_version, type_id)
    idx += 6
    if type_id == "100":
        print("literal packet")
        while p_str[idx] != '0':
            idx += 5
        idx += 5
    else:
        print("operator packet")
        length_type_id = p_str[idx]
        if length_type_id == '0':
            # Next 15 Bits Demo Sub-Packet Length
            idx += 16
        else:
            # Next 11 Bits Demo # of Sub-Packets
            idx += 12
    return idx, packet_version

def pt1():
    input_lines = read_input()
    idx = 0
    pv_sum = 0
    p_str = hex_to_bin(input_lines[0])
    while idx < len(p_str):
        idx,pv = read_single_packet(idx,p_str)
        pv_sum += bin_to_dec(pv)
    return pv_sum

def packet_instruction(idx,p_str):
    if len(p_str) - idx <= 5:
        return "", len(p_str)
    _ = p_str[idx:idx+3]
    type_id = p_str[idx+3:idx+6]
    idx += 6
    if type_id == "100":
        binary_string = ""
        while p_str[idx] != '0':
            binary_string = binary_string + p_str[idx+1:idx+5]
            idx += 5
        binary_string = binary_string + p_str[idx+1:idx+5]   
        idx += 5
        to_return = bin_to_dec(binary_string)
    else:
        if type_id == "000":
            to_return = '+'
        elif type_id == "001":
            to_return = '*'
        elif type_id == "010":
            to_return = 'min'
        elif type_id == "011": 
            to_return = 'max'
        elif type_id == "101": 
            to_return = '>'
        elif type_id == "110": 
            to_return = '<'
        elif type_id == "111":
            to_return = '='
    return to_return, idx

def parse_packets(idx,p_str):
    to_return, new_idx = packet_instruction(idx,p_str)
    if isinstance(to_return,int):
        return to_return, new_idx
    else:
        length_type_id = p_str[new_idx]
        values = []
        if length_type_id == '0':
            # Next 15 Bits Demo Sub-Packet Length
            num_bits = bin_to_dec(p_str[new_idx+1:new_idx+16])
            new_starter_idx = new_idx+16
            while new_starter_idx < new_idx+16+num_bits:
                sub_to_return, new_starter_idx = parse_packets(new_starter_idx,p_str)
                values.append(sub_to_return)
        else:
            # Next 11 Bits Demo # of Sub-Packets
            num_sub_packets= bin_to_dec(p_str[new_idx+1:new_idx+12])
            new_starter_idx = new_idx+12
            for _ in range(num_sub_packets):
                sub_to_return, new_starter_idx = parse_packets(new_starter_idx,p_str)
                values.append(sub_to_return)
        return perform_operation(to_return,values), new_starter_idx  
    
def perform_operation(o,values):
    print(o)
    if o == "+":
        s = 0
        for v in values:
            s += v
    elif o == "*":
        s = 1
        for v in values:
            s *= v
    elif o == "min":
        s = min(values)
    elif o == "max":
        s = max(values)
    elif o == ">":
        if values[0] > values[1]:
            s = 1
        else:
            s = 0
    elif o == "<":
        if values[0] < values[1]:
            s = 1
        else:
            s = 0
    elif o == "=":
        if values[0] == values[1]:
            s = 1
        else:
            s = 0
    return s

def pt2():
    input_lines = read_input()
    idx = 0
    p_str = hex_to_bin(input_lines[0])
    v, idx= parse_packets(idx,p_str)
    return v

if __name__ == '__main__':
    print(pt2())