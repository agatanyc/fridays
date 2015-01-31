"""Implements a dictionary interface described on [Hackpad](
    https://hackpad.com/Hash-Tables-Friday-Sept-19-1030am-NNBqlsk9PYa ).
"""
import bisect

class Dictionary1:

    def __init__(self):
        self._d = dict()

    def add_key_value_pair(self, key, value):
        """(str, int) -> NoneType"""
        self._d[key] = value

    def get_value(self, key):
        """(str) -> int"""
        return self._d[key]

    def remove_key(self, key):
        """(str) -> int"""
        if key not in self._d:
            return None
        v = self._d[key]
        del self._d[key]
        return v


class Dictionary2:

    def __init__(self):
        self._xs = []   # List of pairs

    def add_key_value_pair(self, key, value):
        """(str, int) -> NoneType"""
        self.remove_key(key)
        self._xs.append((key, value))

    def get_value(self, key):
        """(str) -> int"""
        vs = [x[1] for x in self._xs if x[0] == key]
        return vs[0] if vs else None

    def remove_key(self, key):
        """(str) -> int"""
        v = self.get_value(key)
        self._xs = [x for x in self._xs if x[0] != key]
        return v

class Dictionary3:

    class Pair:
        """Weakly ordered by key"""

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __ge__(self, other): return self.key >= other.key
        def __gt__(self, other): return self.key > other.key
        def __le__(self, other): return self.key <= other.key
        def __lt__(self, other): return self.key < other.key

    def __init__(self):
        self._xs = [] # Sorted list of Pair objects

    def add_key_value_pair(self, key, value):
        """(str, int) -> NoneType"""
        x = Dictionary3.Pair(key, value)
        i = bisect.bisect_left(self._xs, x)
        if i == len(self._xs):
            self._xs.append(x)
        elif self._xs[i].key == x.key:
            self._xs[i] = x
        else:
            self._xs.insert(i, x)

    def get_value(self, key):
        """(str) -> int"""
        i = bisect.bisect_left(self._xs, Dictionary3.Pair(key, None))
        return None if i == len(self._xs) else self._xs[i].value

    def remove_key(self, key):
        """(str) -> int"""
        i = bisect.bisect_left(self._xs, Dictionary3.Pair(key, None))
        if i != len(self._xs) and self._xs[i].key == key:
            return self._xs.pop(i).value

def test_dict(D):
    d = D()
    d.add_key_value_pair('one', 1)
    d.add_key_value_pair('two', 2)
    d.add_key_value_pair('three', 3)
    assert(d.get_value('two') == 2)
    assert(d.remove_key('one') == 1)
    assert(d.get_value('two') == 2)
    assert(d.remove_key('one') == None)

if __name__ == '__main__':
    test_dict(Dictionary1)
    test_dict(Dictionary2)
    test_dict(Dictionary3)
