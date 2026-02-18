from math import inf
#An Vertex class with simple definition
class Vertex:
    def __init__(self,val,adj_list = []):
        self.val = val
        self.adj_list = adj_list

#A Graph is composed of vertices
class Graph:
    def __init__(self,vertices_list = []):
        self.vertices_list = vertices_list
        self.vertex_count = len(vertices_list)
        self.edge_count = 0
        for i in vertices_list:
            self.edge_count += len(i.adj_list)


#A vertex that stores additional properties 
class ExtendedVertex(Vertex):
    def __init__(self,val,adj_list=[]):
        super().__init__(val,adj_list)
        #UpperBound for the distance from source
        self.d = inf
        self.parent = None

def relax(node):
    src = node[0]
    destination = node[1]
    cost = node[2]
    if src.d + cost < destination.d:
        destination.d = src.d + cost
        destination.parent = src


def sssp_bellman_ford(graph,source,destination):
    #Initializing Graph Vertices with upperbound and parent
    extended_vertices_dict = {}
    for i in graph.vertices_list:
        extended_vertices_dict[i.val] = ExtendedVertex(i.val,i.adj_list)
    extended_vertices_dict[source.val].d = 0
    def print_path(destination):
        if destination.parent == None:
            print(destination.val,end = '')
        else:
            print_path(destination.parent)
            print(' -> ',destination.val,end = '')


    for _ in range(graph.vertex_count):
        for i in extended_vertices_dict.values():
            for j in i.adj_list:
                relax((i,extended_vertices_dict[j[0].val],j[1]))
    print(f'shortest_distance to {destination.val} = {extended_vertices_dict[destination.val].d}')
    print_path(extended_vertices_dict[destination.val])
        


#Initialization of Graph Thanks to Gemini
# Initialize Vertices
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")

# Define weighted edges: (destination_vertex, weight)
a.adj_list = [(b, 4), (c, 5)]
b.adj_list = [(d, 3)]
c.adj_list = [(b, -10)] # Negative edge
d.adj_list = []

# Create Graph
my_graph = Graph([a, b, c, d])
#End of initialization

sssp_bellman_ford(my_graph,a,b)