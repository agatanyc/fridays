def last_index(x, xs, a=-1, i=0):
    if xs:
        return last_index(x, xs[1:], i if xs[0] == x else a, i + 1)
    else:
        return a

xs = [3, 4, 5, 6, 7, 8]
print(last_index(5, xs))
