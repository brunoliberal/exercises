class Graph:
    def __init__(self, vert_qty):
        self.vert_qty = vert_qty
        self.adj_list = [[] for i in range(vert_qty)]

    def connect(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def print_distances(self, distances):
        for i in distances:
            if i != 0:
                print(i, end=' ')
        print()

    def find_all_distances(self, start_v):
        queue = [start_v]
        distances = [-1 for _ in range(self.vert_qty)]
        distances[start_v] = 0
        visited = [False for _ in range(self.vert_qty)]
        visited[start_v] = True
        while queue:
            cur_node = queue.pop(0)
            for i in self.adj_list[cur_node]:
                if not visited[i]:
                    distances[i] = distances[cur_node] + 6
                    if len(self.adj_list[i]) > 1:
                        queue.append(i)
                    visited[i] = True
        self.print_distances(distances)

# t = int(input())
# for i in range(t):
#     n,m = [int(value) for value in input().split()]
#     graph = Graph(n)
#     for i in range(m):
#         x,y = [int(x) for x in input().split()]
#         graph.connect(x-1,y-1)
#     s = int(input())
#     graph.find_all_distances(s-1)

