# Feature Selection and Feature Engineering

Feature selection - also known as variable selection, attribute selection, or variable subset selection - is a method used to select a subset of features (variables, dimensions) from an initial dataset.

Feature selection is important because it can:

- Shorten training times
- Simplify models and make them easier to interpret
- Enhances testing set performance by reducing overfitting

One important reason to drop features is the high correlation and redundancy between input variables or the irrelevancy of certain features. These input variables can thus be removed without incurring much loss of information.

Feature engineering in some ways is the opposite of feature selection. With feature selection, you remove variables. In feature engineering, you create new variables to enhance the model. In many cases. you are using domain knowledge for the enhancement.

## Feature selection

A critical component of the machine learning pipeline is deciding which features will be used as inputs to the model. It is important to lower the amount of input features for a variety of reasons including:

- Reducing the multi collinearity of the input features will make the machine learning model parameters easier to interpret. *Multicollinearity* (also *collinearity*) is a phenomenon observed with features in a dataset where one predictor feature ina a regression model can be linearly predicted from the other's features with a sustantial degree of accuracy.
- Reducing the time required to run the model and the amount of storage space the model needs will allow us to run more variations of the models leading to quicker and better results.
- The smaller number of input features a model requires, the easier it is to explain it. When the number of features goes up, the explainability of the model goes down.
- As the number of dimensions increases, the possible configurations increase exponentially, and the number of configurations covered by an observation decreases. As you have more features to describe your target, you might be able to describe the data more precisely, but your model will not generalize with new data points - your model will overfit the data. This is known as the *curse of dimensionality*.

Exploratory data analysis can be a good way to get an intuitive understanding and to obtain insights into the dataset we are working with. The following are three approaches that are commonly used to obtain these insights:

- Feature importance
- Univariable selection
- Correlation matrix with heatmap

### Feature importance

Feature importance provides a score for each feature in a dataset. A higher score means the feature has more importance or relevancy in relation to the output feature.

### Univariate selection

Statistical tests can be used to determine which features have the strongest correlation to the output variable. The scikit-learn library has a class called `SelectKBest` that provides a set of statistical tests to select the K "best" features in a dataset.