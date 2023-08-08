# Nearest Neighbor Classifier

## Overview
Designed and implemented Nearest-Neighbor Classifier in Python. Using two greedy feature search algorithms to optimize classifier's accuracy. Accuracy computed using k-fold cross validation.

## Instructions

User must format data as a .txt file, and save data in datasets folder[^1]. All user interactions are done through a C.L.I.

1. User prompted to input filename
   (file will not be found if not defined by the path variable,       defined in main.py)
2. If file is found program will output the number of instances, features, and default rate [^2] of the given dataset.
3. Choose:
    1. Forward Selection
         - Outputs: The optimal subset of features along with its       accuracy.
    3. Backward Selection
    4. test subset of features



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



