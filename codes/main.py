import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
DS = "data/HR Employee Attrition.csv"
RANDOM_SEED = 0

# Read data set
df = pd.read_csv(filepath_or_buffer=DS)

# Split data set to train and test data
train_size = int(df.shape[0] * 0.8)
test_size = int(df.shape[0] - train_size)
train_df = df.sample(n=train_size, frac=None, replace=False, random_state=RANDOM_SEED,weights=None, axis="index")


## TESTING
cols = train_df.columns
for idx, c in enumerate(cols):
    print(f"{idx+1}. {c}\n")