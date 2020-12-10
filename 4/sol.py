def valid_passport(line):
    parts = line.split()
    if len(parts) < 7:
        return False
    if len(parts) == 7:
        for part in parts:
            if part.split(':')[0] == "cid":
                return False
    for part in parts:
        first = part.split(':')[0]
        second = part.split(':')[1]
        if validate_field(first,second) == False:
            return False
    return True

def validate_field(first,second):
    if first == 'byr':
        try:
            second = int(second)
            return second >= 1920 and second <= 2002
        except:
            return False
    if first == 'iyr':
        try:
            second = int(second)
            return second >= 2010 and second <= 2020
        except:
            return False
    if first == 'eyr':
        try:
            second = int(second)
            return second >= 2020 and second <= 2030
        except:
            return False
    if first == 'hgt':
        if second[-2:] == 'cm':
            try:
                value = int(second[:-2])
                return value >= 150 and value <= 193
            except:
                return False
        elif second[-2:] == 'in':
            try:
                value = int(second[:-2])
                return value >= 59 and value <= 76
            except:
                return False
        else:
            return False
    if first == 'hcl':
        if len(second) != 7:
            return False
        if second[0] != '#':
            return False
        for i in range(1,7):
            char = ord(second[i])
            is_num = False
            is_char = False
            is_num = char >= ord('0') and char <= ord('9')
            is_char = char >= ord('a') and char <= ord('f')
            if (is_num or is_char) == False:
                return False
        return True
    if first == 'ecl':
        possible = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if second in possible:
            return True
        return False
    if first == 'pid':
        if len(second) != 9:
            return False 
        try:
            sample_num = int(second)
            return True
        except:
            return False
    return True
    

def pt1(input_fp="input.txt"):
    with open(input_fp) as f:
        valid = 0
        line_num = 0
        temp_passport = ""
        for line in f:
            if line == '\n':
                if valid_passport(temp_passport):
                    valid += 1
                temp_passport = ""
            else:
                line = line.rstrip()
                temp_passport = temp_passport + " " + line
            line_num += 1
        if valid_passport(temp_passport):
            valid += 1
    return valid

if __name__ == "__main__":
    print(pt1())

