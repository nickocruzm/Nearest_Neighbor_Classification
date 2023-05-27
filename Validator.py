from Node import Node
import math

    
def majority_vote(a, nearest_neighbors):
    total_votes = len(nearest_neighbors)
    class_1_votes = 0
    for n in nearest_neighbors:
        node = n['node']
        if(float(1.0) == node.TrueLabel):
            class_1_votes += 1
        
    class_2_votes = (total_votes - class_1_votes)
    if(class_1_votes > class_2_votes):
        return float(1.0)
    elif(class_2_votes > class_1_votes):
        return float(2.0)
    else:
        print("TIE")
        return(-1)

def Determine_Accuracy(NODES, feature_subset, k):
        accurate_computations = 0
        for i in range(0,len(NODES)):
            for j in range(i,len(NODES)):
                if i == j:
                    continue
                else:
                    nearest_neighbors = NODES[i].get_nearest_neighbors(k)
                    computed_Lbl = majority_vote(NODES[i],nearest_neighbors)
                    NODES[i].ComputedLabel = computed_Lbl
                    
        
            if(computed_Lbl == NODES[i].TrueLabel):
                accurate_computations += 1
        
        return accurate_computations/(len(NODES))
            
            
        
        

                    
                    
                        
                        
                        
                        
                        
                        
                    
                    
                    
                    
                    # try:
                    #     euclidean_dist(node, neighbor)
                        
                    # except IndexError:
                    #     print("...evaluating neighbors distance...")

                    
                    # finally:
                    #     print("...computing accuracy...")
   
    