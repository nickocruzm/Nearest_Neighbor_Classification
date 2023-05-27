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



#fileName = input('data files name: ')                      
# raw_data = read_data(fileName)

# # convert data into NODES
# NODES = convert_data(raw_data)

# compute_distances(NODES,[3,5,7])

# Determine_Accuracy(NODES, [3,5,7], 1)

# print(acc)
