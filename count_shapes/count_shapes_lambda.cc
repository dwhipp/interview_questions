#include <vector>
#include <utility>

using std::vector;

int CountShapes(const vector<vector<bool>>& image_in) {
  typedef std::pair<int,int> Coord;

  vector<vector<bool>> image = image_in; // copy.

  auto erase_point = [&] (Coord coord) {
    int x = coord.first;
    int y = coord.second;
    if (y < 0 ||
        x < 0 ||
        y >= static_cast<int>(image.size()) ||
        x >= static_cast<int>(image[y].size()) ||
        !image[y][x]) {
      return false;
    }
    image[y][x] = false;
    return true;
  };

  auto erase_neighbors = [&] (Coord coord) {
    vector<Coord> neighbors;
    for (int dx : {-1, 0, 1}) {
      for (int dy : {-1, 0, 1}) {
        Coord neighbor(coord.first + dx, coord.second + dy);
        if (erase_point(neighbor)) {
          neighbors.push_back(neighbor);
        }
      }
    }
    return neighbors;
  };

  auto erase_shape = [&] (Coord coord) {
    if (!erase_point(coord)) {
      return false;
    }
    vector<Coord> stack = {coord};
    while (!stack.empty()) {
      vector<Coord> neighbors = erase_neighbors(stack.back());
      stack.pop_back();
      stack.insert(stack.end(), neighbors.begin(), neighbors.end());
    }
    return true;
  };

  int count = 0;
  for (std::size_t y = 0; y < image.size(); y++) {
    for (std::size_t x = 0; x < image[y].size(); x++) {
      count += erase_shape({x, y});
    }
  }

  return count;
}
