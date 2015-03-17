from itertools import islice

def permute(xs):
    if xs:
        if len(xs) == 1:
            yield set(xs).pop()
        else:
            for x in xs:
                for s in permute(xs.difference({x})):
                    yield x + s

if __name__ == '__main__':
    for s in permute(set('abc')):
        print(s)
