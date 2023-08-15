import numpy as np
from Node import Node

def read_data(fileName:str)-> list():
    """
        read in the files contents, for each row
        convert data into float datatype, then place row into matrix.
        
        return: 2D Matrix
    """
    matrix = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split() for line in lines]
    for row in data:
        matrix.append([float(x) for x in row])
    
    return matrix

def Data_to_Nodes(raw_data) -> list():
    """
        Turns data instances into Nodes, placing them within a container to be returned.
    """
    return [Node(n) for n in raw_data]

def default_accuracy(raw_data) -> float:
    """
        default accuracy := frequency of a class divided by the total number of instances.
        returns the default accuracy of the data.        
    """
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
        """
            1st closure contained in normalize_data()
            using the minimum values and maximum values returned from find_min_max(),
            data is normalized falling in between 0 and 1.
            
            returns dataset, with normalized data
        """
        def find_min_max(matrix):
            """
                2nd clousure contained in normalize_data()
                
                return 2 arrays, of the min and max values for each column.
            """
            num_rows = len(matrix)
            num_cols = len(matrix[0])
            
            # containers to hold the minmums and maximums of each column
            min_values = [float('inf')] * num_cols
            max_values = [float('-inf')] * num_cols
            
            # Find the min and max of each col, nested loop skips j=0, because that field contains the true instance's classification.
            for i in range(num_rows):
                for j in range(1,num_cols):
                    if matrix[i][j] < min_values[j]: min_values[j] = matrix[i][j]
                    if matrix[i][j] > max_values[j]: max_values[j] = matrix[i][j]
            return min_values, max_values
            
        mins,maxes = find_min_max(data)
        num_of_features = len(maxes)
        num_of_instances = len(data)
        
        # (i) column that is being iterated
        for i in range(1,num_of_features):
            # (j) instance being normalized
            for j in range(0,num_of_instances):
                data[j][i] = (data[j][i] - mins[i])/(maxes[i] - mins[i])
        
        return data
    
    return min_max_normalization(raw_data)

def get_nearest_neighbors(distances_memory, instance):
    """
        for the distances in memory, retrieve the minimum distance in relative to the given instance
    """
    return min(distances_memory[instance])
