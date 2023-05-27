from Node import Node
import math
def convert_data(raw_data):
    NODES = []
    for instance in raw_data:
        NODES.append(Node(instance))
    
    return NODES
def euclidean_distance(a,b,feature_subset):
    distance = 0
    for k in feature_subset:
        x1 = a.get_feature(k)
        x2 = b.get_feature(k)
        
        diff = math.pow( (x1-x2), 2)
        distance = distance + diff
    
    distance = math.sqrt(distance)
    return distance

def compute_distances(NODES,feature_subset): 
    # for every i-th node:
    for i in range(0,len(NODES)):
        node = NODES[i]
        for j in range(0,len(NODES)):
            if i == j:
                continue
            else:
                neighbor = NODES[j]
                distance = euclidean_distance(node,neighbor,feature_subset)
                node.update_neighbors({'node':NODES[j], 'distance': distance})



    