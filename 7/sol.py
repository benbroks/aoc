def get_outer_inner_pt1(line):
    parts = line.split()
    outer = parts[0] + ' ' + parts[1]
    i = 2
    inner = []
    while i < len(parts):
        try:
            num_bags = int(parts[i])
            inner.append(parts[i+1] + ' ' + parts[i+2])
            i += 4
        except:
            i += 1
    return outer, inner

def generate_graph_pt1(input_fp='input.txt'):
    connections = {}
    with open(input_fp) as f:
        for line in f:
            outer, inner = get_outer_inner_pt1(line)
            for color in inner:
                if color not in connections:
                    connections[color] = set()
                connections[color].add(outer)
    return connections

def get_outer_inner_pt2(line):
    parts = line.split()
    outer = parts[0] + ' ' + parts[1]
    i = 2
    inner = []
    while i < len(parts):
        try:
            num_bags = int(parts[i])
            inner.append((num_bags,parts[i+1] + ' ' + parts[i+2]))
            i += 4
        except:
            i += 1
    return outer, inner

def generate_graph_pt2(input_fp='input.txt'):
    connections = {}
    with open(input_fp) as f:
        for line in f:
            outer, inner = get_outer_inner_pt2(line)
            connections[outer] = {}
            for p in inner:
                connections[outer][p[1]] = p[0]
    return connections

def how_many_bags(connections,color):
    if len(connections[color]) == 0:
        return 1
    else:
        how_many = 1
        for item in connections[color]:
            how_many += connections[color][item] * how_many_bags(connections,item)
        return how_many

def pt1():
    connections = generate_graph_pt1()
    to_explore = ['shiny gold']
    seen = set()
    while len(to_explore) > 0:
        p = to_explore[0]
        to_explore = to_explore[1:]
        seen.add(p)
        if p in connections:
            for new_p in connections[p]:
                if new_p not in seen:
                    to_explore.append(new_p)
    return len(seen) - 1

def pt2():
    connections = generate_graph_pt2()
    inside = how_many_bags(connections,'shiny gold') - 1
    print(inside)

if __name__ == '__main__':
    pt2()

