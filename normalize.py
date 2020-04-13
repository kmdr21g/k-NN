import math


def normalize(data, axis=None):
    y = []
    norm = math.sqrt(data[0]**2 + data[1]**2 + data[2]**2)
    for i in data:
        y.append(i / norm)
    return y


def window(f_name):
    seiki = []

    with open(f_name, mode="r") as f:
        lines = [list(map(lambda x: float(x) if x is not "" else 1.2, l.split(",")[4:7]))
                 for l in f.readlines()[1:-1]]

        for wl in lines:
            seiki.append(list(normalize(wl)))

    return seiki


def write_file(num, part):
    r_name = str(num) + "_" + str(part) + ".csv"
    w_name = r_name[:-4] + "_nor.csv"

    seiki = window(r_name)

    with open(w_name, mode="w") as f:
        for row in seiki:
            for elem in row[:-1]:
                print(elem, end=',', file=f)
            print(row[-1], file=f)


if __name__ == "__main__":
    for i in range(1, 6):
        for j in range(1, 12):
            if j == 7 or j == 9:
                continue
            else:
                write_file(i, j)
