from Data import *
from Validator import *
from NN_Classifier import *
from Node import Node

# outputs Trace by iterating through a list of node objects. Retrieving the node.id attribute, and nodes.neighbor that is at the top of list.
# Actual Accuracy is computed in Validator.py
def Accuracy_Trace(NODES):
    for node in NODES:
        print(f'object {node.id} is class {node.TrueLabel}')
        print(f"nearest_neighbor(s): {node.neighbors[0]['node'].id}, which is class {node.neighbors[0]['node'].TrueLabel}")

if __name__ == '__main__':
    fileName = input("filename: ")
    
    # Read in DataFile
    raw_data = read_data(fileName)
    NODES = convert_data(raw_data)
    
    # Pass in feature subset wanted
    number_of_features = len(NODES[0].features)
    print(f'Features: 1 to {number_of_features}')
    print('\t input nums seperated by spaces of features to use for classification: EX) -> 2 5 7')
    print('\t if no input is given, classifier will default to using all features')
    feature_subset_str = input("Feature_subset: ")
    feature_subset = [int(x) for x in feature_subset_str.split()]
    
    
    print('\t how many (k)-neighbors would like to be used for classification')
    k = int(input('k_neighbors: '))
    
    
    # Accuracy
    accuracy = Validator.Determine_Accuracy(NODES,feature_subset,k)
    print(f'\t accuracy of {k}-Nearest Neighbors Classifier, using features {feature_subset} features: {accuracy*100}%')
    
    #Accuracy_Trace(NODES)
    
    #classify
    print(f"insert ID of instance you'd like to classify from 1 to {len(NODES)}")
    id_num = int(input('id: '))
    NN_Classifier.classify(id_num,NODES,feature_subset,k)
  
 