with open("input.txt", "r") as fin:
    n = int(fin.readline())
    n_bin = bin(n)[2:]

    orders = [i for i, j in enumerate(n_bin[::-1]) if j == "1"]
    orders = "\n".join([str(i) for i in orders])

with open("output.txt", "w") as fout:
    fout.write(orders)
