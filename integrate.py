import pandas as pd


def read_file(num, part):
    if num == 100:
        r_name = "A.csv"
    elif num == 200:
        r_name = "B.csv"
    elif num == 300:
        r_name = "C.csv"
    else:
        r_name = str(num) + "_" + str(part) + "_ma.csv"
    df = pd.read_csv(r_name,names=('ax','ay','az','label'))
    return df


if __name__ == "__main__":
    teacher = pd.DataFrame(index=[], columns=('ax','ay','az','label'))
    test = pd.DataFrame(index=[], columns=('ax','ay','az','label'))

    for i in range(1, 6):
        for j in range(1, 12):
            if j == 7 or j == 9:
                continue
            if i <= 2:
                test = pd.concat([test, read_file(i, j)])
                test.sample(frac=1).to_csv("A.csv", header=False, index=False)
            elif i == 3 or i == 4:
                test = pd.concat([test, read_file(i, j)])
                test.sample(frac=1).to_csv("B.csv", header=False, index=False)
            elif i == 5:
                test = pd.concat([test, read_file(i, j)])
                test.sample(frac=1).to_csv("C.csv", header=False, index=False)

    for i in range(1, 4):
        if i == 1:
            teacher = pd.concat([teacher, read_file(200, 200)])
            teacher = pd.concat([teacher, read_file(300, 300)])
            teacher.sample(frac=1).to_csv("BC.csv", header=False, index=False)
        elif i == 2:
            teacher = pd.concat([teacher, read_file(100, 100)])
            teacher = pd.concat([teacher, read_file(300, 300)])
            teacher.sample(frac=1).to_csv("AC.csv", header=False, index=False)
        else:
            teacher = pd.concat([teacher, read_file(100, 100)])
            teacher = pd.concat([teacher, read_file(200, 320)])
            teacher.sample(frac=1).to_csv("AB.csv", header=False, index=False)