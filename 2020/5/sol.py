def get_seat_id(line,num_row_digits=7,num_col_digits=3):
    # Get Row
    row_num = 0
    col_num = 0
    for i in range(num_row_digits):
        if line[i] == 'B':
            row_num += 2**(num_row_digits-i-1)
    for j in range(num_row_digits,num_row_digits+num_col_digits):
        if line[j] == 'R':
            col_num += 2**(num_col_digits-(j-num_row_digits)-1)
    return row_num*8 + col_num


def pt1(input_fp="input.txt"):
    max_id = 0
    with open(input_fp) as f:
        for line in f:
            max_id = max(get_seat_id(line),max_id)
    return max_id

def pt2(input_fp="input.txt"):
    filled_seats = set()
    with open(input_fp) as f:
        for line in f:
            filled_seats.add(get_seat_id(line))
    
    for i in range(2**10):
        if i not in filled_seats:
            if i+1 in filled_seats and i-1 in filled_seats:
                return i


if __name__ == "__main__":
    print(pt2())