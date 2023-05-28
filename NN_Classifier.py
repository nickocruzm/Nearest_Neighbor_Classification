from Node import Node
import math

class NN_Classifier:
        
    @classmethod
    def euclidean_distance(cls,a,b,feature_subset):
        distance = 0
        for k in feature_subset:
            x1 = a.get_feature(k)
            x2 = b.get_feature(k)
            
            diff = math.pow( (x1-x2), 2)
            distance = distance + diff
        
        distance = math.sqrt(distance)
        return distance

    @classmethod
    def compute_distances(cls,NODES,feature_subset): 
        # for every i-th node:
        for i in range(0,len(NODES)):
            node = NODES[i]
            for j in range(0,len(NODES)):
                if i == j:
                    continue
                else:
                    neighbor = NODES[j]
                    distance = NN_Classifier.euclidean_distance(node,neighbor,feature_subset)
                    node.update_neighbors({'node':NODES[j], 'distance': distance})

    @classmethod
    def majority_vote(cls,a, nearest_neighbors):
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

    @classmethod
    def classify(cls,id_num, NODES, feature_subset, k):
        # get node to classify
        node = NODES[id_num -1]
        if(node.ComputedLabel != None):
            print(f'classifying Object_{id_num}')
            print(f"\t {k}-nearest neighbors: (id, classification) = {[(i['node'].id, i['node'].TrueLabel) for i in node.get_nearest_neighbors(k)]}")
            print(f'Object classified as: {node.ComputedLabel}')
            print(f'True classification is: {node.TrueLabel}')
        else:
            compute_distances(NODES,feature_subset)
            for i in range(0,len(NODES)):
                nearest_neighbors = NODES[i].get_nearest_neighbors(k)
                computed_Lbl = majority_vote(NODES[i],nearest_neighbors)
                NODES[i].ComputedLabel = computed_Lbl

 
    
    