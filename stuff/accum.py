class Accumulator:

    def __init__(self):
        self._count = 0         # Variable _count

    @property                   # property decorator can be treat method as getter or setter
    def count(self):
        return self._count      # User will get _count value

    def add(self, more=1):
        self._count += more
