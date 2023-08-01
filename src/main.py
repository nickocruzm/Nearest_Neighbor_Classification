from Data import *
from Validator import *
from NN_Classifier import *
from Node import Node
from Search import *

# outputs Trace by iterating through a list of node objects. Retrieving the node.id attribute, and nodes.neighbor that is at the top of list.
# Actual Accuracy is computed in Validator.py
# def Accuracy_Trace(NODES):
#     for node in NODES:
#         print(f'object {node.id} is class {node.TrueLabel}')
#         print(f"nearest_neighbor(s): {node.neighbors[0]['node'].id}, which is class {node.neighbors[0]['node'].TrueLabel}")

if __name__ == '__main__':
    path = "/Users/nickocruz/Developer/GitHub/Project_2_MachineLearning/datasets/"
    fileName_str = input("fileName: ")
    fileName = path + fileName_str
    raw_data = read_data(fileName)
    
    normalized_data = normalize_data(raw_data)
    Nodes = Data_to_Nodes(normalized_data)
    
    
    default_Rate = (raw_data)
    print(f'\t {fileName} \n Quantities: Instance = {len(Nodes)}, Features = {len(Nodes[0].features)}  \n default rate: {default_Rate}')
    

    
    print("choose one:\n \t 1. Forward Selection \n\t 2: Backwards Elmination \n\t 3. Test Subset of Features ")
    choice = int(input("-> "))
    
    if(choice == 1): 
        best_features = forward_selection(normalized_data)
    if(choice == 2):
        all_features = [i for i in range(1,len(Nodes[0].features)+1)]
        accuracy = get_accuracy(Nodes, all_features)
        print(f'Using all features gives an accuracy of {accuracy}')
        best_features = Backward_elimination(normalized_data, accuracy)
        
    if(choice == 3):
        number_of_features = len(Nodes[0].features)
        print(f'Features: 1 to {number_of_features}')
        print('\t input nums seperated by spaces of features to use for classification: EX) -> 2 5 7')
        print('\t if no input is given, classifier will default to using all features')
        feature_subset_str = input("Feature_subset: ")
        feature_subset = [int(x) for x in feature_subset_str.split()]
        k = 1
        
        # Accuracy
        NN_Classifier.compute_distances(Nodes, feature_subset)
        accuracy = Validator.Determine_Accuracy(Nodes)
        print(f'\t accuracy of {k}-Nearest Neighbors Classifier, using features {feature_subset} features: {accuracy}')

    

