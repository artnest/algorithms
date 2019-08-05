#include <iostream>
#include <fstream>
#include <map>

int main(int argc, char const *argv[]) {
    std::ifstream in("input.txt");
    int m;
    in >> m;
    int c;
    in >> c;
    int n;
    in >> n;

    std::map<int, int> map;
    int i = 0;
    while (i < m) {
        map.insert(std::make_pair(i, -1));
        i++;
    }

    int x = 0;
    while (in >> x) {
        auto it = map.begin();
        for (; it != map.end(); it++) {
            if (it->second == x) {
                break;
            }
        }

        if (it == map.end()) {
            int i = 0;
            int idx = (x % m + c * i) % m;
            while (map[idx] != -1) {
                i++;
                idx = (x % m + c * i) % m;
            }
            map[idx] = x;
        }
    }
    in.close();

    std::ofstream out("output.txt");
    for (auto it = map.cbegin(); it != map.cend(); it++) {
        out << it->second << " ";
    }

    return 0;
}
