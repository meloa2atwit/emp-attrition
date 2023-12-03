import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
DS = "data/HR Employee Attrition.csv"

# Read data set
df = pd.read_csv(filepath_or_buffer=DS)

# Split data set to train and test data
train_size = int(df.shape[0] * 0.8)
test_size = int(df.shape[0] - train_size)
train_df = df.sample(n=train_size, frac=None, replace=False, weights=None, axis="index")


## TESTING
print( train_df["Tr"])