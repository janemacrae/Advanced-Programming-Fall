def add(n):
    if n==1:
        return 1
    else:
        return add(n-1)+n
