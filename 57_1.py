with open("input.txt", "r") as fin:
    m, c, n = fin.readline().strip().split()
    m = int(m)
    c = int(c)

    hashtable = {i: -1 for i in range(m)}
    for line in fin.readlines():
        x = int(line.strip())
        if x not in hashtable.values():
            i = 0
            idx = (x % m + c * i) % m
            while hashtable[idx] != -1:
                i += 1
                idx = (x % m + c * i) % m
            hashtable[idx] = x

with open("output.txt", "w") as fout:
    hashtable_str = " ".join([str(i) for i in hashtable.values()])
    fout.write(hashtable_str)
