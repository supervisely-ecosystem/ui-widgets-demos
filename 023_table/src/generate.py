import pandas as pd


def multiplication_table():
    a = list(range(1, 11))
    b = list(range(1, 11))

    data = []
    for row in b:
        temp = []
        for number in a:
            temp.append(round(row * number, 1))
        data.append(temp)

    a = [str(i) for i in a]
    b = [str(i) for i in b]
    df = pd.DataFrame(data=data, index=b, columns=a)
    return df
