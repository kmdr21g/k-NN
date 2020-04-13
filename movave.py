import numpy as np


def window(f_name, window=5, step=1):
    avg = []
    var = []

    with open(f_name, mode="r") as f: 
        lines = [list(map(lambda x: float(x), l.split(",")))
                 for l in f.readlines()[1:]]

        for wl in [lines[i:i + window]
                   for i in range(0, len(lines) - 1, step)]:
            avg.append(list(np.average(np.array(wl), axis=0)))
            var.append(list(np.var(np.array(wl), axis=0)))

    return avg, var


def write_file(num, part):
    r_name = str(num) + "_" + str(part) + "_nor.csv"
    w_name = r_name[:-8] + "_ma.csv"

    avg, var = window(r_name)

    with open(w_name, mode="w") as f:
        for row in avg:
            for elem in row[:-1]:
                print(elem, end=',', file=f)
            print(row[-1], ",", part, sep="", file=f)


if __name__ == "__main__":
    for i in range(1, 6):
        for j in range(1, 12):
            if j == 7 or j == 9:
                continue
            else:
                write_file(i, j)