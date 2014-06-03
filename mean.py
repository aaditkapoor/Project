def compute(word):
    numbers = range(len(word))
    flag = 0
    total = sum(numbers)
    if total % 2 == 0:
        flag = 1
    mean = total / len(word)
    if flag == 1:
        return range(mean+1)
    else:
        return range(mean)
