import queue
from collections import defaultdict


def bfs(v):
    if used[v]:
        return

    q.put(v)
    used[v] = True
    global m
    marks[v] = m
    m += 1
    while not q.empty():
        v = q.get()
        for w in adj[v]:
            if not used[w]:
                q.put(w)
                used[w] = True
                marks[w] = m
                m += 1


with open("input.txt", "r") as fin:
    n = int(fin.readline())

    adj = defaultdict(list)
    for i, line in enumerate(fin.readlines()):
        for j, el in enumerate(line.strip().split()):
            if int(el) == 1:
                adj[i].append(j)

q = queue.Queue()
used = [False] * n
marks = [0] * n
m = 1

for vertex in range(n):
    bfs(vertex)

with open("output.txt", "w") as fout:
    marks_str = " ".join([str(mark) for mark in marks])
    fout.write(marks_str)
