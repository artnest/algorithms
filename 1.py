import queue
from collections import defaultdict


def dfs(v):
    if used[v]:
        return

    used[v] = True
    global m
    m += 1
    for w in adj[v]:
        dfs(w)


with open("input.txt", "r") as fin:
    n = int(fin.readline())
    edges = 0

    adj = defaultdict(list)
    for i, line in enumerate(fin.readlines()):
        for j, el in enumerate(line.strip().split()):
            if int(el) == 1:
                adj[i].append(j)
                edges += 1

used = [False] * n
m = 0

for vertex in range(n):
    dfs(vertex)
edges //= 2

with open("output.txt", "w") as fout:
    if edges == n - 1 and m == n:
        fout.write("Yes")
    else:
        fout.write("No")
