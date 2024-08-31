from Node import Node
import logging
logging.basicConfig(filename='Data.log', filemode='a', level=logging.INFO)


def getFile():
    fileName = input("\n filename: ")
    filePath = "datasets/" + fileName
    
    logger = logging.getLogger(__name__)
    logger.info("File path")
    
    return filePath

def read_data(fileName:str) -> list():
    """
        read in the files contents, for each row
        convert data into float datatype, then place row into matrix.
        
        return: 2D matrix
    """
   
    matrix = []
    
    
    with open(fileName, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split() for line in lines]
    
    for row in data:
        matrix.append([float(x) for x in row])
    
    return matrix

def default_accuracy(data) -> float:
    """
        runtime: O(n);
        
        frequency of a classification divided by the total number of instances.
        returns the default accuracy of the data.       
    """
    A = 0; B = 0; total_instances = len(data)

    for instance in range(0,total_instances): 
        if(data[instance][0] == 1.0): A = A + 1
        else: B = B + 1
        
    most_frequent = max(A,B)
    return(most_frequent / total_instances)

def find_min_max(matrix):
    """  
        runtime: O(n^2)
        
        determines the min and max of each features.
    """
    
    number_of_rows = len(matrix)
    number_of_cols = len(matrix[0])
    
    # containers to hold the minmums and maximums of each column
    min_values = [float('inf')] * number_of_rows
    max_values = [float('-inf')] * num_cols

    # Find the min and max of each col
    # nested loop skips j=0, because that field contains the true instance's classification.
    
    for i in range(0,number_of_rows):
        for j in range(1,num_cols):
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

        for i in range(1,num_of_features):
            # (j) instance being normalized
            for j in range(0,num_of_instances):
                data[j][i] = (data[j][i] - mins[i])/(maxes[i] - mins[i])
        
        return data
