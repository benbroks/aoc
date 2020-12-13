def decode_instruction_pt1(line, curr_direction):
    command = line[0]
    value = int(line[1:])
    x_diff, y_diff = 0, 0
    if command == 'R':
        curr_direction += value
        curr_direction = curr_direction % 360
    elif command == 'L':
        curr_direction -= value
        curr_direction = curr_direction % 360
    elif command == 'F':
        if curr_direction == 0:
            y_diff = value
        elif curr_direction == 90:
            x_diff = value
        elif curr_direction == 180:
            y_diff = -1*value
        else:
            x_diff = -1*value
    elif command == 'N':
        y_diff = value
    elif command == 'E':
        x_diff = value
    elif command == 'S':
        y_diff = -1*value
    elif command == 'W':
        x_diff = -1*value
    return x_diff, y_diff, curr_direction

def pt1(input_fp='input.txt'):
    curr_x = 0
    curr_y = 0
    curr_direction = 90
    with open(input_fp) as f:
        for line in f:
            x_diff, y_diff, curr_direction = decode_instruction_pt1(line, curr_direction)
            curr_x += x_diff
            curr_y += y_diff
    return abs(curr_y) + abs(curr_x)

def decode_instruction_pt2(line, waypoint_x, waypoint_y):
    command = line[0]
    value = int(line[1:])
    x_diff, y_diff = 0, 0
    if command == 'R' or command == 'L':
        if (command == 'R' and value == 90) or (command == 'L' and value == 270):
            waypoint_x, waypoint_y = waypoint_y, -1*waypoint_x
        elif (command == 'L' and value == 90) or (command == 'R' and value == 270):
            waypoint_x, waypoint_y = -1*waypoint_y, waypoint_x
        else:
            waypoint_x, waypoint_y = -1*waypoint_x, -1*waypoint_y
    elif command == 'F':
        x_diff = waypoint_x*value
        y_diff = waypoint_y*value
    elif command == 'N':
        waypoint_y += value
    elif command == 'E':
        waypoint_x += value
    elif command == 'S':
        waypoint_y -= value
    elif command == 'W':
       waypoint_x -= value
    return x_diff, y_diff, waypoint_x, waypoint_y



def pt2(input_fp='input.txt'):
    waypoint_x = 10
    waypoint_y = 1
    curr_x = 0
    curr_y = 0
    with open(input_fp) as f:
        for line in f:
            x_diff, y_diff, waypoint_x, waypoint_y = decode_instruction_pt2(line, waypoint_x, waypoint_y)
            curr_x += x_diff
            curr_y += y_diff
    return abs(curr_y) + abs(curr_x)
        
if __name__ == '__main__':
    print(pt2())
