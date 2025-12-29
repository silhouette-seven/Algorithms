class Node:
    def __init__(self,t):
        self.t = t
        self.no_of_keys = 0
        self.key_array = [None for i in 2*t - 1]
        self.child_array = [None for i in 2*t]
        self.leaf = True
        
class BTree:
    def __init__(self,t):
        self.root = Node(self.t)
        
    def search(self,key,sub_tree_root = 'rt'):
        if sub_tree_root == 'rt':
            sub_tree_root = self.root
        i = 0
        while i < sub_tree_root.no_of_keys and sub_tree_root.key_array[i] < key:
            i+=1
        if i < sub_tree_root.no_of_keys and sub_tree_root.key_array[i] == key:
            return (sub_tree_root,i)
        if sub_tree_root.leaf:
            return None
        return self.search(key,sub_tree_root.child_array[i])
    
    def split_node(self,parent_node,index):
        node_to_be_splitted = parent_node.child_array[index]
        new_node = Node()
        median = node_to_be_splitted.key_array[node_to_be_splitted.t]
        r = 0
        for i in range(node_to_be_splitted.t+1,2*node_to_be_splitted.t):
            new_node.key_array[r] = node_to_be_splitted.key_array[i]
            r+=1
        r = 0
        if not(node_to_be_splitted.leaf):
            for j in range(node_to_be_splitted.t+1,2*node_to_be_splitted.t+1):
                new_node.child_array[r] = node_to_be_splitted.child_array[j]
                r+=1
        node_to_be_splitted.no_of_keys = node_to_be_splitted.t - 1
        for k in range(parent_node.no_of_nodes-1,index-1,-1):
            parent_node.key_array[k+1] = parent_node.key_array[k]
        for l in range(parent_node.no_of_nodes,index,-1):
            parent_node.child_array[l+1] = parent_node.child_array[l]
        parent_node.key_array[index] = median
        parent_node.child_array[i] = node_to_be_splitted
        parent_node.child_array[i+1] = new_node
        # It has 2t - 1 elements
        
        
