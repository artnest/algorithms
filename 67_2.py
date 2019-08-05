import queue
from collections import defaultdict


def dfs(v):
    if used[v]:
        return

    used[v] = True
    global m
    marks[v] = m
    m += 1
    for w in adj[v]:
        dfs(w)


with open("input.txt", "r") as fin:
    n = int(fin.readline())

    adj = defaultdict(list)
    for i, line in enumerate(fin.readlines()):
        for j, el in enumerate(line.strip().split()):
            if int(el) == 1:
                adj[i].append(j)

used = [False] * n
marks = [0] * n
m = 1

for vertex in range(n):
    dfs(vertex)

with open("output.txt", "w") as fout:
    marks_str = " ".join([str(mark) for mark in marks])
    fout.write(marks_str)
