# Nearest Neighbor Classifier

Designed and implemented a Nearest-Neighbor Classifier in Python, employing two greedy algorithms to optimize accuracy. Normalized data using min-max normalization, with accuracy evaluated through k-fold cross-validation.


![DataTable](images/dataTable.png)

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

### Feature Selection
   Feature Selection greatly improves the accuracy of classifiers. When comparing the accuracy results of a classifier using all features, with a classifier using only a subset of features we notice an increase in accuracy for the classifier when used with a subset of features. However, this is not the case for the default rates of the datasets. The Default Rates seem to be greater than the accuracies produced by Backwards Elimination, whereas Forward Selection seems to produce a greater accuracy than the default rate. 
After applying feature selection, the features used during classification are narrowed, as a fortunate consequence this also allows faster computation in the future when classifying new instances. Using Forward Search narrows the features down more so than Backwards elimination, which decreases future runtimes more so. However the great decrease in features after applying Forward Search may indicate that the subset of features has been overfitted.
   The cost of applying feature selection to a dataset can be justified by the increase in accuracy. However, there are instances where a feature selection is too expensive such as when the increase in accuracy is negligible. To justify the cost of computing a subset of features certain factors must be determined such as; the desired accuracy compared with the current, if the resulting feature subset be used on future data sets or do the values of features greatly varying indicating the subset of features to be overfitted to the current data set.
   While Forward Selection provides a simple model with high accuracy, the potential of the subset features being overfitted is great. Whereas Backwards elimination does not greatly narrow down the subset of features, it does decrease the potential of overfitting which may lead to more accurate future classifications.


## Scatter Plots


![largeDataset Scatterplot](images/large_scatter.png)

![smallDataset Scatterplot](images/small_scatter.png)

[^3]: The first column in each dataset are the true classifications of an instance. So there are number of features + 1 cols for each dataset.




