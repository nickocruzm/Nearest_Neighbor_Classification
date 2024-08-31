from Node import Node

import logging
logging.basicConfig(filename='prgm.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    filemode='a',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def getFile():
    fileName = input("\n filename: ")
    filePath = "datasets/" + fileName
    
    logger.info("getFile()")
    
    return filePath

def read_data(fileName:str) -> list():
    """
        read in the files contents, for each row
        cast data into float datatype, then place row into matrix.
        
        return: 2D matrix
    """
   
    matrix = []
    
    
    with open(fileName, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split() for line in lines]

    # Type Casting [x: string -> float]
    # append row to matrix
    for row in data:
        matrix.append([float(x) for x in row])
    
    return matrix

def default_accuracy(data) -> float:
    """
        runtime: O(n);
        
        Finds the most frequent classification 
        then divides it by the total number of instances.
        
        returns float.       
    """
    # classA represents classification 1.0
    # classB represents classification 2.0
    
    classA = 0
    classB = 0
    
    total_instances = len(data)
    
    # count number of instances classified as 1.0 and 2.0
    for instance in range(0,total_instances): 
        if(data[instance][0] == 1.0): classA = classA + 1
        else: classB = classB + 1
    
    # most frequent classification in dataset
    most_frequent = max(classA,classB)
    
    
    return(most_frequent / total_instances)

def find_min_max(matrix):
    
    """  
        runtime: O(n^2)
        
        determines the min and max of each set of features.
        matrix columns contain feature values.
        
        returns: list of min values and max values as a tuple.
    """
    
    number_of_rows = len(matrix)
    number_of_cols = len(matrix[0])
    
    # containers to hold the minmums and maximums of each column
    min_values = [float('inf')] * number_of_rows
    max_values = [float('-inf')] * number_of_cols

    # Find the min and max of each col
    #   (i) moves along the y-axis, traversing rows.
    #   (j) moves along the x-axis, traversing columns.
    #        nested loop skips j=0, because that field contains the instance's true classification.
    #   Traverse each row checking if that column's value is a min or max of that feature
    #  if min or max is found store value in container
    for i in range(0,number_of_rows):
        for j in range(1,number_of_cols):
            if matrix[i][j] < min_values[j]: min_values[j] = matrix[i][j]
            if matrix[i][j] > max_values[j]: max_values[j] = matrix[i][j]
            
    return min_values, max_values

def normalize_data(data):
    
        """
            runtime: O(n^2)
            
            data is normalized by min and max values of each feature falling in between 0 and 1.
            returns dataset, with normalized data.
            
        """
       
            
        mins,maxes = find_min_max(data)
        num_of_features = len(maxes)
        num_of_instances = len(data)
        

        # Ignore first column
        #   Because first column contains true classifications
        # iterating down each column to normalize elements.
        for j in range(1,num_of_features):
            for i in range(0,num_of_instances):
                data[i][j] = (data[i][j] - mins[j])/(maxes[j] - mins[j])
        
        return data
