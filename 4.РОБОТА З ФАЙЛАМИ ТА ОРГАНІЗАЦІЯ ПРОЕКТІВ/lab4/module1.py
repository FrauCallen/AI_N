def array_num(x):
    Y = []
    for i in range(len(x)):
        num = 0
        for j in range(len(x)):
            if x[i] == x[j]:
                num += 1
        if num == 1:
            Y = Y + [x[i]]
    max_element = max(Y)
    min_element = min(Y)
    return max_element, min_element