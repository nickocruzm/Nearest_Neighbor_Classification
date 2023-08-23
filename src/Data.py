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

def default_accuracy(raw_data) -> float:
    """
        runtime: O(n);
        
        frequency of a classification divided by the total number of instances.
        returns the default accuracy of the data.       
    """
    A = 0; B = 0; total_instances = len(raw_data)

    for instance in range(0,total_instances): 
        if(raw_data[instance][0] == 1.0): A = A + 1
        else: B = B + 1
        
    most_frequent = max(A,B)
    return(most_frequent / total_instances)

def find_min_max(matrix):
    """  
        runtime: O(n^2)
        determines the min and max of each features.
    """
    num_rows = len(matrix); num_cols = len(matrix[0])
    # containers to hold the minmums and maximums of each column
    min_values = [float('inf')] * num_rows
    max_values = [float('-inf')] * num_cols

    # Find the min and max of each col
    # nested loop skips j=0, because that field contains the true instance's classification.
    for i in range(num_rows):
        for j in range(1,num_cols):
            if matrix[i][j] < min_values[j]: min_values[j] = matrix[i][j]
            if matrix[i][j] > max_values[j]: max_values[j] = matrix[i][j]
    return min_values, max_values

def normalize_data(data):
        """
            runtime: O(n^2)
            data is normalized by min and max values of each feature falling in between 0 and 1.
            returns dataset, with normalized data
        """
       
            
        mins,maxes = find_min_max(data)
        num_of_features = len(maxes)
        num_of_instances = len(data)
        
        # (i) column that is being iterated
        for i in range(1,num_of_features):
            # (j) instance being normalized
            for j in range(0,num_of_instances):
                data[j][i] = (data[j][i] - mins[i])/(maxes[i] - mins[i])
        
        return data
