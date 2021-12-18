def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def pt1():
    line_strings = read_input()
    fish_sequence = [int(n) for n in line_strings[0].split(',')]
    num_fishes = 0
    for f in fish_sequence:
        num_fishes += lantern_children(f,80)
    return num_fishes

def pt2():
    line_strings = read_input()
    fish_sequence = [int(n) for n in line_strings[0].split(',')]
    dplc = DpLanternChildren(max_wait=8, max_days=256)
    total_fishes = 0
    for f in fish_sequence:
        total_fishes += dplc.num_fishes(f,256)
    return total_fishes
    

class DpLanternChildren:
    def __init__(self, max_wait, max_days):
        self.memo = []
        self.max_wait = max_wait
        self.max_days = max_days
        for _ in range(max_wait+1):
            self.memo.append([0]*(max_days+1))
        for days_left in range(max_days+1):
            for days_until_child in range(max_wait+1):
                if days_until_child >= days_left:
                    self.memo[days_until_child][days_left] = 1
                else:
                    self.memo[days_until_child][days_left] = self.memo[6][days_left-days_until_child-1] + self.memo[8][days_left-days_until_child-1]
    
    def num_fishes(self, timer, num_days):
        if timer <= self.max_wait and num_days <= self.max_days:
            return self.memo[timer][num_days]
        else:
            return 0
    
def lantern_children(timer_value, n):
    if n < 0:
        return 0
    if timer_value >= n:
        return 1
    return lantern_children(6,n-timer_value-1) + lantern_children(8,n-timer_value-1)
    

if __name__ == '__main__':
    print(pt2())