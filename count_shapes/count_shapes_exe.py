import subprocess

class CountShapesExe:
  def __init__(self, path):
    self.path = path
    self.__name__ = path

  def CountShapes(self, image):
    p = subprocess.Popen([self.path],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    stdin = p.stdin
    stdout = p.stdout

    stdin.writelines(''.join(row) + '\n' for row in image)
    stdin.close()
    result = stdout.readline()
    status = p.wait()

    return int(result)
