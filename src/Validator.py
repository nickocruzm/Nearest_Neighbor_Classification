from Node import Node
import math
from NN_Classifier import *



class Validator:
    
    @classmethod
    def leave_one_out_cross_validation(cls,Nodes,feature_subset,new_feature:int = -1):
        nearest_neighbor = None
        minimum_distance = float('inf')
        accuracy = 0
        total_instances = len(Nodes)
        
        if new_feature != -1:
            new_subset = feature_subset.copy()
            new_subset.append(new_feature)
        else:
            new_subset = feature_subset.copy()   
        NN_Classifier.compute_distances(Nodes, new_subset)
        accuracy = Validator.Determine_Accuracy(Nodes)
        return accuracy
    
    @classmethod
    def Determine_Accuracy(cls,Nodes):
        """
            Determines accuracy using only the features given in the feature_subset
            on the data set
        """
        accurate_computations = 0
        for i in range(0,len(Nodes)):
            if (Nodes[i].neighbors_sorted == False):
                Nodes[i].sort_neighbors()
                        
            nearest_neighbor = Nodes[i].neighbors[0]['node']
                    
            # nn_classification = NN_Classifier.majority_vote(NODES[i],nearest_neighbors)
            
            Nodes[i].NN_classification = nearest_neighbor.classification
                    
            if(Nodes[i].NN_classification == Nodes[i].classification):
                accurate_computations += 1
        
        return accurate_computations/len(Nodes)

