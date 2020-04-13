import numpy as np


def window(f_name):
    with open(f_name, mode="r") as f:
        data = [list(map(lambda x: float(x), l.split(",")))for l in f.readlines()]
        acc = data[-1][0]
        data = data[:-1]
        data = np.array(data, dtype='int32')
    return data, acc


if __name__ == "__main__":

    data1, acc1 = window("cm_1.csv")
    data2, acc2 = window("cm_2.csv")
    data3, acc3 = window("cm_3.csv")

    ave_data = (data1 + data2 + data3)/3
    ave_data = ave_data.astype('int32')

    ave_acc = (acc1 + acc2 + acc3) / 3.0

    hd = "Pre\\Ans\t|1\t2\t3\t4\t5\t6\t8\t10\t11"
    line = "---" * (len(hd)-3)
    print(hd, "\n", line)
    i = 1
    for row in ave_data:
        if i == 7 or i == 9:
            i += 1
        print(i, "\t|", end="")
        i += 1
        for elem in row[:-1]:
            print(elem, end='\t')
        print(row[-1])
    print("\nAverage Accuracy: ", ave_acc, "%")
