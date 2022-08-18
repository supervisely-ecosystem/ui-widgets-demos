def multiplication_chart():
    data = []
    for row in list(range(1, 11)):
        temp = []
        for number in list(range(1, 11)):
            temp.append(round(row * number, 1))
        data.append(temp)
    return data
