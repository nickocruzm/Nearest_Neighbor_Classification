class Node:
    instances = 1
    def __init__(self,data_row):
        self.id = Node.instances
        Node.instances += 1
        # The Classification that is given
        self.TrueLabel = data_row[0]
        
        # Features given
        self.features = data_row[1:]
        
        # The classification that is computed through the NN_Classifier
        self.ComputedLabel = None
        
        # neighbors of node formatted as [ {'node': Node object, 'distance': float} ]
        # 'node', holds pointer to node object
        # 'distance', is the euclidean distance computed
        self.neighbors = []
    
    # updates neighbors and sorts
    def update_neighbors(self,neighbor):
        self.neighbors.append(neighbor)
        self.neighbors = sorted(self.neighbors,key=lambda x:x['distance'])
    
    # neighbors already sorted in ascending order, get first (k) items
    def get_nearest_neighbors(self,k):
        k_nearest = []
        for i in range(0,k):
            k_nearest.append(self.neighbors[i])
        
        return k_nearest
    
    # gets the kth feature
    def get_feature(self,k):
        # index starts at 0, kth feature would be located feature[k-1]
        index = k-1
        return self.features[k-1]


    def print_neighbors(self):
        for n in self.neighbors:
            print(n)
    
    @classmethod
    def get_instances_count(cls):
        return cls.instances
    
        
        
        
    
    