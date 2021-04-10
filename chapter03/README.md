# Machine Learning Pipelines

## What is a machine learning pipeline?

From choosing the proper ingestion mechanism to data cleansing to feature engineering, the initial steps in a machine learning pipeline are just as important as model selection. Also being able to properly measure and monitor the performance of your model in production and diciding when and how to retrain your models can be the difference between great results and mediocre outcomes.

Many machine learning solutions exist to implement these pipelines. It is certainly possible to set up basic machine learning pipelines using just the Python or R languages. Some of the tools that data pipelines commonly leverage are:

- Hadoop
- Spark
- Spark Streaming
- Kafka
- Azure
- AWS
- Google Cloud Platform
- R
- SAS
- Databricks
- Python

One important item to consider is that each step on the pipeline produces an output that becomes the input for the next step in the pipeline. Machine learning pipelines can be cyclical and iterative. Every step in the pipeline might be repeated to achieve better results or cleaner data. Finally, the output variable might be used as input the next time the pipeline cycle is performed.

The main steps in a machine learning pipeline are:

1. **Problem Definition**: Define the business problem.
2. **Data Ingestion**: Identify and collect the dataset.
3. **Data Preparation**: Process and prepare the data using techniques such as:
   1. Impute missing values
   2. Remove duplicate records
   3. Normalize values (change numeric values in a dataset to use a common scale)
   4. Perform another type of cleanup or mappings
   5. Complete feature extraction
   6. Eliminate correlated features
   7. Perform feature engineering
4. **Data Segregation**: Split the data into a training set, validation set, and testing set.
5. **Model Training**: Train the machine models against the training dataset.
6. **Candidate Model Evaluation**: Measure the performance of the models using test and validation subsets of data to determine model accuracy.
7. **Model Deployment**: Once a model is chosen, deploy it into production for inference.
8. **Performance Monitoring**: Continuously monitor model performance, retrain, and calibrate accordingly. Collect new data to continue to improve the model and prevent it from becoming stale.

## Problem definition

Asking and framing the right question is paramount! It might mean the difference between making a technological breakthrough or failing, or it could be the difference between a startup company succeeding or the company going bankrupt.

## Data ingestion

Once you have crafted and polished your question to a degree to which you are satisfied with, the next step is to gather the raw data that will help you answer the question.

Important considerations:

- What data provider or vendor should be used? Can they be trusted?
- How will it be ingested? Hadoop, Impala, Spark, just Python, and so on?
- Should it be stored as a file or in a database?
- What type of database? Traditional RDBMS, NoSQL, graph.
- Should it even be stored? If we have a real-time feed into the pipeline, it might not even be necessary or efficient to store the input.
- What format should the input be? Parquet, JSON, CSV.

As of now, picking relevant input variables and setting up successful models still requires the data scientist to have domain knowledge. And in some cases intimate and deep domain knowledge.

## Data preparation

Processing the raw data. Some of the transformations that need to be done are:

- Data Cleaning
- Filtration
- Aggregation
- Augmentation
- Consolidation
- Storage

Some of the most popular stacks are built around:

- Azure ML service
- AWS SageMaker
- GCP Cloud ML Engine
- SAS
- RapidMiner
- Knime

One of the most popular tools to perform these transformations is Apache Spark, but it still needs a data store. For persistence, the most common solutions are:

- Hadoop Distributed File System (HDFS)
- HBase
- Apache Cassandra
- Amazon S3
- Azure Blob Storage

Some of the real-time data procesing solutions out there provide fault-tolerant, scalable, low-latency data ingestion. Some of the favorite ones are:

- Apache Kafka
- Azure Event Hubs
- AWS Kinesis

We need to ensure that the data is clean. More likely than not, the data will not be perfect, and the data quality will be less than optimal. The data can be unfit for several reasons:

### Missing values

Following are six different ways to deal with missing values:

- **Do Nothing**
- **Imputation using median values**
- **Imputationm using the most frequent value or a constant**

### Duplicate records or values

If two values are truly identical, it is easy to create a query or a program that can find duplicate values. The trouble starts if two records or values are supposed to identify the same entity but there is a slight difference between the two values. A traditional database query for duplicates might not find spelling errors, missing values, address changes, or people who left out their middle name. Some people use aliases.

Unless all the details match exactly, it is difficult to determine whether different records refer to the same entity. Additionally, often most duplicates are false positives. Two individuals might share the same name, address, and data of birth but still be different people. The solution to identifying duplicates is to use **fuzzy matching** instead of exact matching.

### Feature scaling

Datasets ofent contain features with varying magnitudes. This kind of variation in magnitudes in the features often has a detrimental effect on the accuracy of predictions. Many machine learning algorithm use Euclidean distance between the data points for their calculations. If we don't make the adjustment, features with a high order of magnitude will have an over-weighted impact on the results.

The most common methods for feature scaling are:

- Rescaling (min-max normalization)
- Mean normalization
- Standardization (Z-score normalization)
- Scaling to unit length

### Inconsistent values

Data can contain often inconsistent values. Furthermore, data can be inconsistent in a variety of ways.

Two approaches to handle this are rule-based and example-based. A rule-based system will work better when there is less variability in the data, and it doesn't change quickly. The rule-based approach breaks when we have fast moving data. Some time, we might want to consider a hybrid approach and use both methods.

## Data segregation

In order to train a model using the processed data, it is recommended to split the data into two subsets:

- Training data
- Test data

and sometimes into three:

- Training data
- Validation data
- Test data

The training data is visible to the model and it is trained on this data. The training creates and inference engine that can be later applied to new data points that the model has not previously seen. The test data represents this unseen data and it now can be used to make predictions on this previously unseen data.

## Model training

This is an iterative process and various algorithms might be tested until you have a model that sufficiently answers your question.

### Candidate model evaluation and selection

After the model training, an optimal model is selected for the problem at hand. We don't always pick the best performing model.

### Model deployment

It is typically exposed via an API and embedded in decision-making frameworks as part of an analytics solution.

How it gets exposed and deployed should be determined by the business requirements. Some questions to consider in the deployment selection:

- Does the system need to be able to make predictions in real-time (if yes, how fast?)
- How often do the models need to be updated?
- What amount of volume or traffic is expected?
- What is the size of the datasets?
- Are there regulations, policies and other constraints that need to be followed and abided by?

Regardless of the architecture chosen for the model deployment it is a good idea to use the following principles:

- **Reproducibility**
- **Automation**
- **Extensibility**
- **Modularity**
- **Testing**

### Performance monitoring

Once a model is deployed it must be closely monitored to make sure that the model is performing satisfactorily. 

#### Model performance

Performance in the data science context means how accuracte are the predictions. Data scientists monitoring machine learning models are primarily looking at a single metric: drift. Drift happens when the data no longer a relevant or useful input to the model. Data can change and lose its predictive value.

#### Operational performance

Machine learning pipelines are still software systems. For this reason, it's still important to monitor resource consumption, including:

- **CPU utilization**
- **Memory usage**
- **Disk usage**
- **Network I/O traffic**
- **Latency**
- **Throughput**

#### Total cost of ownership (TCO)

Companies should also be focues on the benefit they gain from the model versus the cost.

#### Service performance

Monitoring of the **service level agreements (SLAs)**