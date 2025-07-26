#include <iostream>
#include <fstream>
#include <deque>
#include <string>

void printLastKLines(const std::string& filename, int k) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "File not found" << std::endl;
        return;
    }
    std::deque<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
        if (lines.size() > static_cast<size_t>(k)) {
            lines.pop_front();
        }
    }
    for (const auto& l : lines) {
        std::cout << l << std::endl;
    }
}