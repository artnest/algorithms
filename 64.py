with open("input.txt", "r") as fin:
    n = int(fin.readline().strip().split()[0])
    matrix = [[0] * n for i in range(n)]

    for entry in fin.readlines():
        i, j = entry.strip().split()
        matrix[int(i) - 1][int(j) - 1] = 1
        matrix[int(j) - 1][int(i) - 1] = 1

with open("output.txt", "w") as fout:
    for row in matrix:
        matrix[matrix.index(row)] = " ".join([str(i) for i in row])
    matrix = "\n".join(matrix)
    fout.write(matrix)
