#include <iostream>
#include <vector>
#include <string>

using std::vector;

extern int CountShapes(const vector<vector<bool>>& image);

int main() {
  std::string line;
  vector<vector<bool>> image;
  while (std::getline(std::cin, line)) {
    vector<bool> row(line.size());
    for (std::size_t i = 0; i < line.size(); ++i) {
      if (line[i] == 'X') {
        row[i] = true;
      }
    }
    image.push_back(row);
  }
  std::cout << CountShapes(image) << std::endl;
}
