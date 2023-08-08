# Nearest Neighbor Classifier

## Overview
Designed and implemented Nearest-Neighbor Classifier in Python. Using two greedy algorithms to optimize classifier's accuracy. Normalized data with min-max normalization, accuracy computed using k-fold cross validation.

## Instructions

User must format data as a .txt file, and save data in datasets folder[^1]. All user interactions are done through a C.L.I.

1. User prompted to input filename
   (file will not be found if not defined by the path variable,       defined in main.py)
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

Datasets are read formatted as .txt files, found in the datasets folder. Two test datasets are provided:

  - Small_dataset.txt, [100x10]
      - 100 Instansces
      - 10 Features
  - Large_dataset.txt [1000x100]
      - 1000 Instances
      - 100 Features

If you'd like to know more about me or this project please visit [nickocruzm.com](https:://nickocruzm.com)


