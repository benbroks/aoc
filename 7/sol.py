def get_outer_inner(line):
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

def generate_graph(input_fp='input.txt'):
    connections = {}
    with open(input_fp) as f:
        for line in f:
            outer, inner = get_outer_inner(line)
            for color in inner:
                if color not in connections:
                    connections[color] = set()
                connections[color].add(outer)
    return connections

def pt1():
    connections = generate_graph()
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



if __name__ == '__main__':
    print(pt1())

