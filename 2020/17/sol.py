def parse_text(input_fp='input.txt'):
    states = {}
    with open(input_fp) as f:
        y = 0
        for line in f:
            line = line.rstrip()
            for x in range(len(line)):
                if x not in states:
                    states[x] = {}
                if y not in states[x]:
                    states[x][y] = {}
                if line[x] == '.':
                    states[x][y][0] = 0
                else:
                    states[x][y][0] = 1
            y += 1
    return states

def generate_neighbors(x,y,z):
    potential = [-1,0,1]
    neighbors = set()
    for i in potential:
        for j in potential:
            for k in potential:
                if i != 0 or j != 0 or k != 0:
                    neighbors.add((x+i,y+j,z+k))
    return neighbors

def active_neighbors(states,neighbors):
    total = 0
    for n in neighbors:
        x,y,z = n[0],n[1],n[2]
        if x in states and y in states[x] and z in states[x][y]:
            total += states[x][y][z]
    return total

def update_neighborhood(states):
    all_neighbors = set()
    new_states = {}
    # Generate Neighbors
    for x in states:
        for y in states[x]:
            for z in states[x][y]:
                neighbors = generate_neighbors(x,y,z)
                all_neighbors.update(neighbors)
    # Determine Active Members
    for loc in all_neighbors:
        x,y,z = loc[0],loc[1],loc[2]
        local_neighbors = generate_neighbors(x,y,z)
        actives = active_neighbors(states,local_neighbors)
        if x not in new_states:
            new_states[x] = {}
        if y not in new_states[x]:
            new_states[x][y] = {}
        if x in states and y in states[x] and z in states[x][y] and states[x][y][z] == 1:
            if actives == 2 or actives == 3:
                new_states[x][y][z] = 1
            else:
                new_states[x][y][z] = 0
        else:
            if actives == 3:
                new_states[x][y][z] = 1
            else:
                new_states[x][y][z] = 0
    return new_states

def total_active(states):
    total = 0
    for x in states:
        for y in states[x]:
            for z in states[x][y]:
                total += states[x][y][z]
    return total
        
def pt1():
    states = parse_text()
    for i in range(6):
        states = update_neighborhood(states)
    return total_active(states)
    
def parse_text_pt2(input_fp='input.txt'):
    states = {}
    with open(input_fp) as f:
        y = 0
        z = 0
        w = 0
        for line in f:
            line = line.rstrip()
            for x in range(len(line)):
                if x not in states:
                    states[x] = {}
                if y not in states[x]:
                    states[x][y] = {}
                if z not in states[x][y]:
                    states[x][y][z] = {}
                if line[x] == '.':
                    states[x][y][z][w] = 0
                else:
                    states[x][y][z][w] = 1
            y += 1
    return states

def generate_neighbors_pt2(x,y,z,w):
    potential = [-1,0,1]
    neighbors = set()
    for i in potential:
        for j in potential:
            for k in potential:
                for l in potential:
                    if i != 0 or j != 0 or k != 0 or l != 0:
                        neighbors.add((x+i,y+j,z+k,w+l))
    return neighbors

def active_neighbors_pt2(states,neighbors):
    total = 0
    for n in neighbors:
        x,y,z,w = n[0],n[1],n[2],n[3]
        if x in states and y in states[x] and z in states[x][y] and w in states[x][y][z]:
            total += states[x][y][z][w]
    return total

def update_neighborhood_pt2(states):
    all_neighbors = set()
    new_states = {}
    # Generate Neighbors
    for x in states:
        for y in states[x]:
            for z in states[x][y]:
                for w in states[x][y][z]:
                    neighbors = generate_neighbors_pt2(x,y,z,w)
                    all_neighbors.update(neighbors)
    # Determine Active Members
    for loc in all_neighbors:
        x,y,z,w = loc[0],loc[1],loc[2],loc[3]
        local_neighbors = generate_neighbors_pt2(x,y,z,w)
        actives = active_neighbors_pt2(states,local_neighbors)
        if x not in new_states:
            new_states[x] = {}
        if y not in new_states[x]:
            new_states[x][y] = {}
        if z not in new_states[x][y]:
            new_states[x][y][z] = {}
        if x in states and y in states[x] and z in states[x][y] and w in states[x][y][z] and states[x][y][z][w] == 1:
            if actives == 2 or actives == 3:
                new_states[x][y][z][w] = 1
            else:
                new_states[x][y][z][w] = 0
        else:
            if actives == 3:
                new_states[x][y][z][w] = 1
            else:
                new_states[x][y][z][w] = 0
    return new_states

def total_active_pt2(states):
    total = 0
    for x in states:
        for y in states[x]:
            for z in states[x][y]:
                for w in states[x][y][z]:
                    total += states[x][y][z][w]
    return total

def pt2():
    states = parse_text_pt2()
    for _ in range(6):
        states = update_neighborhood_pt2(states)
    return total_active_pt2(states)

if __name__ =='__main__':
    print(pt2())