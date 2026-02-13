class TreeNode:

    def __init__(self,val,parent=None):
        self.val = val
        self.parent = self



class DisjointSetNode:

    def __init__(self,initial_value):
        self.root = TreeNode(initial_value)

def path_compression_heuristic(current_node):
    if current_node.parent != current_node:
        current_node.parent = path_compression_heuristic(current_node.parent)
    return current_node.parent
def get_set(setA):
    return path_compression_heuristic(setA.root)



def union(setA,setB):
    a = get_set(setA)
    b = get_set(setB)
    if b != a:
        b.parent = a

def MSTKruskal(graph):
    nodes = {}
    edge_list = []
    a = []
    for i in graph.vertices:
        nodes[i.val] = DisjointSetNode(i)
        for j in i.adjacency_list:
            edge_list.append((j[1],i.val,j[0].val))
    edge_list.sort()
    for i in edge_list:
        source = i[1]
        destination = i[2]
        if get_set(nodes[source]) != get_set(nodes[destination]):
            a.append(i)
            union(nodes[source],nodes[destination])
    return a
            

        



class Vertex:
    def __init__(self,val,adj = []):
        self.val = val
        self.adjacency_list = adj
class Graph:
    def __init__(self,vertices = []):
        self.vertices = vertices


v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)


v0.adjacency_list = [(v1, 10), (v2, 6), (v3, 5)]
v1.adjacency_list = [(v0, 10), (v3, 15)]
v2.adjacency_list = [(v0, 6), (v3, 4)]
v3.adjacency_list = [(v1, 15), (v0, 5), (v2, 4)]


my_graph = Graph([v0, v1, v2, v3])
print(MSTKruskal(my_graph))





