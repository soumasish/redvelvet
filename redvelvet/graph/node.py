class Node:
    def __init__(self, id, value):
        self._id = id
        self._value = value
        self._neighbors = set()

    def add_edge(self, node):
        self._neighbors.add(node)

    def get_neighbors(self):
        return list(self._neighbors)

    def get_item(self):
        return self._value

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

    def __repr__(self):
        s = '{'
        s += str(self._value)
        s += ', ['
        for neighbor in self._neighbors:
            s += str(neighbor.get_item())
            s += ', '
        s += ']}'
        return s