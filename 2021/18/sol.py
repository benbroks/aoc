def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

class Node:
    def __init__(self,l,parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        if isinstance(l,int):
            self.val = l
        else:
            self.val = None
        if not isinstance(l,int):
            self.left = Node(l[0],self)
            self.right = Node(l[1],self)
        
    def __add__(self,other):
        result = Node([1,1])
        result.left = self
        self.parent = result
        result.right = other
        other.parent = result
        result.update_layer_from_root()
        return result
        
    def update_layer_from_root(self):
        if self.parent is None:
            self.layer = 0
        else:
            self.layer = self.parent.layer + 1
        if self.left is not None:
            self.left.update_layer_from_root()
        if self.right is not None:
            self.right.update_layer_from_root()
    
    def __str__(self):
        if isinstance(self.val,int):
            return self.val.__str__()
        else:
            return "[{},{}]".format(self.left.__str__(), self.right.__str__())
    
    def magnitude(self):
        if isinstance(self.val,int):
            return self.val
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()
    
def find_exploding_pair(p):
    if p is None:
        return None
    if p.layer == 4 and not isinstance(p.val,int):
        return p
    a = find_exploding_pair(p.left)
    if a is None:
        return find_exploding_pair(p.right)
    else:
        return a

def find_split_value(p):
    if p is None:
        return None
    if isinstance(p.val,int) and p.val >= 10:
        return p
    a = find_split_value(p.left)
    if a is None:
        return find_split_value(p.right)
    else:
        return a

def l2r_ordering(n):
    if n is None:
        return []
    if isinstance(n.val,int):
        return [n]
    return l2r_ordering(n.left) + l2r_ordering(n.right)

def find_next_left_val(node_ordering,l_node):
    idx = node_ordering.index(l_node)
    if idx == 0:
        return None
    return node_ordering[idx-1]

def find_next_right_val(node_ordering,r_node):
    idx = node_ordering.index(r_node)
    if idx == len(node_ordering)-1:
        return None
    return node_ordering[idx+1]

def explode(n,ordering):
    l = find_next_left_val(ordering,n.left)
    r = find_next_right_val(ordering,n.right)
    if l is not None:
        l.val += n.left.val
    if r is not None:
        r.val += n.right.val
    n.left = None
    n.right = None
    n.val = 0
    while n.parent is not None:
        n = n.parent
    return n

def split(n):
    if n.val % 2 == 1:
        l = int((n.val-1)/2)
        r = int((n.val+1)/2)
    else:
        l, r = int(n.val/2), int(n.val/2)
    l_n = Node(l,n)
    r_n = Node(r,n)
    n.val = [l,r]
    n.left = l_n
    n.right = r_n
    n.update_layer_from_root()
    while n.parent is not None:
        n = n.parent
    return n

def reduce_once(p,a,b):
    if a is not None:
        ordering = l2r_ordering(p) 
        p = explode(a,ordering)
    elif b is not None:
        p = split(b)
    return p
    

def reduce(p):
    a = find_exploding_pair(p)
    b = find_split_value(p)
    while a is not None or b is not None:
        if a is not None:
            ordering = l2r_ordering(p) 
            p = explode(a,ordering)
        elif b is not None:
            p = split(b)
        a = find_exploding_pair(p)   
        b = find_split_value(p)
    return p

def pt1():
    input_lines = read_input()
    literal_lines = [Node(eval(i)) for i in input_lines]
    while len(literal_lines) > 1:
        l = literal_lines[0]
        l.update_layer_from_root()
        r = literal_lines[1]
        r.update_layer_from_root()
        p = l+r
        p.update_layer_from_root()
        p = reduce(p)
        literal_lines = [p] + literal_lines[2:]
    return literal_lines[0].magnitude()

def pt2():
    input_lines = read_input()
    max_magnitude = 0
    n = len(input_lines)
    for i in range(n):
        for j in range(i+1,n):
            literal_lines = [Node(eval(k)) for k in input_lines]
            l = literal_lines[i]
            l.update_layer_from_root()
            r = literal_lines[j]
            r.update_layer_from_root()
            c = l+r
            c.update_layer_from_root
            c = reduce(c)
            max_magnitude = max(max_magnitude,c.magnitude())
            literal_lines = [Node(eval(k)) for k in input_lines]
            l = literal_lines[i]
            l.update_layer_from_root()
            r = literal_lines[j]
            r.update_layer_from_root()
            d = r+l
            d.update_layer_from_root
            d = reduce(d)
            max_magnitude = max(max_magnitude,d.magnitude())
    return max_magnitude
    

if __name__ == "__main__":
    print(pt2())        
