def CountShapes(image):
  """Counts the number of shapes in an image.

  Args:
    image: a list of lists of pixels. A pixel is represented as a string; if
        it's value is 'X' then the pixel is considered black, and thus part of'
        a shape.

  Returns:
    a count of the number of connected groups of black pixels in the image.
  """
  visited = [[False] * len(row) for row in image]

  def IsUnvistedBlackPixel(x, y):
    """Checks if we need to process a pixel."""
    if x < 0 or y < 0 or y >= len(image) or x >= len(image[y]) or visited[y][x]:
      return False
    return image[y][x] == 'X'

  def GetNeighbors(x, y):
    """Generates the coordinates of the 8 neighboring pixels."""
    for dx in (-1,0,1):
      for dy in (-1,0,1):
        if (dx,dy) != (0,0):
          yield (x+dx, y+dy)

  def MaybeVisitConnectedPixels(x, y):
    """Recursively explores the connected neighbors of a pixel.

    Returns 1 if the given pixel needs to be processed, otherwise 0.
    """
    if not IsUnvistedBlackPixel(x, y):
      return 0
    visited[y][x] = True
    for neighbor in GetNeighbors(x, y):
      MaybeVisitConnectedPixels(*neighbor)
    return 1

  count = 0
  for y in range(len(image)):
    for x in range(len(image[y])):
      count += MaybeVisitConnectedPixels(x, y)
  return count
