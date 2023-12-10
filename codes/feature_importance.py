from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # Constants
# DS = "data/HR Employee Attrition.csv"
# RANDOM_SEED = 0

# # Read data set
# df = pd.read_csv(filepath_or_buffer=DS)

# # Data Cleaning
 
# df = df.select_dtypes(include='number')

# # Get feature importance
# X = df.drop('Attrition', axis=1)
# y = df['Attrition']

# model = RandomForestRegressor(random_state=RANDOM_SEED)
# model.fit(X, y)

# feature_importances = model.feature_importances_
# feature_names = X.columns
# importance_dict = dict(zip(feature_names, feature_importances))
# sorted_importance = np.array(sorted(importance_dict.items(), key=lambda x: x[1], reverse=True))

# plt.xlabel("Feature")
# plt.ylabel("Importance Index")
# plt.bar(sorted_importance[:, 0], sorted_importance[:, 1])
# plt.show()

def get_feature_importance(random_seed:int, data_set:pd.DataFrame, target_feature:str):
    # Separate traget column
    X = data_set.drop(target_feature, axis=1)
    y = data_set[target_feature]

    # Set model
    model = RandomForestRegressor(random_state=random_seed)
    model.fit(X, y)

    # Get feature importance
    feature_importances = model.feature_importances_
    feature_names = X.columns
    importance_dict = dict(zip(feature_names, feature_importances))

    return (np.array(sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)), model)