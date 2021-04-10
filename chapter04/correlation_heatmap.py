import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

# all independent columns
columns = data.iloc[:, 0:7]

# target feature
target = data.iloc[:, -1]

# get the correlations between each feature
correlation_matrix = data.corr()

# get the most correlated features
top_correlations = correlation_matrix.index

# plot the correlation heatmap using the most correlated features
plt.figure(figsize=(20, 20))
sns.heatmap(data[top_correlations].corr(), annot=True, cmap="RdYlGn")
plt.show()