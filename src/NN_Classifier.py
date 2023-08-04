from Node import Node
import math

class NN_Classifier:
    
    @classmethod
    def euclidean_distance(cls, node_a: Node, node_b: Node, feature_subset: list()):
        distance = 0
        for k in feature_subset:
            x1, x2 = node_a.get_feature(k), node_b.get_feature(k)
            diff = math.pow((x1-x2), 2)
            distance = distance + diff
        distance = math.sqrt(distance)
        return distance
    
    @classmethod
    def compute_distances(cls,NODES,feature_subset):
        for i in range(0,len(NODES)):
            node = NODES[i]
            for j in range(i,len(NODES)):
                if i == j: continue
                else:
                    neighbor = NODES[j]
                    distance = NN_Classifier.euclidean_distance(node,neighbor,feature_subset)
                    NODES[j].update_neighbors({'node': node, 'distance': distance})
                    node.update_neighbors({'node':NODES[j], 'distance': distance})

    @classmethod
    def classify(cls, NODES, features):
        node = NODES[id_num - 1]
        compute_distances(NODES,feature_subset)
        for i in range(0,len(NODES)):
            NODES[i].sort_neighbors
            nearest_neighbor = NODES[i].neighbors[0]['node']

        
            
