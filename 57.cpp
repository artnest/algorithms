#include <iostream>
#include <fstream>
#include <cstring>

long long get_hash(long long *h, int l, int r) {
    long long result = h[r];
    if (l > 0) {
        result -= h[l - 1];
    }
    return result;
}

int min_cycle_shift(char *s, char *t, int init_len) {
    const int p = 31; // lowercase latin characters
    long long *pow = new long long[2 * init_len];

    pow[0] = 1;
    for (int i = 1; i < 2 * init_len; ++i) {
        pow[i] = pow[i - 1] * p;
    }

    long long *hs = new long long[2 * init_len];
    hs[0] = s[0];
    for (int i = 1; i < 2 * init_len; i++) {
        hs[i] = hs[i - 1] + pow[i] * s[i];
    }

    long long ht;
    ht = t[0];
    for (int i = 1; i < init_len; ++i) {
        ht += pow[i] * t[i];
    }

    int k = -1;
    for (int i = 0; i + init_len <= 2 * init_len; i++) {
        if (get_hash(hs, i, i + init_len - 1) == ht * pow[i]) {
            k = i;
            break;
        }
    }

    delete[] pow;
    delete[] hs;
    return k;
}

int main() {
    std::ifstream fin("input.txt");
    int len;
    fin >> len;

    char *s1 = new char[2 * len];
    char *str1 = new char[len];
    char *s2 = new char[len];

    fin >> str1;
    strcpy(s1, str1);
    strcat(s1, str1);
    fin >> s2;
    fin.close();

    int k = min_cycle_shift(s1, s2, len);
    delete[] str1;
    delete[] s1;
    delete[] s2;

    std::ofstream fout("output.txt");
    fout << k << std::endl;
    fout.close();

    return 0;
}
