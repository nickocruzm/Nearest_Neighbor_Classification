import numpy as np
from Node import Node

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

