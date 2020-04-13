from math import sqrt
from functools import reduce
import numpy as np

cm = np.zeros((11, 11),  dtype=np.int16)

def window(f_name):
    avg = []
    var = []
    label = []

    with open(f_name, mode="r") as f:
        lines = [list(map(lambda x: float(x), l.split(",")))
                 for l in f.readlines()[1:5001]]

        for i in lines:
            avg.append(i[:3])
            var.append(i[:3])
            label.append([int(i[-1])])

    return avg, var, label


def calc_eucl(feature):
    # √{(0 + tea-tes[0] + tea-tes[1] + …)^2}
    return sqrt(reduce(lambda a, b: a + b ** 2, feature, 0))


def calc_manh(feature):
    return reduce(lambda a, b: a + b, feature)


def knn(teacher, test, calc_func, k=3):
    # calc_func = calc_eucl()
    result = {}

    tmp = [[calc_func(
        [tea - tes for tea, tes in zip(teac[:-1], test)]), teac[-1]] for teac in teacher]

    for d in sorted(tmp, key=lambda x: x[0])[:k]:
        # tmp[0](距離)を昇順ソートしたものを値が小さい方から3つ
        result[d[1]] = 1 if d[1] not in result else result[d[1]] + 1
        """
        もしd[1](ラベル)がresultに含まれていなければ result[d[1]] = 1
        それ以外は result[d[1]]+1
        """

    return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]
    # x[1](ラベル)を基準にresultを降順ソート


def check_ans(ans, pre):
    global cm
    for i in range(1, 12):
        if ans == pre and ans == i:
            cm[i-1, i-1] = cm[i-1, i-1]+1
        elif ans != pre and pre == i:
            cm[ans-1, i-1] = cm[ans-1, i-1]+1
    return 1 if(ans == pre) else 0
    # testのラベル == knnで予測したラベルのとき1、それ以外は0


if __name__ == "__main__":  
    teacher = [a + v + label for (a, v, label) in zip(window("BC.csv")[0], window("BC.csv")[1], window("BC.csv")[-1])]
    test = [a + v + label for (a, v, label) in zip(window("A.csv")[0], window("A.csv")[1], window("A.csv")[-1])]

    cor = reduce(
        lambda a, b: a + b, [check_ans(i[-1], knn(teacher, i[:-1], calc_eucl)) for i in test])

    cm = np.delete(cm, 6, axis=0)
    cm = np.delete(cm, 6, axis=1)
    cm = np.delete(cm, 7, axis=0)
    cm = np.delete(cm, 7, axis=1)

    hd = "Ans\\Pre\t|1\t2\t3\t4\t5\t6\t8\t10\t11"
    line = "---" * (len(hd)-3)
    print(hd, "\n", line)
    i = 1
    for row in cm:
        if i == 7 or i == 9:
            i += 1
        print(i, "\t|", end="")
        i += 1
        for elem in row[:-1]:
            print(elem, end='\t')
        print(row[-1])

        with open("cm_1.csv", mode="w") as f:
            for a in cm:
                print(*a, sep=",", file=f)
            print(str(cor / len(test) * 100), file=f)

    print("\nAccuracy : " + str(cor / len(test) * 100) + " %")