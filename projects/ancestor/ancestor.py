class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            # TODO: Do we need error checking here?

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')


def earliest_ancestor(ancestors, starting_node):
    # Build our graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges in reverse
        graph.add_edge(pair[1], pair[0])

    qq = Queue()
    qq.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while qq.size() > 0:
        path = qq.dequeue()
        v = path[-1]

        if(len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            qq.enqueue(path_copy)

    return earliest_ancestor


# Expected ancestors format:
# [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11, 8), (10,1)]
# Starting_node = 6

# Expected answer - 10

"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""
