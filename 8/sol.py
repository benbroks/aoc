def store_instructions(input_fp='input.txt'):
    instructions=[]
    with open(input_fp) as f:
        for line in f:
            instructions.append(line)
    return instructions


def pt1():
    executed = set()
    curr_line = 0
    acc = 0
    instructions = store_instructions()
    while curr_line not in executed:
        cmds = instructions[curr_line].split()
        print(cmds)
        executed.add(curr_line)
        if cmds[0] == 'nop':
            curr_line += 1
        if cmds[0] == 'jmp':
            if cmds[1][0] == '+':
                curr_line += int(cmds[1][1:])
            else:
                curr_line -= int(cmds[1][1:])
        if cmds[0] == 'acc':
            if cmds[1][0] == '+':
                acc += int(cmds[1][1:])
            else:
                acc -= int(cmds[1][1:])
            curr_line += 1
    return acc

def sample_execution(instructions):
    executed = set()
    curr_line = 0
    acc = 0
    while curr_line not in executed and curr_line < len(instructions):
        cmds = instructions[curr_line].split()
        print(cmds)
        executed.add(curr_line)
        if cmds[0] == 'nop':
            curr_line += 1
        if cmds[0] == 'jmp':
            if cmds[1][0] == '+':
                curr_line += int(cmds[1][1:])
            else:
                curr_line -= int(cmds[1][1:])
        if cmds[0] == 'acc':
            if cmds[1][0] == '+':
                acc += int(cmds[1][1:])
            else:
                acc -= int(cmds[1][1:])
            curr_line += 1
    if curr_line == len(instructions):
        return acc
    else:
        return 'fail'


def pt2():
    instructions = store_instructions()
    for i in range(len(instructions)):
        if instructions[i][:3] == 'jmp':
            instructions[i] = 'nop' + instructions[i][3:]
            sample_run = sample_execution(instructions)
            instructions[i] = 'jmp' + instructions[i][3:]
            if sample_run != 'fail':
                return sample_run
        if instructions[i][:3] == 'nop':
            instructions[i] = 'jmp' + instructions[i][3:]
            sample_run = sample_execution(instructions)
            instructions[i] = 'nop' + instructions[i][3:]
            if sample_run != 'fail':
                return sample_run
        else:
            continue
    return 'fail'

if __name__ == '__main__':
    acc = pt2()
    print(acc)