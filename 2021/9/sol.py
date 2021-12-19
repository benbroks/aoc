def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def is_low_point(i,j,depth_map):
    num_rows = len(depth_map)
    num_cols = len(depth_map[0])
    candidates = []
    if i-1 >= 0:
        candidates.append(depth_map[i-1][j])
    if i+1 < num_rows:
        candidates.append(depth_map[i+1][j])
    if j-1 >= 0:
        candidates.append(depth_map[i][j-1])
    if j+1 < num_cols:
        candidates.append(depth_map[i][j+1])
    current_num = depth_map[i][j]
    is_min = True
    for c in candidates:
        if current_num >= c:
            is_min = False
    return is_min

def pt1():
    input_lines = read_input()
    depth_map = []
    
    for l in input_lines:
        depth_map.append([int(i) for i in l])
    low_points = []
    num_rows = len(depth_map)
    num_cols = len(depth_map[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if is_low_point(i,j,depth_map):
                low_points.append(depth_map[i][j])
    
    return sum(low_points) + len(low_points)

def mark_basin_center(i,j,depth_map,basin_low_point,o_map):
    if basin_low_point[i][j] is not None or depth_map[i][j] == 9:
        return basin_low_point, o_map
    num_rows = len(depth_map)
    num_cols = len(depth_map[0])
    candidates = []
    if i-1 >= 0:
        candidates.append((i-1,j))
    if i+1 < num_rows:
        candidates.append((i+1,j))
    if j-1 >= 0:
        candidates.append((i,j-1))
    if j+1 < num_cols:
        candidates.append((i,j+1))
    candidates.sort(key=lambda x:depth_map[x[0]][x[1]])
    flow_towards = candidates[0]
    basin_low_point, o_map = mark_basin_center(flow_towards[0],flow_towards[1],depth_map,basin_low_point,o_map)
    basin_low_point[i][j] = basin_low_point[flow_towards[0]][flow_towards[1]]
    o_map[basin_low_point[flow_towards[0]][flow_towards[1]]] += 1
    return basin_low_point, o_map
    
def pt2():
    input_lines = read_input()
    depth_map = []
    basin_low_point = []
    o_map = {}
    
    for l in input_lines:
        depth_map.append([int(i) for i in l])
        basin_low_point.append([None]*len(l))
    low_points = []
    num_rows = len(depth_map)
    num_cols = len(depth_map[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if is_low_point(i,j,depth_map):
                low_points.append(depth_map[i][j])
                basin_low_point[i][j] = "{},{}".format(i,j)
                o_map[basin_low_point[i][j]] = 1
    for i in range(num_rows):
        for j in range(num_cols):
            basin_low_point,o_map = mark_basin_center(i,j,depth_map,basin_low_point,o_map)
    basin_sizes= o_map.values()
    basin_sizes.sort(reverse=True)
    result = 1
    for b_s in basin_sizes[:3]:
        result *= b_s
    return result


if __name__ == '__main__':
    print(pt2())