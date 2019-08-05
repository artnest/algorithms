#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <limits>

int multiply_order(std::vector<int> p) {
    int n = p.size();
    int** dp = new int*[n];
    for (int i = 0; i < n; i++) {
        dp[i] = new int[n];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = 0;
        }
    }

    for (int l = 1; l < n - 1; l++) {
        for (int i = 1; i < n - l; i++) {
            int j = i + l;
            dp[i][j] = std::numeric_limits<int>::max();

            for (int k = i; k < j; k++) {
                dp[i][j] = std::min(dp[i][j],
                                    dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]);
            }
        }
    }

    int k = dp[1][n - 1];

    for (int i = 0; i < n; i++) {
        delete dp[i];
    }
    delete[] dp;

    return k;
}

int main(int argc, char const *argv[]) {
    std::ifstream fin("input.txt");
    int d;
    fin >> d;

    std::vector<int> dims;
    fin >> d;
    dims.push_back(d);
    while (!fin.eof()) {
        fin >> d;
        dims.push_back(d);
        fin >> d;
    }
    fin.close();

    int k = multiply_order(dims);
    std::ofstream fout("output.txt");
    fout << k << std::endl;
    fout.close();

    return 0;
}
