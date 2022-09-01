class Graph:
    def __init__(self):
        self.adj_list = {}

    #prints the vertex
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    #adds the vertex using dictionary
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()
