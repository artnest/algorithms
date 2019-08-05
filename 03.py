import sys


def multiply_order(p):
    n = len(p)
    dp = [[0] * n for i in range(n)]
    for l in range(1, n - 1):
        for i in range(1, n - l):
            j = i + l
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j])
    return dp[1][n - 1]


with open("input.txt", "r") as fin:
    _n_ = int(fin.readline())
    dims = []
    for line in fin.readlines():
        _n, _m = map(int, line.strip().split())
        if _n not in dims:
            dims.append(_n)
        if _m not in dims:
            dims.append(_m)

with open("output.txt", "w") as fout:
    operations = multiply_order(dims)
    fout.write(str(operations))
