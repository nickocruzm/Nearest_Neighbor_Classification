from Node import Node
from Data import *
from Validator import *

def get_accuracy(nodes, features):
    accurate_classifications = 0
    NN_Classifier.compute_distances(nodes,features)
    for i in range(0,len(nodes)):
        nodes[i].sort_neighbors()
        nearest_neighbor = nodes[i].neighbors[0]['node']
        if(nearest_neighbor.classification == nodes[i].classification):
            accurate_classifications += 1
    
    return accurate_classifications / len(nodes)

def leave_feature_out(nodes, features, f):
    subset = features.copy()
    subset.remove(f)
    accurate_classifications = 0
    NN_Classifier.compute_distances(nodes,subset)
    for i in range(0,len(nodes)):
        nodes[i].sort_neighbors()
        nearest_neighbor = nodes[i].neighbors[0]['node']
        if(nearest_neighbor.classification == nodes[i].classification):
            accurate_classifications += 1
    
    return accurate_classifications / len(nodes)

def forward_selection(raw_data, default_accuracy:float=0.0): 
    last_best_found = 0
    total_features = len(raw_data[0])-1             # number of features starting at col[1]
    best_feature = -1
    best_accuracy = default_accuracy
    feature_subset = []                            # contains the features with the best accuracy

    for i in range(1,total_features+1):
        if(last_best_found >= 1):
            break    
        for j in range(1,total_features+1):
            node_set = Data_to_Nodes(raw_data)
            new_feature = j
            if new_feature not in feature_subset:
                accuracy = leave_one_out_cross_validation(node_set, feature_subset, new_feature)
                #print(f'current: {feature_subset}, new_feature: {new_feature}, accuracy: {accuracy}')
                
            if(accuracy >= best_accuracy):
                best_feature = new_feature
                best_accuracy = accuracy   
        
        if best_feature != -1:
            last_best_found = 0
            feature_subset.append(best_feature)
            best_feature = -1
        
        else:
            last_best_found += 1
        
        #print(f'Level: {i} \n\tBest Feature Subset: {feature_subset} with an accuracy {best_accuracy}')
    return feature_subset,best_accuracy

def Backward_elimination(data, Threshold):
    features = len(data[0])
    current_features_set = [i for i in range(1,features)]
    best_accuracy = Threshold
        
    for i in range(1,features+1):
        dropped_feature = None
        for k in range(1,features+1):
            if k in current_features_set:
                Nodes = Data_to_Nodes(data)
                subset = list(current_features_set[:])
                accuracy = leave_feature_out(Nodes,subset,k)
                
                print(f'Features{subset}, after dropping feature {k} accuracy: {accuracy}')
            
                if(accuracy > best_accuracy):
                    best_accuracy = accuracy
                    dropped_feature = k
                
                    
        if dropped_feature != None:
            current_features_set.remove(dropped_feature)
            print(f'dropped feature {dropped_feature}, current_feature subset: {current_features_set}')
        else:
            break
    
    print(f'\t{current_features_set}')
    Nodes = Data_to_Nodes(data)
    NN_Classifier.compute_distances(Nodes, current_features_set)
    acc = Determine_Accuracy(Nodes)
          
    print(f'Final Chosen Features using Backwards Elimination: {current_features_set}, with an accuracy of {acc}')

    