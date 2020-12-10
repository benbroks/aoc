def parse_line(t):
    t.rstrip()
    parts = t.split(' ')
    # Range
    r = parts[0].split('-')
    min_ = int(r[0])
    max_ = int(r[1])
    # Char
    char = parts[1][0]
    # Password
    pwd = parts[2]
    return min_,max_,char,pwd

def valid_password_pt1(min_,max_,letter,pwd):
    count = 0
    for char in pwd:
        if char == letter:
            count += 1
    if count >= min_ and count <= max_:
        return True
    return False

def valid_password_pt2(p1,p2,letter,pwd):
    a = pwd[p1-1] == letter
    b = pwd[p2-1] == letter
    return a != b

def pt1(input_fp="input.txt"):
    valid = 0
    with open(input_fp) as f:
        for line in f:
            min_,max_,char,pwd = parse_line(line)
            if valid_password_pt1(min_,max_,char,pwd):
                valid += 1

def pt2(input_fp="input.txt"):
    valid = 0
    with open(input_fp) as f:
        for line in f:
            min_,max_,char,pwd = parse_line(line)
            if valid_password_pt2(min_,max_,char,pwd):
                valid += 1
    print(valid)
    

if __name__ == "__main__":
    pt2()
