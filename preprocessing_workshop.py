import pandas as pd

from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("housing.csv")

# Identify the missing values in the dataset
missing_values = data.isnull().sum()
print(missing_values)

# Handle the missing values by dropping or filling them with the mean of the column
# TODO: Choose your poison for NA values and activate only the preferred method
# Drop it like it's hot
# data = data.dropna()
# Fill it up!
data["total_bedrooms"].fillna(data["total_bedrooms"].mean(), inplace=True)

# Identify categorical features
categorical_features = data.select_dtypes(include=["object"]).columns

# TODO: Choose your poison for handling categorical values
# Encode the categorical features using one-hot encoding or label encoding
data = pd.get_dummies(data, columns=categorical_features)

"""
label_encoder = LabelEncoder()

for feature in categorical_features:
    data[feature] = label_encoder.fit_transform(data[feature])
"""

# Write the file to a new CSV
data.to_csv("housing_preprocessed.csv", index=False)
