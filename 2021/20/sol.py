import numpy as np

def read_input(input_fp="input.txt"):
  with open(input_fp) as f:
      line_strings = [line.strip() for line in f]
  return line_strings

def bin_to_dec(bin_str):
  n = len(bin_str)
  value = 0
  for i,v in enumerate(bin_str):
    value += int(v)*(2**(n-i-1))
  return value

def add_padding(m: np.ndarray, pad_val: int) -> np.ndarray:
  if pad_val == 0:
    new_array = np.zeros((m.shape[0] + 4, m.shape[1] + 4))
  else:
    new_array = np.ones((m.shape[0] + 4, m.shape[1] + 4))
  new_array[2:-2, 2:-2] = m
  return new_array
  
def get_binary_number_from_map_location(i:int,j:int,m:np.ndarray) -> int:
  pass

def enhance(image: np.ndarray, encoding: np.ndarray, pad_val: int):
  image = add_padding(image, pad_val)
  kernel_idxs = np.array([[[i, j] for j in range(-1, 2)] for i in range(-1, 2)]).reshape(-1, 2)

  x_idxs = np.arange(1, image.shape[0] - 1)
  y_idxs = np.arange(1, image.shape[1] - 1)
  XX, YY = np.meshgrid(x_idxs, y_idxs)
  pairs = np.stack((XX, YY)).transpose(1,2,0).reshape(-1, 2)
  
  indexed_points = np.expand_dims(kernel_idxs, 0) + np.expand_dims(pairs, 1)
  ip = indexed_points.reshape(-1, 2)
  results = image[ip[:,0], ip[:,1]].reshape(*indexed_points.shape[:2])
  powers_of_two = (2 ** np.arange(8,-1,-1)).reshape(1, -1)
  encoding_indices = (results * powers_of_two).sum(1).astype(int) 
  transformed = np.transpose(encoding[encoding_indices].reshape(*XX.shape))
      
  return transformed

def pt1():
  # Make algorithm array
  # Make map array
  input_lines = read_input()
  encoding = np.array([i for i in input_lines[0]]) == '#'
  image = np.array([np.array([j for j in i]) for i in input_lines[2:]]) == "#"
  print(image.shape)
  for i in range(2):
    if i > 0 and encoding[0] == True:
      image = enhance(image, encoding,1)
    else:
      image = enhance(image, encoding,0)
  print(image.shape)
  cast = np.zeros(image.shape)
  cast[image] = 1
  return int(np.sum(cast))

def pt2():
  # Make algorithm array
  # Make map array
  input_lines = read_input()
  encoding = np.array([i for i in input_lines[0]]) == '#'
  image = np.array([np.array([j for j in i]) for i in input_lines[2:]]) == "#"
  print(image.shape)
  for i in range(50):
    if i == 0 or (not encoding[0]):
      image = enhance(image, encoding,0)
    else:
      if not encoding[-1]:
        image = enhance(image, encoding,i%2)
      else:
        image = enhance(image, encoding,1)
    
  cast = np.zeros(image.shape)
  cast[image] = 1
  return int(np.sum(cast))

if __name__ == '__main__':
  print(pt2())