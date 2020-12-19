import copy 

def assemble_line_ranges(line):
    post_name = line[line.find(':')+1:]
    parts = post_name.split(' ')
    ranges = []
    for item in parts:
        if '-' in item:
            p1 = int(item.split('-')[0])
            p2 = int(item.split('-')[1])
            ranges.append((p1,p2))
    return ranges

def ticket_values(line):
    line = line.rstrip()
    return [int(i) for i in line.split(',')]

def ranges_and_tickets(input_fp='input.txt'):
    with open(input_fp) as f:
        lines = f.readlines()
        # Taking in Ranges
        i = 0
        ranges = []
        while i < len(lines):
            if lines[i] == '\n':
                break
            sample_range = assemble_line_ranges(lines[i])
            ranges += sample_range
            i += 1
        ranges.sort(key=lambda x:x[0])
        i += 2
        # My ticket
        all_ticket_values = []
        all_ticket_values += ticket_values(lines[i])
        i += 3
        # All other tickets
        while i < len(lines):
            all_ticket_values += ticket_values(lines[i])
            i += 1
        return ranges, all_ticket_values

def in_range(new_ranges,v):
    for r in new_ranges:
        if v < r[0]:
            return False
        elif v >= r[0] and v <= r[1]:
            return True
    return False

def pt1():
    ranges, all_ticket_values = ranges_and_tickets()
    new_ranges = []
    # Compress Ranges
    current_min = ranges[0][0]
    current_max = ranges[0][1]
    for p in ranges:
        if current_max < p[0]:
            new_ranges.append((current_min,current_max))
            current_min = p[0]
            current_max = p[1]
        else:
            current_max = max(p[1],current_max)
    new_ranges.append((current_min,current_max))
    # Evaluate Ticket Values
    sum_ = 0
    for v in all_ticket_values:
        if not in_range(new_ranges,v):
            sum_ += v
    return sum_

def ranges_and_tickets_pt2(input_fp='input.txt'):
    with open(input_fp) as f:
        lines = f.readlines()
        # Taking in Ranges
        i = 0
        ranges = []
        while i < len(lines):
            if lines[i] == '\n':
                break
            sample_range = assemble_line_ranges(lines[i])
            ranges.append(sample_range)
            i += 1
        i += 2
        # My ticket
        all_ticket_values = []
        all_ticket_values.append(ticket_values(lines[i]))
        i += 3
        # All other tickets
        while i < len(lines):
            all_ticket_values.append(ticket_values(lines[i]))
            i += 1
        return ranges, all_ticket_values


def merge_candidate_lists(l1,l2):
    updated = []
    for i in range(len(l1)):
        a = l1[i]
        b = l2[i]
        b = b.intersection(a)

        updated.append(b)
    return updated

def candidates_for_ticket(ranges,ticket):
    candidates = []
    for value in ticket:
        potential_candidates = candidates_for_ticket_value(ranges,value)
        if len(potential_candidates) == 0:
            return []
        candidates.append(potential_candidates)
    return candidates
        

def candidates_for_ticket_value(ranges,value):
    potential_candidates = set()
    for i in range(len(ranges)):
        r = ranges[i]
        if value >= r[0][0] and value <= r[0][1]:
            potential_candidates.add(i)
        elif value >= r[1][0] and value <= r[1][1]:
            potential_candidates.add(i)
    return potential_candidates

def get_matching(potential_matchings):
    final_matching = [-1] * len(potential_matchings)
    found = 0
    while found < len(potential_matchings):
        for i in range(len(potential_matchings)):
            if len(potential_matchings[i]) == 1:
                for item in potential_matchings[i]:
                    final_matching[i] = item
                for j in range(len(potential_matchings)):
                    if final_matching[i] in potential_matchings[j]:
                        potential_matchings[j].remove(final_matching[i])
                found += 1
    return final_matching

def pt2():
    ranges, all_ticket_values = ranges_and_tickets_pt2()
    og = candidates_for_ticket(ranges,all_ticket_values[0])
    for ticket in all_ticket_values[1:]:
        candidates = candidates_for_ticket(ranges,ticket)
        if len(candidates) > 0:
            og = merge_candidate_lists(og,candidates)
    mapping = get_matching(og)
    print(mapping)
    my_ticket = all_ticket_values[0]
    product = 1
    for i in range(len(mapping)):
        if mapping[i] < 6:
            product *= my_ticket[i]
    return product

if __name__ == '__main__':
    print(pt2())