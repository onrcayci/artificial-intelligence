import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

# read the csv data file
training_data = pd.read_csv("train.csv")

# get all the columns
all_columns = training_data.iloc[:, 0:7]

# pick last column for the target feature
last_column = training_data.iloc[:, -1]

# instantiate the classifier
classifier = ExtraTreesClassifier()

# train the classifier
classifier.fit(all_columns, last_column)

# plot the graph of feature importances for better visualization
feature_importances = pd.Series(classifier.feature_importances_, index=all_columns.columns)

# create a bar plot
feature_importances.plot(kind='bar')
plt.show()