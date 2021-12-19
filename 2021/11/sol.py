def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def flash_octopus(i,j,to_flash,m):
  n = len(m)
  if i-1 >= 0:
    # Top
    if m[i-1][j] > 0:
      m[i-1][j] += 1
      if m[i-1][j] > 9:
        to_flash.add((i-1,j))
    # Upper Left
    if j-1 >= 0:
      if m[i-1][j-1] > 0:
        m[i-1][j-1] += 1
        if m[i-1][j-1] > 9:
          to_flash.add((i-1,j-1))
    # Upper Right
    if j+1 < n:
      if m[i-1][j+1] > 0:
        m[i-1][j+1] += 1
        if m[i-1][j+1] > 9:
          to_flash.add((i-1,j+1))
  if i+1 < n:
    # Bottom
    if m[i+1][j] > 0:
      m[i+1][j] += 1
      if m[i+1][j] > 9:
        to_flash.add((i+1,j))
    # Bottom Left
    if j-1 >= 0:
      if m[i+1][j-1] > 0:
        m[i+1][j-1] += 1
        if m[i+1][j-1] > 9:
          to_flash.add((i+1,j-1))
    # Bottom Right
    if j+1 < n:
      if m[i+1][j+1] > 0:
        m[i+1][j+1] += 1
        if m[i+1][j+1] > 9:
          to_flash.add((i+1,j+1))
  # Left
  if j-1 >= 0:
    if m[i][j-1] > 0:
      m[i][j-1] += 1
      if m[i][j-1] > 9:
        to_flash.add((i,j-1))
  # Right
  if j+1 < n:
    if m[i][j+1] > 0:
      m[i][j+1] += 1
      if m[i][j+1] > 9:
        to_flash.add((i,j+1))
  m[i][j] = 0
  return to_flash,m

def update_array(m):
  n = len(m)
  to_flash = set()
  flash_count = 0
  # Increment Every Value by 1
  for i in range(n):
    for j in range(n):
      m[i][j] += 1
      if m[i][j] > 9:
        to_flash.add((i,j))
  while len(to_flash) > 0:    
    p = to_flash.pop()
    flash_count += 1
    to_flash, m = flash_octopus(p[0],p[1],to_flash,m)
  return m, flash_count

def pt1():
    input_lines = read_input()
    m = []
    total_flash_count = 0
    for l in input_lines:
      m.append([int(c) for c in l])
    for _ in range(100):
      m, flash_count = update_array(m)
      total_flash_count += flash_count
    return total_flash_count

def pt2():
    input_lines = read_input()
    m = []
    for l in input_lines:
      m.append([int(c) for c in l])
    steps = 0
    flash_count = 0
    while flash_count != len(m)**2:
      m, flash_count = update_array(m)
      steps += 1
    return steps

if __name__ == '__main__':
    print(pt2())