import random
import time
import numpy as np

def leave_one_out_cross_validation(data,current_set,feature_to_add):
    random.seed(time.time())
    acc = round(100*random.random(), 3)
    return acc

def feature_search_demo(data):
    current_feature_set = list()
    cols = len(data[0])
    for i in range(1,cols):
        print(f'Level {i} of tree')
        level_feature_added = list()
        new_feature = None
        best_accuracy = 0
        
        for k in range(1,cols):
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
                
    
data = np.random.randint(10, size=(5,5))

feature_search_demo(data)