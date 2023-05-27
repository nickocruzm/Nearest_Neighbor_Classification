from data_handler import *
from Validator import *
from Classifier import *
from Node import Node

if __name__ == '__main__':
    fileName = input("filename: ")
    
    # Read in DataFile
    raw_data = read_data(fileName)
    NODES = convert_data(raw_data)
    
    # Pass in feature subset wanted
    number_of_features = len(NODES[0].features)
    print(f'Features: 1 to {number_of_features}')
    print('input nums seperated by spaces of features to use for classification: EX) -> 2 5 7')
    print('if no input is given, classifier will default to using all features')
    feature_subset_str = input("Feature_subset: ")
    feature_subset = [int(x) for x in feature_subset_str.split()]
    
    print('how many (k)-neighbors would like to be used for classification: ')
    k = int(input('k_neighbors: '))
    
    compute_distances(NODES,feature_subset)
    
    
    
    
    # Accuracy
    accuracy = Determine_Accuracy(NODES,feature_subset,k)
    print(f'accuracy of {k}-Nearest Neighbors Classifier, using {len(feature_subset)} features: {accuracy*100}%')
    
    # classify
    print(f"insert ID of instance you'd like to classify from 1 to {len(NODES)}")
    # ID = int(input('id: '))
    
    # if(NODES[ID].ComputedLabel != None):
    
    
    
    

        
 
    
    
    