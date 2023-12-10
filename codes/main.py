import pandas as pd
import matplotlib.pyplot as plt
import feature_importance

# Constants
DS = "data/HR Employee Attrition.csv"
RANDOM_SEED = 0

# Read data set
df = pd.read_csv(filepath_or_buffer=DS)

# Data cleaning
df["Attrition"].replace( {"Yes":1, "No":0}, inplace=True )
# df = df.select_dtypes(include='number')

# Set size of train data and test data
train_size = int(df.shape[0] * 0.8)
test_size = int(df.shape[0] - train_size)

# Random select training data
train_df = df.sample(n=train_size, frac=None, replace=False, random_state=RANDOM_SEED, weights=None, axis="index")


# TESTING
# rv = feature_importance.get_feature_importance(data_set=train_df, random_seed=RANDOM_SEED, target_feature="Attrition")
# print(rv)

# TESTING
# Identify columns with at least one NaN value
non_numerical_columns = df.select_dtypes(exclude='number').columns.tolist()
print(non_numerical_columns)

