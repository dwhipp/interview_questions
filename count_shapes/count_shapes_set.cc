#include <vector>
#include <set>
#include <utility>

using std::vector;
using std::set;

int CountShapes(const vector<vector<bool>>& image) {
  typedef std::pair<int,int> Coord;

  set<Coord> black_pixels;
  for (std::size_t y = 0; y < image.size(); y++) {
    for (std::size_t x = 0; x < image[y].size(); x++) {
      if (image[y][x]) {
        black_pixels.insert({x,y});
      }
    }
  }

  int count = 0;
  vector<Coord> stack;
  while (true) {
    Coord coord;
    if (stack.empty()) {
      if (black_pixels.empty()) {
        return count;
      }
      count++;
      auto iter = black_pixels.begin();
      coord = *iter;
      black_pixels.erase(iter);
    } else {
      coord = stack.back();
      stack.pop_back();
    }

    for (int dx : {-1, 0, 1}) {
      for (int dy : {-1, 0, 1}) {
        if (dx == 0 && dy == 0) continue;
        auto neighbor = black_pixels.find({coord.first+dx, coord.second+dy});
        if (neighbor != black_pixels.end()) {
          stack.push_back(*neighbor);
          black_pixels.erase(neighbor);
        }
      }
    }
  }
}
