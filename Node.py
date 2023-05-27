class Node:
    instances = 1
    def __init__(self,data_row):
        self.id = Node.instances
        Node.instances += 1
        self.TrueLabel = data_row[0]
        self.features = data_row[1:]
        self.ComputedLabel = None
        self.neighbors = []
    
    def update_neighbors(self,neighbor):
        self.neighbors.append(neighbor)
        self.neighbors = sorted(self.neighbors,key=lambda x:x['distance'])
        
    def get_nearest_neighbors(self,k):
        k_nearest = []
        # neighbors already sorted in ascending order, just get first (k) items
        for i in range(0,k):
            k_nearest.append(self.neighbors[i])
        
        return k_nearest
    
    def get_feature(self,k):
        index = k-1
        return self.features[k-1]

    def print_neighbors(self):
        for n in self.neighbors:
            print(n)
    
    @classmethod
    def get_instances_count(cls):
        return cls.instances
    
        
        
        
    
    