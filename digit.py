def digit(n):
    if n<10:
        return 1
    else:
        return digit(n/10)+1
