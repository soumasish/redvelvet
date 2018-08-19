class StringBuilder:
    def __init__(self, initializer=None):
        self.store = [initializer]

    def append(self, item):
        self.store.append(item)

    def to_string(self):
        return ''.join(self.store)

