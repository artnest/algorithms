def wagner_fischer(s1, s2, deletion=1, insertion=1, substitution=1):
    len_s1 = len(s1)
    len_s2 = len(s2)

    d = [[0] * (len_s2 + 1) for i in range(len_s1 + 1)]

    for i in range(1, len_s1 + 1):
        d[i][0] = i * deletion
    for j in range(1, len_s2 + 1):
        d[0][j] = j * insertion

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j] + deletion,
                              d[i][j - 1] + insertion,
                              d[i - 1][j - 1] + substitution)
    return d[len_s1][len_s2]


with open("in.txt", "r") as fin:
    del_cost = int(fin.readline())
    ins_cost = int(fin.readline())
    sub_cost = int(fin.readline())

    str1 = fin.readline().strip()
    str2 = fin.readline().strip()

p = wagner_fischer(str1, str2, del_cost, ins_cost, sub_cost)

with open("out.txt", "w") as fout:
    fout.write(str(p))
