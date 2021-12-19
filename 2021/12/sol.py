from os import path
import copy


def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def traverse_graph_pt2(graph, seen_caves, path_traversed, double_visit):
    current_node = path_traversed[-1]
    if current_node == 'end':
        return 1
    num_unique_paths = 0
    for n in graph[current_node]:
        if n[0].isupper():
            num_unique_paths += traverse_graph_pt2(graph, seen_caves, path_traversed + [n], double_visit)
        else:
            if n not in seen_caves:
                sc_copy = copy.deepcopy(seen_caves)
                sc_copy[n] = 1
                num_unique_paths += traverse_graph_pt2(graph, sc_copy, path_traversed + [n], double_visit)
            elif seen_caves[n] == 1 and not double_visit and n != 'start':
                sc_copy = copy.deepcopy(seen_caves)
                sc_copy[n] += 1
                num_unique_paths += traverse_graph_pt2(graph, sc_copy, path_traversed + [n], True)
    return num_unique_paths

def traverse_graph_pt1(graph, seen_caves, path_traversed):
    current_node = path_traversed[-1]
    if current_node == 'end':
        return 1
    num_unique_paths = 0
    for n in graph[current_node]:
        if n[0].islower():
            if n in seen_caves:
                continue
            else:
                sc_copy = copy.deepcopy(seen_caves)
                sc_copy[n] = 1
                num_unique_paths += traverse_graph_pt1(graph, sc_copy, path_traversed + [n])
        else:
            num_unique_paths += traverse_graph_pt1(graph, seen_caves, path_traversed + [n])
    return num_unique_paths

def pt1():
    graph = {}
    input_lines = read_input()
    for l in input_lines:
        nodes = l.split('-')
        n1 = nodes[0]
        n2 = nodes[1]
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
        
    seen_small_caves = {'start':1}
    path_traversed = ['start']
    num_unique_paths = traverse_graph_pt1(graph, seen_small_caves, path_traversed)
    return num_unique_paths

def pt2():
    graph = {}
    input_lines = read_input()
    for l in input_lines:
        nodes = l.split('-')
        n1 = nodes[0]
        n2 = nodes[1]
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
        
    seen_small_caves = {'start':1}
    path_traversed = ['start']
    num_unique_paths = traverse_graph_pt2(graph, seen_small_caves, path_traversed, False)
    return num_unique_paths

if __name__ == '__main__':
    print(pt2())