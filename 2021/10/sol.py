def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def valid_chunk(chunk_str):
    stack = []
    opposites = {"]":"[", "}":"{", ">":"<", ")":"("}
    for c in chunk_str:
        if c == "[" or c == "(" or c == "{" or c == "<":
            stack.append(c)
        else:
            if opposites[c] != stack[-1]:
                return c
            stack.pop()
    return ""

def pt1():
    input_lines = read_input()
    final_score = 0
    score_map = {")":3, "]":57, "}":1197, ">": 25137}
    for l in input_lines:
        c = valid_chunk(l)
        if c in score_map:
            final_score += score_map[c]
    return final_score

def pt2_incomplete_checker(chunk_str):
    stack = []
    opposites = {"]":"[", "}":"{", ">":"<", ")":"("}
    inv_opposites = {v: k for k, v in opposites.items()}
    for c in chunk_str:
        if c == "[" or c == "(" or c == "{" or c == "<":
            stack.append(c)
        else:
            if opposites[c] != stack[-1]:
                return []
            stack.pop()
    if len(stack) > 1:
        return [inv_opposites[s] for s in reversed(stack)]
    return []

def pt2():
    input_lines = read_input()
    score_list = []
    score_map = {")":1, "]":2, "}":3, ">": 4}
    for l in input_lines:
        to_complete = pt2_incomplete_checker(l)
        if len(to_complete) > 0:
            score_list.append(0)
        for c in to_complete:
            score_list[-1] *= 5
            score_list[-1] += score_map[c]
    score_list.sort()
    n = len(score_list)
    return score_list[int((n-1)/2)]


if __name__ == '__main__':
    print(pt2())