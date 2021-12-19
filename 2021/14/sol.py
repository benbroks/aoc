def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def pt1():
    input_lines = read_input()
    input_string = input_lines[0]
    
    rule_map = {}
    for l in input_lines[2:]:
        parts = l.split()
        rule_map[parts[0]] = parts[2]
        
    # Expanding String
    for _ in range(10):
        i = 0
        while i < len(input_string)-1:
            pair_to_examine = input_string[i:i+2]
            if pair_to_examine in rule_map:
                input_string = input_string[:i+1] + rule_map[pair_to_examine] + input_string[i+1:] 
                i += 2
            else:
                i += 1
    # Create Char Occurrence Map
    o_map = {}
    for c in input_string:
        if c in o_map:
            o_map[c] += 1
        else:
            o_map[c] = 1
    
    return max(o_map.values()) - min(o_map.values())

def pt1():
    input_lines = read_input()
    input_string = input_lines[0]
    
    rule_map = {}
    for l in input_lines[2:]:
        parts = l.split()
        rule_map[parts[0]] = parts[2]
        
    # Expanding String
    for _ in range(40):
        i = 0
        while i < len(input_string)-1:
            pair_to_examine = input_string[i:i+2]
            if pair_to_examine in rule_map:
                input_string = input_string[:i+1] + rule_map[pair_to_examine] + input_string[i+1:] 
                i += 2
            else:
                i += 1
    # Create Char Occurrence Map
    o_map = {}
    for c in input_string:
        if c in o_map:
            o_map[c] += 1
        else:
            o_map[c] = 1
    
    return max(o_map.values()) - min(o_map.values())

def merge_dictionaries(a,b):
    o = {}
    for k in a:
        o[k] = a[k]
    for k in b:
        if k in o:
            o[k] += b[k]
        else:
            o[k] = b[k]
    return o

def recursive_calc(pair, steps_left, rule_map):
    print(steps_left, pair)
    if steps_left == 0:
        o = {}
        if pair[0] == pair[1]:
            o[pair[0]] = 2
        else:
            o[pair[0]] = 1
            o[pair[1]] = 1
        return o
    middle_char = rule_map[pair]
    a = recursive_calc(pair[0]+middle_char, steps_left-1,rule_map)
    b = recursive_calc(middle_char+pair[1], steps_left-1,rule_map)
    c = merge_dictionaries(a,b)
    c[middle_char] -= 1
    return c

class MemoizedCalc:
    def __init__(self, rule_map, max_steps):
        self.m = {}
        for t in range(max_steps+1):
            self.m[t] = {}
            for p in rule_map:
                c = {}
                if t == 0:
                    if p[0] == p[1]:
                        c[p[0]] = 2
                    else:
                        c[p[0]] = 1
                        c[p[1]] = 1
                else:
                    m_c = rule_map[p]
                    p1 = p[0] + m_c
                    p2 = m_c + p[1]
                    a = self.m[t-1][p1]
                    b = self.m[t-1][p2]
                    c = merge_dictionaries(a,b)
                    c[m_c] -= 1
                self.m[t][p] = c
    
    def get_results(self, p,t):
        return self.m[t][p]

def pt2():
    input_lines = read_input()
    input_string = input_lines[0]
    
    rule_map = {}
    for l in input_lines[2:]:
        parts = l.split()
        rule_map[parts[0]] = parts[2]
        
    # Generating String Dictionary
    for _ in range(2):
        i = 0
        c = {}
        m = MemoizedCalc(rule_map,40)
        while i < len(input_string)-1:
            pair_to_examine = input_string[i:i+2]
            new_m = m.get_results(pair_to_examine, 40)
            c = merge_dictionaries(c,new_m)
            if i != 0:
                c[input_string[i]] -= 1
            i += 1
    return max(c.values()) - min(c.values())

    
if __name__ == '__main__':
    print(pt2())