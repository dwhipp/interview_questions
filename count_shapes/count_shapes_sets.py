kNeighbors_n8 = [(dx, dy) for dx in (-1,0,1)
                          for dy in (-1,0,1)
                          if (dx,dy) != (0,0)]

def GetNeighbors(x, y):
  return ((x+dx, y+dy) for dx, dy in kNeighbors_n8)

def DFS(node_fn, init):
  stack = [init]
  while stack:
    stack.extend(node_fn(*stack.pop()))

def CountShapes(image):
  black_coords = set((x,y) for y in range(len(image))
                           for x in range(len(image[y]))
                           if image[y][x] == 'X')

  def RemoveBlackNeighbors(x, y):
    black_neighbors = black_coords.intersection(GetNeighbors(x, y))
    black_coords.difference_update(black_neighbors)
    return black_neighbors

  count = 0
  while black_coords:
    count += 1
    DFS(RemoveBlackNeighbors, black_coords.pop())
  return count
