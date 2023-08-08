import numpy as np
from Node import Node

def read_data(fileName):
    matrix = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split() for line in lines]
    for row in data:
        matrix.append([float(x) for x in row])
    
    return matrix

def Data_to_Nodes(raw_data):
    return [Node(n) for n in raw_data]

def default_accuracy(raw_data):
    A = 0
    B = 0
    total_instances = len(raw_data)
    for instance in range(0,total_instances): 
        if(raw_data[instance][0] == 1.0): A = A + 1
        if(raw_data[instance][0] == 2.0): B = B + 1
        
    most_frequent = max(A,B)
    return(most_frequent / total_instances)

def normalize_data(raw_data):
    def min_max_normalization(data):
        def find_min_max(matrix):
            num_rows = len(matrix)
            num_cols = len(matrix[0])

            min_values = [float('inf')] * num_cols
            max_values = [float('-inf')] * num_cols

            for i in range(num_rows):
                for j in range(1,num_cols):
                    if matrix[i][j] < min_values[j]: min_values[j] = matrix[i][j]
                    if matrix[i][j] > max_values[j]: max_values[j] = matrix[i][j]
            return min_values, max_values
            
        mins,maxes = find_min_max(data)
        num_of_features = len(maxes)
        num_of_instances = len(data)
        
        for i in range(1,num_of_features):
            for j in range(0,num_of_instances):
                data[j][i] = (data[j][i] - mins[i])/(maxes[i] - mins[i])
        
        return data
    
    return min_max_normalization(raw_data)
def get_nearest_neighbors(distances_memory, instance):
    """
        for the distances in memory, retrieve the minimum distance in relative to the given instance
    """
    return min(distances_memory[instance])
