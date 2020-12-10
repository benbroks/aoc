def pt1(input_fp="input.txt",x_diff=3,y_diff=1):
    y_coord = 0
    x_coord = 0
    num_trees = 0
    with open(input_fp) as f:
        for line in f:
            if x_coord % y_diff == 0:
                line = line.rstrip()
                if line[y_coord % len(line)] == '#':
                    num_trees += 1
                y_coord += x_diff
            x_coord += 1
    return num_trees

def pt2():
    a = pt1(x_diff=1,y_diff=1)
    b = pt1(x_diff=3,y_diff=1)
    c = pt1(x_diff=5,y_diff=1)
    d = pt1(x_diff=7,y_diff=1)
    e = pt1(x_diff=1,y_diff=2)
    return a*b*c*d*e

if __name__ == "__main__":
    print(pt2())
            
