from os import read


def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

class Edge:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def get_f(self):
        return (self.x1,self.y1)

    def get_t(self):
        return (self.x2,self.y2)

    def __eq__(self, other):
        return self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2
    
    def __hash__(self):
        return hash((self.x1,self.x2,self.y1,self.y2))
    
    def __str__(self):
        return "({},{}) -> ({},{})".format(self.x1, self.y1, self.x2, self.y2)

def dijkstra(m):
    n = len(m)
    distance_map = []
    for _ in range(n):
        distance_map.append([-1]*n)
    distance_map[0][0] = 0
    to_visit = set()
    to_visit.add(Edge(0,0,0,1))
    to_visit.add(Edge(0,0,1,0))
    # Find Minimum Edge
    while distance_map[n-1][n-1] == -1:
        min_weight = None
        min_edge = None
        to_remove = set()
        for e in to_visit:
            f = e.get_f()
            t = e.get_t()
            if distance_map[t[0]][t[1]] != -1:
                to_remove.add(e)
            if min_weight is None:
                min_weight = distance_map[f[0]][f[1]] + int(m[t[0]][t[1]])
                min_edge = e
            else:
                if min_weight > distance_map[f[0]][f[1]] + int(m[t[0]][t[1]]):
                    min_weight = distance_map[f[0]][f[1]] + int(m[t[0]][t[1]])
                    min_edge = e
        # Apply Minimum Edge
        f = min_edge.get_f()
        t = min_edge.get_t()
        if distance_map[t[0]][t[1]] == -1:
            distance_map[t[0]][t[1]] = min_weight
            if t[0]-1 >= 0:
                to_visit.add(Edge(t[0],t[1],t[0]-1,t[1]))
            if t[0]+1 < n:
                to_visit.add(Edge(t[0],t[1],t[0]+1,t[1]))
            if t[1]-1 >= 0:
                to_visit.add(Edge(t[0],t[1],t[0],t[1]-1))
            if t[1]+1 < n:
                to_visit.add(Edge(t[0],t[1],t[0],t[1]+1))
            to_remove.add(min_edge)
        for e in to_remove:
            to_visit.remove(e)
        
    return distance_map[n-1][n-1]

def construct_new_map(m):
    n = len(m)
    # Add Rows
    for i in range(4):
        for j in range(n):
            new_row = ''.join([str(int(k)+i+1) if int(k)+i+1 <= 9 else str(int(k)+i+1-9) for k in m[j]])
            m.append(new_row)
    # Add Columns
    for i in range(4):
        for j in range(5*n):
            m[j] = m[j] + ''.join([str(int(k)+i+1) if int(k)+i+1 <= 9 else str(int(k)+i+1-9) for k in m[j][:n]])
    return m                        

def pt1():
    input_lines = read_input()
    m = []
    n = len(input_lines)
    for l in input_lines:
        m.append(l)
    
    return dijkstra(m)

def pt2():
    input_lines = read_input()
    m = []
    n = len(input_lines)
    for l in input_lines:
        m.append(l)
    updated_m = construct_new_map(m)
    
    return dijkstra(updated_m)

if __name__ == '__main__':
    print(pt2())