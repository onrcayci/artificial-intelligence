import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

training_data = pd.read_csv("train.csv")

# get all columns of training data
all_columns = training_data.iloc[:, 0:7]

# get the last column of training data as the target feature
last_column = training_data.iloc[:, -1]

# apply SelectKBest class to extract top 5 features
best_features = SelectKBest(score_func=chi2, k=5)

# fit the training data according to the target feature
training = best_features.fit(all_columns, last_column)

# convert the scores into a pandas data frame
dfscores = pd.DataFrame(training.scores_)

# convert the columns into a pandas data frame
dfcolumns = pd.DataFrame(all_columns.columns)

# concatenate the data frames
scores = pd.concat([dfcolumns, dfscores], axis=1)

# update column names
scores.columns = ["specs", "score"]

# print the dataset
print(scores)