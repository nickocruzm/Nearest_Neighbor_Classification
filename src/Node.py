class Node:
    instances = 1
    def __init__(self,data_row):
        self.id = Node.instances
        Node.instances += 1
        
        self.classification = data_row[0]    # Given Classifications
        self.features = data_row[1:]         # Given Features
         
        self.neighbors = []                 # neighbors of node formatted as [ {'node': Node object, 'distance': float} ]
                                            # 'node', holds pointer to node object
                                            # 'distance', is the euclidean distance computed
    
        self.neighbors_sorted = False
        
    def __eq__(self, Other):
        return (self.id == other.id)
    
    def update_distance(self,neighbor,i):
        pass
        
    # updates neighbor
    def update_neighbors(self,neighbor):
        self.neighbors_sorted = False
        self.neighbors.append(neighbor)
        
    
    def sort_neighbors(self):
        self.neighbors_sorted = True
        self.neighbors = sorted(self.neighbors,key=lambda x:x['distance'])
    
    # neighbors already sorted in ascending order, get first (k) items
    def get_nearest_neighbors(self,k):
        k_nearest = []
        for i in range(0,k):
            k_nearest.append(self.neighbors[i]) 
        return k_nearest
    
    # gets the kth feature
    def get_feature(self,k):
        index = k-1
        return self.features[k-1]


    def print_neighbors(self):
        for n in self.neighbors:
            print(n)
    
    @classmethod
    def get_instances_count(cls):
        return cls.instances
    
        
        
        
    