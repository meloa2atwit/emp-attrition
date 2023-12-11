from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np


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