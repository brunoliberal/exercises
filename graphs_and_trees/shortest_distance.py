import sys


class Graph:
    def __init__(self, vert_qty):
        self.vertices = vert_qty
        self.edges = [[0 for i in range(vert_qty)] for i in range(vert_qty)]

    def connect(self, v1, v2):
        self.edges[v1][v2] = 6
        self.edges[v2][v1] = 6

    def find_all_distances(self, start_v):
        visited = []
        distances = [sys.maxsize for i in range(self.vertices)]
        distances[start_v] = 0
        for i in range(self.vertices):  # must look through all vertices
            # first loop cur = start_v
            cur = self.select_min_weight(visited, distances)
            # mark as visited
            visited.append(cur)
            # update weight on all adj vertices not yet visited
            for i in range(self.vertices):
                acum_weight = distances[cur] + self.edges[cur][i]
                if i not in visited and self.edges[cur][i] != 0 and acum_weight < distances[i]:
                    distances[i] = acum_weight
        self.print_distances(distances)

    def select_min_weight(self, visited, distances):
        min_weight = sys.maxsize
        cur = None
        for i in range(self.vertices):
            if i not in visited and distances[i] <= min_weight:
                min_weight = distances[i]
                cur = i
        return cur

    @staticmethod
    def print_distances(distances):
        dist = []
        for i in distances:
            if i == sys.maxsize:
                dist.append('-1')
            elif i != 0:
                dist.append(str(i))
        print(' '.join(dist))


# loops = int(input())
# for i in range(loops):  # for each query create graph
#     v_qty, e_qty = [int(value) for value in input().split()]
#     graph = Graph(v_qty)
#     for j in range(e_qty):
#         x, y = [int(x) for x in input().split()]
#         graph.connect(x-1, y-1)
#     s = int(input())
#     graph.find_all_distances(s-1)

