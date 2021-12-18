def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def build_line_segment(line_string):
  split_by_space = line_string.split()
  first_pair = split_by_space[0].split(',')
  second_pair = split_by_space[2].split(',')
  x1 = int(first_pair[0])
  y1 = int(first_pair[1])
  x2 = int(second_pair[0])
  y2 = int(second_pair[1])
  return x1,y1,x2,y2

def enumerate_line_segment(x1,y1,x2,y2,o_map,overlap_count):
  if x1 == x2:
    if x1 not in o_map:
      o_map[x1] = {}
    min_y = min(y1,y2)
    max_y = max(y1,y2)
    for y in range(min_y,max_y+1):
      if y not in o_map[x1]:
        o_map[x1][y] = 1
        if x1 == 8 and y == 2:
          print("yep")
      else:
        if o_map[x1][y] == 1:
          overlap_count += 1
        o_map[x1][y] += 1
  elif y1 == y2:
    min_x = min(x1,x2)
    max_x = max(x1,x2)
    for x in range(min_x,max_x+1):
      if x not in o_map:
        o_map[x] = {}
      if y1 not in o_map[x]:
        o_map[x][y1] = 1
      else:
        if o_map[x][y1] == 1:
          overlap_count += 1
        o_map[x][y1] += 1
  else:
    x_increasing = x1 <= x2
    y_increasing = y1 <= y2
    temp_x = x1
    temp_y = y1
    while temp_x != x2:
      # Update Occurrences & Overlap Count
      if temp_x not in o_map:
        o_map[temp_x] = {}
      if temp_y not in o_map[temp_x]:
        o_map[temp_x][temp_y] = 1
      else:
        if o_map[temp_x][temp_y] == 1:
          overlap_count += 1
        o_map[temp_x][temp_y] += 1
      # Update X & Y
      if x_increasing:
        temp_x += 1
      else:
        temp_x -= 1
      if y_increasing:
        temp_y += 1
      else:
        temp_y -= 1
    if temp_x not in o_map:
      o_map[temp_x] = {}
    if temp_y not in o_map[temp_x]:
      o_map[temp_x][temp_y] = 1
    else:
      if o_map[temp_x][temp_y] == 1:
        overlap_count += 1
      o_map[temp_x][temp_y] += 1
  return o_map,overlap_count

def pt1():
  line_strings = read_input()
  overlap_count = 0
  o_map = {}
  for line_string in line_strings:
    x1,y1,x2,y2 = build_line_segment(line_string)
    o_map, overlap_count = enumerate_line_segment(x1,y1,x2,y2,o_map,overlap_count)
  return overlap_count

if __name__ == '__main__':
  print(pt1())