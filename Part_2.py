import numpy as np
from Node import Node
from Validator import Determine_Accuracy
import math
def read_data(fileName) -> np.array:
    # Read the file
    with open(fileName, 'r') as file:
        # Read lines and split by whitespace
        lines = file.readlines()
        data = [line.strip().split() for line in lines]

    # Convert data to a numpy array
    matrix = np.array(data, dtype=float)
    return matrix

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
        for j in range(i,len(NODES)):
            if i == j:
                continue
            else:
                neighbor = NODES[j]
                distance = euclidean_distance(node,neighbor,feature_subset)
                node.update_neighbors({'node':NODES[j], 'distance': distance})



                      
raw_data = read_data('small_test_dataset.txt')

# convert data into NODES
NODES = convert_data(raw_data)



compute_distances(NODES,[3,5,7])

acc = Determine_Accuracy(NODES, [3,5,7], 1)

print(acc)
