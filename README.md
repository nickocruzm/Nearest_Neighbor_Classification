# Nearest Neighbor Classifier

Designed and implemented a Nearest-Neighbor Classifier in Python, employing two greedy algorithms to optimize accuracy. Normalized data using min-max normalization, with accuracy evaluated through k-fold cross-validation.


## Datasets


| Dataset | Instances | Features |
| ------- | --------- | -------- |
| Small   | 100       | 10       |
| Large   | 1000      | 40       |


![DataTable](images/dataTable.png)



Datasets are formatted as .txt files, found in the datasets dir. Users may import datasets to use classifer on, see Dataset Formatting to better understand how to format imported datasets.


### Dataset Formatting
   - Each row represents an instance
   - The first column of each dataset is the instance's true label
   - Each column after the first is represents the features of instances
   - DATASET[instance][feature] will locate the particular insatance and the given feature.

### Feature Selection

   Feature Selection significantly improves the accuracy of classifiers. When comparing the accuracy results of a classifier using all features to one using a subset we often see an increase in accuracy with the subset.
   
   Feature selection narrows down the features used in classification, leading to faster computation when classifying new instances. Forward Selection tends to reduce the number of features more drastically than Backward Elimination, resulting in shorter future runtimes. However, the significant reduction in features with Forward Selection may indicate potential overfitting.

   The cost of applying feature selection is justified by the accuracy improvement it provides. However, in cases where the accuracy increase is negligible, the expense may not be warranted. Factors such as the desired accuracy, the applicability of the feature subset to future datasets, and the variability of feature values must be considered to avoid overfitting.

   While Forward Selection produces a simpler model with high accuracy, the risk of overfitting is higher. On the other hand, Backward Elimination, though less aggressive in reducing the feature set, minimizes the potential for overfitting, potentially leading to more accurate future classifications.


## Scatter Plots


![largeDataset Scatterplot](images/large_scatter.png)

![smallDataset Scatterplot](images/small_scatter.png)

[^3]: The first column in each dataset are the true classifications of an instance. So there are number of features + 1 cols for each dataset.




