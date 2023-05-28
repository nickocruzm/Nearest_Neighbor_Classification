from Node import Node
from NN_Classifier import *



class Validator:
    
    @classmethod
    def Determine_Accuracy(cls,NODES, feature_subset, k):
            if(len(NODES[0].neighbors) == 0):
                NN_Classifier.compute_distances(NODES,feature_subset)
            
            
            accurate_computations = 0
            for i in range(0,len(NODES)):            
                for j in range(i,len(NODES)):
                    if i == j:
                        continue
                    else:
                        nearest_neighbors = NODES[i].get_nearest_neighbors(k)
                        
                        computed_Lbl = NN_Classifier.majority_vote(NODES[i],nearest_neighbors)
                        NODES[i].ComputedLabel = computed_Lbl
                        
                if(computed_Lbl == NODES[i].TrueLabel):
                    accurate_computations += 1
            
            return accurate_computations/(len(NODES))
   
    