def sum(xs, a=0):
    if xs:
        return sum(xs[1:], a + xs[0])
    else:
        return a

    # return sum(xs[1:], a + xs[0]) if xs else a

xs = [1, 2, 3, 4, 5, 6, 7]
print(sum(xs))
