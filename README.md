# Nearest Neighbor Classifier

## Overview
Designed and implemented Nearest-Neighbor Classifier in Python. Using two greedy algorithms to optimize classifier's accuracy. Normalized data with min-max normalization, accuracy computed using k-fold cross validation.

## Instructions

User must format data as a .txt file, and save data in datasets folder[^1]. All user interactions are done through the command line (CLI).

1. User prompted to input filename
   (ensure file is located in the defined path variable, defined in main.py)
2. If file is found program will output the number of instances, features, and default rate [^2] of the given dataset.
3. Choose action to perform, input the number associated with each action:
    1. Forward Selection
         - Output: The optimal subset of features along with its       accuracy.
    2. Backwards Elimination
         - Output: The accuracy using all features, the subset of features optimized by backwards elimination along with its accuracy. 
    3. test subset of features
         - Input: comma seperated subset of features
         - Output: classifer's accuracy using the given subset.



[^1]: If not wanting to place files in the declared path, alter the path (found in main.py)
[^2]: What the accuracy of classifying instances would be if classifications were done at random.

## Datasets

Datasets are formatted as .txt files, found in the datasets dir. Users may import datasets to use classifer on, see Dataset Formatting to better understand how to format imported datasets

Two test datasets are provided:

  - Small_dataset.txt, [100x10]
      - 100 Instansces
      - 10 Features[^3]
  - Large_dataset.txt [1000x100]
      - 1000 Instances
      - 100 Features

### Dataset Formatting
   - Each row represents an instance
   - The first column of each dataset is the instance's true label
   - Each column after the first is represents the features of instances
   - DATASET[instance][feature] will locate the particular insatance and the given feature. 

[^3]: The first column in each dataset are the true classifications of an instance. So there are number of features + 1 cols for each dataset.
For more information, please visit [https://nickocruzm.com](https://nickocruzm.com/), (site is under development)


