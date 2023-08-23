from Node import Node
from Data import *
from NN_Classifier import *
from Validator import *
from Search import *

if __name__ == '__main__':
    path = "datasets/"
    fileName_str = input("fileName: ")
    fileName = path + fileName_str
    raw_data = read_data(fileName)
    
    normalized_data = normalize_data(raw_data)
    Nodes = Data_to_Nodes(normalized_data)
    
    
    default_Rate = default_accuracy(raw_data)
    print(f'{fileName_str} contains {len(Nodes)} instances each with {len(Nodes[0].features)} Features, with a default rate of {default_Rate} \n')
    

    
    print("choose one: \t 1. Forward Selection \t 2: Backwards Elmination \t 3. Test Subset of Features ")
    choice = int(input("-> "))
    
    if(choice == 1): 
        best_features,best_accuracy = forward_selection(normalized_data)
        print(f'best subset of features{best_features}, accuracy: {best_accuracy}')

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
       
        # calculate the distances between nodes
        NN_Classifier.compute_distances(Nodes, feature_subset)
        
        # compute accuracy of the given subset of features
        accuracy = Determine_Accuracy(Nodes)
        print(f'\t accuracy of Nearest Neighbor Classifier, using features {feature_subset} features: {accuracy}')

    

