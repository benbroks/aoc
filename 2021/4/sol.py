def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

class Board:
  def __init__(self, input_array):
    self.input_array = input_array
    self.unmarked_set = set()
    self.num_to_coord = {}
    for i in range(5):
      for j in range(5):
        item = input_array[i][j]
        self.unmarked_set.add(item)
        self.num_to_coord[item] = i,j
    self.row_sums = 5*[0]
    self.col_sums = 5*[0]
    self.won = False
  
  def mark_cell(self, num):
    if num not in self.unmarked_set:
      return -1
    self.unmarked_set.remove(num)
    i,j = self.num_to_coord[num]
    self.row_sums[i] += 1
    self.col_sums[j] += 1
    if self.row_sums[i] == 5 or self.col_sums[j] == 5:
      self.won = True
      return sum([int(n) for n in self.unmarked_set])*int(num)
    return -1
  
  def __str__(self):
    rep = ""
    for item in self.input_array:
      rep += item.__str__() + "\n"
    return rep

def pt1():
  line_strings = read_input()
  drawings = line_strings[0].split(',')
  num_boards = int((len(line_strings) - 1)/6)
  master_board_list = []
  # Construct Boards
  for i in range(num_boards):
    where_board_is = line_strings[2+6*i:7+6*i]
    input_array = [line.split() for line in where_board_is]
    master_board_list.append(Board(input_array))
  # Run Drawings
  num_worth_checking = len(master_board_list)
  for d in drawings:
    for b in master_board_list:
      if not b.won:
        did_we_win = b.mark_cell(d)
        if did_we_win > -1:
          if num_worth_checking == 1:
            return did_we_win
          else:
            num_worth_checking -= 1

if __name__ == '__main__':
  print(pt1())