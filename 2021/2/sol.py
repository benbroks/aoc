def populate_commands(input_fp="input.txt"):
    # loading in
    with open(input_fp) as f:
        commands = [line.split() for line in f]
    return commands


def pt1(commands = None):
    if commands is None:
        commands = populate_commands()
    x_position = 0
    y_position = 0
    for word, v in commands:
        v = int(v)
        if word == 'forward':
            x_position += v
        elif word == 'down':
            y_position += v
        else:
            y_position -= v
    return x_position * y_position

def pt2(commands = None):
    if commands is None:
        commands = populate_commands()
    x_position = 0
    y_position = 0
    aim = 0
    for word, v in commands:
        v = int(v)
        if word == 'forward':
            x_position += v
            y_position += aim * v
        elif word == 'down':
            aim += v
        else:
            aim -= v
    return x_position * y_position

if __name__ == "__main__":
    print(pt2())