import random
import time
import numpy as np

def euclidean_dist(a,b,arr):
    # Caluculates the distance between the 2 instances a and b.
    rolling_sum = 0
    inst_a = arr[a-1]
    inst_b = arr[b-1]
    # print(f'a: {inst_a}')
    # print(f'b: {inst_b}')
    for i in range(1, len(inst_a)):
        diff = np.power( inst_a[i] - inst_b[i],2)
        rolling_sum = rolling_sum + diff
    return np.sqrt(rolling_sum)


        
        
    

def leave_one_out_cross_validation(data,current_set,feature_to_add):
    num_of_instances = len(data)
    correct_classification = 0
    neighbors = []
    for i in range(0,num_of_instances):
        object_to_classify = data[i][0]
        
        for j in range(0,num_of_instances):
            if(j == i):
                neighbors.append(float('inf'))
            else:
                d = euclidean_dist(i,j,data,)
                neighbors.append(d)
        

        loc = neighbors.index(min(neighbors))
        
        if(data[i][0] == data[loc][0]):
            correct_classification = correct_classification + 1
            
    return correct_classification/len(data)
            
    
    
        
        
            
        
        

def forward_selection(data):
    current_feature_set = list()
    features = data
    #features = data[0].size()
    for i in range(1,features):
        print(f'Level {i} of tree')
        new_feature = None
        best_accuracy = 0
        
        for k in range(1,features+1):
            if k not in current_feature_set:
                accuracy = leave_one_out_cross_validation(data,current_feature_set,k)
                
                print(f'\t ...Considering: feature {k}, with accuracy: {accuracy}')
                
                if accuracy > best_accuracy:
    #                print(f'best accuracy: {best_accuracy} => {accuracy}')
                    best_accuracy = accuracy
                    new_feature = k
        
        if(new_feature != None):
            current_feature_set.append(new_feature)
            print(f'on level {i}, feature {new_feature} was added, result: {current_feature_set}')

def Backwards_elimination(data):
    features = data
    current_features_set = list()
    current_accuracy = 100*round(random.random(),3)
    for ft in range(1,data+1):
        current_features_set.append(ft)
        
    for i in range(1,features + 1):
        print(f'Level {i} of tree')
        dropped_feature = None
        for k in range(1,features+1):
            if k in current_features_set:
                accuracy = leave_one_out_cross_validation(data,current_features_set,k)
                
                print(f'\t ...Considering: dropping feature {k}, with accuracy: {accuracy}')
                
                if accuracy < current_accuracy:
    #                print(f'best accuracy: {best_accuracy} => {accuracy}')
                    current_accuracy = accuracy
                    dropped_feature = k
        
        if(dropped_feature != None):
            current_features_set.remove(dropped_feature)
            print(f'on level {i}, feature {dropped_feature} was dropped, result: {current_features_set}')
            
    print(f'Final Chosen Features using Backwards Elimination: {current_features_set}')      

           
if __name__ == '__main__':
    print("Welcome to Nicko Martinez's Feature Selection Algorithm")
    feature_num = int(input("Please enter total number of features: "))
    print("""
        Type the number of the algorithm you want to run: \n
        \t 1) Forward Selection \n
        \t 2) Backward Elimination \n 
    """ )
    algorithm_choice = int(input("Algo Choice: "))
    data = feature_num
    try:
        if(algorithm_choice == 1): forward_selection(data)
        if(algorithm_choice == 2): Backwards_elimination(data)
        
    finally:
        print("\n \t done")
        
 
    
    
    