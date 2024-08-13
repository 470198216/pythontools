# 使用邻接表表示图

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append((vertex2, weight))

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for v in self.adjacency_list:
                self.adjacency_list[v] = [v2 for v2 in self.adjacency_list[v] if v2[0] != vertex]
            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1] = [v2 for v2 in self.adjacency_list[vertex1] if v2[0] != vertex2]

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")

# 创建图实例
graph = Graph()

# 添加顶点
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

# 添加边
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'C', 2)

# 打印图
graph.print_graph()

# 删除顶点
graph.remove_vertex('B')

# 打印图
print("\nAfter removing vertex 'B':")
graph.print_graph()

# 删除边
graph.add_vertex('B')  # Re-adding vertex for edge removal demonstration
graph.remove_edge('A', 'B')

# 打印图
print("\nAfter removing edge (A, B):")
graph.print_graph()