def last(n):
    return a[-1]
a =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(a, key=last))