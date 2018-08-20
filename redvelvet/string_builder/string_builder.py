class StringBuilder:
    def __init__(self, initializer=None):
        self.store = [initializer]
        self.length = 0

    def append(self, item):
        self.length + len(item)
        self.store.append(item)

    def prepend(self, item):
        self.length + len(item)
        self.store.insert(0, item)

    def to_string(self):
        return ''.join(self.store)

    def __len__(self):
        return self.length

