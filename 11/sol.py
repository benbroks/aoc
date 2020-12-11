def generate_2d_matrix(input_fp='input.txt'):
    matrix = []
    with open(input_fp) as f:
        for line in f:
            line = line.rstrip()
            row = []
            for char in line:
                row.append(char)
            matrix.append(row)
    return matrix

def count_seats(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '#':
                count += 1
    return count

def compare_matrices(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True

def adjacent_occupied_pt1(matrix,i,j):
    rows = len(matrix)
    columns = len(matrix[0])
    occupied = 0
    if i > 0 and matrix[i-1][j] == '#':
        occupied += 1
    if j > 0 and matrix[i][j-1] == '#':
        occupied += 1
    if i < rows-1 and matrix[i+1][j] == '#':
        occupied += 1
    if j < columns-1 and matrix[i][j+1] == '#':
        occupied += 1
    if i > 0 and j > 0 and matrix[i-1][j-1] == '#':
        occupied += 1
    if i < rows-1 and j < columns-1 and matrix[i+1][j+1] == '#':
        occupied += 1
    if i > 0 and j < columns-1 and matrix[i-1][j+1] == '#':
        occupied += 1
    if i < rows-1 and j > 0 and matrix[i+1][j-1] == '#':
        occupied += 1
    return occupied
    
def new_status_pt1(matrix,i,j):
    if matrix[i][j] == 'L' and adjacent_occupied_pt1(matrix,i,j) == 0:
        return '#'
    if matrix[i][j] == '#' and adjacent_occupied_pt1(matrix,i,j) >= 4:
        return 'L'
    return matrix[i][j]

def update_matrix_pt1(matrix):
    copy_matrix = [row[:] for row in matrix]
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            copy_matrix[i][j] = new_status_pt1(matrix,i,j)
    return copy_matrix
    
def pt1():
    old = generate_2d_matrix()
    match = False
    while not match:
        new = update_matrix_pt1(old)
        match = compare_matrices(new,old)
        old = new
    return count_seats(old)

def adjacent_occupied_pt2(matrix,i,j):
    rows = len(matrix)
    columns = len(matrix[0])
    occupied = 0
    # Going Up
    sample_i = i-1
    while sample_i >= 0:
        if matrix[sample_i][j] == '#':
            occupied += 1
            break
        if matrix[sample_i][j] == 'L':
            break
        sample_i -= 1
    # Going Down
    sample_i = i+1
    while sample_i < rows:
        if matrix[sample_i][j] == '#':
            occupied += 1
            break
        if matrix[sample_i][j] == 'L':
            break
        sample_i += 1
    # Going Left
    sample_j = j-1
    while sample_j >= 0:
        if matrix[i][sample_j] == '#':
            occupied += 1
            break
        if matrix[i][sample_j] == 'L':
            break
        sample_j -= 1
    # Going Right
    sample_j = j+1
    while sample_j < columns:
        if matrix[i][sample_j] == '#':
            occupied += 1
            break
        if matrix[i][sample_j] == 'L':
            break
        sample_j += 1
    # Upper Left Diagonal
    sample_i, sample_j = i-1,j-1
    while sample_i >=0 and sample_j >= 0:
        if matrix[sample_i][sample_j] == '#':
            occupied += 1
            break
        if matrix[sample_i][sample_j] == 'L':
            break
        sample_i -= 1
        sample_j -= 1
    # Bottom Right Diagonal
    sample_i, sample_j = i+1,j+1
    while sample_i < rows and sample_j < columns:
        if matrix[sample_i][sample_j] == '#':
            occupied += 1
            break
        if matrix[sample_i][sample_j] == 'L':
            break
        sample_i += 1
        sample_j += 1
    # Upper Right Diagonal
    sample_i, sample_j = i-1,j+1
    while sample_i >= 0 and sample_j < columns:
        if matrix[sample_i][sample_j] == '#':
            occupied += 1
            break
        if matrix[sample_i][sample_j] == 'L':
            break
        sample_i -= 1
        sample_j += 1
    # Bottom Left Diagonal
    sample_i, sample_j = i+1,j-1
    while sample_i < rows and sample_j >= 0:
        if matrix[sample_i][sample_j] == '#':
            occupied += 1
            break
        if matrix[sample_i][sample_j] == 'L':
            break
        sample_i += 1
        sample_j -= 1
    return occupied

def new_status_pt2(matrix,i,j):
    if matrix[i][j] == 'L' and adjacent_occupied_pt2(matrix,i,j) == 0:
        return '#'
    if matrix[i][j] == '#' and adjacent_occupied_pt2(matrix,i,j) >= 5:
        return 'L'
    return matrix[i][j]

def update_matrix_pt2(matrix):
    copy_matrix = [row[:] for row in matrix]
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            copy_matrix[i][j] = new_status_pt2(matrix,i,j)
    return copy_matrix

def pt2():
    old = generate_2d_matrix()
    match = False
    while not match:
        new = update_matrix_pt2(old)
        match = compare_matrices(new,old)
        old = new
    return count_seats(old)

if __name__ == "__main__":
    print(pt2())