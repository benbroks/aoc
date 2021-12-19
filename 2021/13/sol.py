
def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def pt1():
    input_lines = read_input()
    set_of_points = set()
    instructions = []
    find_points_mode = True
    for l in input_lines:
        if l == '':
            find_points_mode = False
        else:
            if find_points_mode:
                set_of_points.add(l)
            else:
                instructions.append(l.split()[-1])
    # Go Through Instructions
    i = instructions[0]
    axis = i[0]
    a_num = int(i.split('=')[-1])
    to_remove = []
    to_add = []
    for p in set_of_points:
        pair_p = p.split(',')
        if axis == 'x':
            to_compare = int(pair_p[0])
            if to_compare > a_num:
                new_p = "{},{}".format(a_num- (to_compare-a_num),pair_p[1])
                to_remove.append(p)
                to_add.append(new_p)
        else:
            to_compare = int(pair_p[1])
            if to_compare > a_num:
                new_p = "{},{}".format(pair_p[0], a_num- (to_compare-a_num))
                to_remove.append(p)
                to_add.append(new_p)
    for p in to_remove:
        set_of_points.remove(p)
    for p in to_add:
        set_of_points.add(p)
        
    return len(set_of_points)

def pt2():
    input_lines = read_input()
    set_of_points = set()
    instructions = []
    find_points_mode = True
    for l in input_lines:
        if l == '':
            find_points_mode = False
        else:
            if find_points_mode:
                set_of_points.add(l)
            else:
                instructions.append(l.split()[-1])
    for i in instructions:
        axis = i[0]
        a_num = int(i.split('=')[-1])
        to_remove = []
        to_add = []
        for p in set_of_points:
            pair_p = p.split(',')
            if axis == 'x':
                to_compare = int(pair_p[0])
                if to_compare > a_num:
                    new_p = "{},{}".format(a_num- (to_compare-a_num),pair_p[1])
                    to_remove.append(p)
                    to_add.append(new_p)
            else:
                to_compare = int(pair_p[1])
                if to_compare > a_num:
                    new_p = "{},{}".format(pair_p[0], a_num- (to_compare-a_num))
                    to_remove.append(p)
                    to_add.append(new_p)
        for p in to_remove:
            set_of_points.remove(p)
        for p in to_add:
            set_of_points.add(p)
    # Max X is 40 (from my data), Max Y is 6
    max_x = 40
    max_y = 6
    for j in range(max_y):
        line_str = ""
        for i in range(max_x):
            if "{},{}".format(i,j) in set_of_points:
                line_str += "#"
            else:
                line_str += "."
        print(line_str)
    
    return 1

if __name__ == '__main__':
    print(pt2())