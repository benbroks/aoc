def update_set_pt1(line, temp):
    for char in line:
        temp.add(char)
    return temp

def update_set_pt2(line,temp):
    if 'placeholder' in temp:
        temp.remove('placeholder')
        for char in line:
            temp.add(char)
        return temp
    else:
        new_set = set()
        for char in line:
            if char in temp:
                new_set.add(char)
        return new_set

def pt1(input_fp="input.txt"):
    with open(input_fp) as f:
        question_sum = 0
        temp_questions = set()
        for line in f:
            if line == '\n':
                question_sum += len(temp_questions)
                temp_questions = set()
            else:
                line = line.rstrip()
                temp_questions = update_set_pt1(line,temp_questions) 
        question_sum += len(temp_questions)
    return question_sum

def pt2(input_fp="input.txt"):
    with open(input_fp) as f:
        question_sum = 0
        temp_questions = set(['placeholder'])
        for line in f:
            if line == '\n':
                question_sum += len(temp_questions)
                temp_questions = set(['placeholder'])
            else:
                line = line.rstrip()
                temp_questions = update_set_pt2(line,temp_questions) 
        question_sum += len(temp_questions)
    return question_sum


if __name__ == "__main__":
    print(pt2())