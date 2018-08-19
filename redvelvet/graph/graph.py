from collections import deque
from .node import Node
from .errors import GraphError


class Graph:
    def __init__(self, directed=False):
        self._vertices = 0
        self._directed = directed
        self._vertex_map = {}

    def add_edge(self, v1, v2, weight=1):
        if v1 in self._vertex_map:
            V1 = self._vertex_map[v1]
        else:
            self._vertices += 1
            V1 = Node(self._vertices, v1)
            self._vertex_map[v1] = V1
        if v2 in self._vertex_map:
            V2 = self._vertex_map[v2]
        else:
            self._vertices += 1
            V2 = Node(self._vertices, v2)
            self._vertex_map[v2] = V2
        if V1 != V2:
            V1.add_edge(V2)
            if not self._directed:
                V2.add_edge(V1)
        else:
            raise GraphError("Cannot add node to itself!")

    def get_all(self):
        return self._vertex_map.items()

    def get_neighbors(self, v):
        return self._vertex_map[v].get_neighbors()

    def get_edge_weight(self, v1, v2):
        pass

    def __len__(self):
        return self._vertices

    def get_indegree(self, v):
        indegree = 0
        if v in self._vertex_map:
            v_node = self._vertex_map[v]
        else:
            raise GraphError("Vertex does not exist!")
        for v in self._vertex_map.values():
            if v_node in v._neighbors:
                indegree += 1
        return indegree

    def breadth_first(self, start=None, apply=None):
        result = []
        queue = deque()
        queue.appendleft(start)
        visited = set()
        while len(queue) > 0:
            vertex = queue.pop()
            modified = apply(vertex)
            result.append(modified)
            if vertex not in visited:
                neighbors = vertex.get_neighbors()
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.appendleft(neighbor)
        return modified

    def depth_first(self, visited, current=None, apply= None):
        if current in visited:
            return
        visited.add(current)
        for vertex in current.get_neighbors():
            self.depth_first(visited, vertex)

    def topological_sort(self):
        queue = deque()
        indegree_map = {k: self.get_indegree(k) for k, v in self.get_all()}
        for k, v in indegree_map.items():
            if v == 0:
                queue.appendleft(k)
        sorted_list = []
        while len(queue) > 0:
            curr = queue.pop()
            sorted_list.append(curr)
            for v in self.get_neighbors(curr):
                val = v.get_item()
                indegree_map[val] -= 1
                if indegree_map[val] == 0:
                    queue.appendleft(val)
        return str(sorted_list)

    def _build_distance_table(self, source):
        distance_table = {item: (None, None) for item in self.vertex_list}
        distance_table[source] = (0, source)
        queue = deque()
        queue.appendleft(source)
        while len(queue) > 0:
            current_vertex = queue.pop()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.get_neighbors(current_vertex):
                if not distance_table[neighbor][0]:
                    distance_table[neighbor] = (1 + current_distance, current_vertex)
                    if len(self.get_neighbors(neighbor)) > 0:
                        queue.appendleft(neighbor)
        return distance_table

    def shortest_path(self, source, destination):
        distance_table = self._build_distance_table(source)
        path = [destination]
        previous_vertex = distance_table[destination][1]

        while previous_vertex and previous_vertex is not source:
            path = [previous_vertex] + path
            previous_vertex = distance_table[previous_vertex][1]

        if not previous_vertex:
            return []
        else:
            path = [source] + path
            return path

    def __str__(self):
        s = ''
        for v in self._vertex_map.values():
            s += str(v)
            s += ', '
        return s

    def __len__(self):
        return self._vertices
