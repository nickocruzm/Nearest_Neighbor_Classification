import numpy as np



features = { 1: 35.4, 2: 56.7, 3: 41.4, 4: 28.5 }

Default_Rate = 55.4


print(f'Using no features and "random" evaluation, I get an accuracy of {Default_Rate}')

best_feature_accuracy = 0
chosen_features = dict()


for ft in features:
    ft_accuracy = features.get(ft)
    print(f'Using feature(s) {ft}, accuracy is x)%')
    # if(best_feature_accuracy < ft_accuracy):
    #     chosen_features[]
        
        
    

