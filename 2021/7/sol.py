from os import read


import math

def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings


def pt1():
    line_strings = read_input()
    position_sequence = [int(n) for n in line_strings[0].split(',')]
    position_sequence.sort()
    n = len(position_sequence)
    if n % 2 == 1:
        ideal = position_sequence[int(n/2)]
    else:
        ideal = (position_sequence[int(n/2)] + position_sequence[int(n/2)-1])/2
    return sum([abs(i-ideal) for i in position_sequence])

def pt2_error(x_star, values):
    summed_error = 0
    for v in values:
        abs_error = abs(x_star-v)
        summed_error += abs_error**2 + abs_error
    return summed_error / 2

def pt2():
    line_strings = read_input()
    position_sequence = [int(n) for n in line_strings[0].split(',')]
    position_sequence.sort()
    n = len(position_sequence)
    if n % 2 == 1:
        median = position_sequence[int(n/2)]
        
    else:
        median = (position_sequence[int(n/2)] + position_sequence[int(n/2)-1])/2
    mean = int(sum(position_sequence)/n)
    min_m = min(mean,median)
    max_m = max(mean,median)
    ideal_error = pt2_error(min_m,position_sequence)
    for x_star in range(min_m,max_m+5):
        current_error = pt2_error(x_star,position_sequence)
        if current_error < ideal_error:
            ideal_error = current_error
    return ideal_error

if __name__ == '__main__':
    print(pt2())