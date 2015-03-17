

class Fucker:
    """Mutable and hashable."""

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

fucker = Fucker("hello")
s = {fucker}
print(fucker in s)      # True

fucker.value = "world"
print(fucker in s)      # False -- it's there, but the set can't find it.
