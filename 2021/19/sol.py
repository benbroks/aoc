from os import read


def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

class Point:
    def __init__(self,x1,x2,x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    
    def __eq__(self, other):
        return self.x1 == other.x1 and self.x2 == other.x2 and self.x3 == other.x3
    
    def __sub__(self, other):
        return Point(self.x1-other.x1,self.x2-other.x2,self.x3-other.x3)
    
    def __add__(self, other):
        return Point(self.x1+other.x1,self.x2+other.x2,self.x3+other.x3)
    
    def __hash__(self):
        return hash((self.x1,self.x2,self.x3))
    
    def __str__(self):
        return "({},{},{})".format(self.x1, self.x2, self.x3)
    
    def switch_dim(self,d1,d2):
        d1,d2 = min(d1,d2),max(d1,d2)
        if d1 <= 2 and d2 <= 2 and d1 != d2:
            if d1 == 0:
                if d2 == 1:
                    self.x1, self.x2 = self.x2, self.x1
                if d2 == 2:
                    self.x1, self.x3 = self.x3, self.x1
            if d1 == 1:
                self.x2, self.x3 = self.x3, self.x2
    
    def flip_dim(self,d1):
        if d1 == 0:
            self.x1 *= -1
        elif d1 == 1:
            self.x2 *= -1
        else:
            self.x3 *= -1

    def pt1():
        input_lines = read_input()
        pcs = []
        pc = set()
        for l in input_lines:
            if l == "":
                pcs.append(pc)
                pc = set()
            elif l[:3] != "---":
                dims = l.split(',')
                p = Point(dims[0],dims[1],dims[2])
                pc.add(p)
        for pc in pcs:
            print(len(pc))
    
if __name__ == '__main__':
    pt1()