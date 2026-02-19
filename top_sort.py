class Vertex: 

    def __init__(self,value): 

        self.value = value 

        self.adj_list = None 

class Graph: 

    def __init__(self,vertices): 

        self.vertex_count = len(vertices) 

        self.vertices = vertices 

        self.edge_count = 0 

        for i in vertices: 

            self.edge_count += len(i.adj_list) 

class LLNode: 

    def __init__(self,val,next=None): 

        self.val = val 

        self.next = next 

class LinkedList: 

    def __init__(self,head=None): 

        self.head = LLNode('Sentinel')
        self.next = head
    def add_to_front(self,node):
        node.next = self.head.next
        self.head.next = node
    def print_list(self):
        i = self.head.next
        while(i != None):
            if i.next == None:
                print(i.val)
                break
            print(str(i.val) + " -> ",end = " ")
            i = i.next


def topological_sort(graph):
    top_list = LinkedList()

    visited = {} 

    finished_time = {} 

    global_counter = [0] 

    for i in graph.vertices: 

        if i not in visited: 

            dfs_recursive_runner(i,finished_time,visited,global_counter,top_list) 

    return top_list

def dfs_recursive_runner(vertex,finished_time,visited,global_counter,top_list): 
    
    if vertex in visited: 

        return 

    visited[vertex] = True 

    for i in vertex.adj_list: 

        dfs_recursive_runner(i,finished_time,visited,global_counter,top_list) 

    global_counter[0]+=1 
    top_list.add_to_front(LLNode(vertex.value))
    finished_time[vertex] = global_counter[0] 


 

 

# 1. Create the vertices 

v1 = Vertex(1) 

v2 = Vertex(2) 

v3 = Vertex(3) 

v4 = Vertex(4) 

 

# 2. Define edges (Directed Graph Example: 1 -> 2, 1 -> 3, 2 -> 4) 

v1.adj_list = [v2, v3] 

v2.adj_list = [v4] 

v3.adj_list = [v4] 

v4.adj_list = [] 

 

# 3. Initialize the Graph 

my_graph = Graph([v1, v2, v3, v4]) 

f = topological_sort(my_graph) 

f.print_list()

 