import math

def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def falls_in_range(y_vel,y1,y2):
    t1 = (-1 + math.sqrt(1+4*(y_vel**2 + y_vel-2*y1)))/2
    t2 = (-1 + math.sqrt(1+4*(y_vel**2 + y_vel-2*y2)))/2
    print(y_vel,t2,t1)
    if int(t1) == t1 or int(t2) == t2:
        return True
    if int(t1) != int(t2):
        return True
    return False
    

def pt1():
    input_lines = read_input()
    split_up = input_lines[0].split()
    x = split_up[-2][:-1]
    y= split_up[-1]
    x1 = int(x.split('=')[1].split('.')[0])
    x2 = int(x.split('=')[1].split('.')[-1])
    y1 = int(y.split('=')[1].split('.')[0])
    y2 = int(y.split('=')[1].split('.')[-1])
    y_vel = 1
    max_vel = 0
    for y_vel in range(0,10000):
        if falls_in_range(y_vel,y1,y2):
            max_vel = y_vel
        y_vel += 1
    return (max_vel+1)*max_vel/2

def does_solution_work(x_vel,y_vel,x1,x2,y1,y2):
    live_x = 0
    live_y = 0
    while True:
        if live_x >= x1 and live_x <= x2 and live_y >= y1 and live_y <= y2:
            return True
        if live_y < y1:
            if live_x > x2 or x_vel == 0:
                return False
        live_x += x_vel
        live_y += y_vel
        x_vel = max(0,x_vel-1)
        y_vel -= 1

def pt2():
    input_lines = read_input()
    split_up = input_lines[0].split()
    x = split_up[-2][:-1]
    y= split_up[-1]
    x1 = int(x.split('=')[1].split('.')[0])
    x2 = int(x.split('=')[1].split('.')[-1])
    y1 = int(y.split('=')[1].split('.')[0])
    y2 = int(y.split('=')[1].split('.')[-1])
    num_solutions = 0
    for x in range(1,51):
        for y in range(-267,267):
            if does_solution_work(x,y,x1,x2,y1,y2):
                num_solutions += 1
    return num_solutions
    

if __name__ == '__main__':
    print(pt2())