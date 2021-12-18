def get_binary_strings(input_fp="input.txt"):
    with open(input_fp) as f:
        binary_strings = [line.strip() for line in f]
    return binary_strings

def populate_dictionary(input_fp="input.txt"):
    binary_string_dict = {}
    # loading in
    binary_strings = get_binary_strings(input_fp="input.txt")
    N = len(binary_strings[0])
    for i in range(N):
        binary_string_dict[i] = {"0": 0, "1": 0}
    for bs in binary_strings:
        for i in range(N):
            binary_string_dict[i][bs[i]] += 1
    return binary_string_dict

def binary_to_int(bs, N):
    value = 0
    for i in range(N):
        if bs[i] == "1":
            value += 2**(N-i-1)
    return value

def pt1(occurrences = None):
    if occurrences is None:
        occurrences = populate_dictionary()
    N = len(occurrences)
    total = 2**N - 1
    gamma_string = ""
    for i in range(N):
        if occurrences[i]["0"] > occurrences[i]["1"]:
            gamma_string += "0"
        else:
            gamma_string += "1"
    gamma_value = binary_to_int(gamma_string, N)
    epsilon_value = total - gamma_value
    return gamma_value*epsilon_value

def pt2(commands = None):
    if commands is None:
        og_binary_strings = get_binary_strings()
        co_binary_strings = get_binary_strings()
    # Oxygen Generator Rating
    N = len(og_binary_strings[0])
    for i in range(N):
        num_zeros = sum([1 if bs[i] == "0" else 0 for bs in og_binary_strings])
        if num_zeros > len(og_binary_strings) - num_zeros:
            og_binary_strings = [bs for bs in og_binary_strings if bs[i] == "0"]
        else:
            og_binary_strings = [bs for bs in og_binary_strings if bs[i] == "1"] 
        if len(og_binary_strings) == 1:
            break
    oxygen_generator_rating = binary_to_int(og_binary_strings[0],N)
    # C02 Scrubber Rating
    N = len(co_binary_strings[0])
    for i in range(N):
        num_zeros = sum([1 if bs[i] == "0" else 0 for bs in co_binary_strings])
        if num_zeros <= len(co_binary_strings) - num_zeros:
            co_binary_strings = [bs for bs in co_binary_strings if bs[i] == "0"]
        else:
            co_binary_strings = [bs for bs in co_binary_strings if bs[i] == "1"] 
        if len(co_binary_strings) == 1:
            break
    co2_scrubber_rating = binary_to_int(co_binary_strings[0],N)
    
    return oxygen_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
    print(pt2())

