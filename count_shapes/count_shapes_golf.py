def CountShapes(image):
  """Counts the number of shapes in an image.

  Args:
    image: a list of lists of pixels. A pixel is represented as a string; if
        it's value is 'X' then the pixel is considered black, and thus part of'
        a shape.

  Returns:
    a count of the number of connected groups of black pixels in the image.
  """
  count = 0
  unvisted_black = [[pixel == 'X' for pixel in row] for row in image]
  for visit in ([(x, y)] for y, row in enumerate(unvisted_black)
                         for x, b in enumerate(row) if b):
    count += 1
    while visit:
      cx, cy = visit.pop()
      for y in range(max(0, cy-1), min(cy+2, len(image))):
        for x in range(max(0, cx-1), min(cx+2, len(image[y]))):
          if unvisted_black[y][x]:
            unvisted_black[y][x] = False
            visit.append((x, y))
  return count
