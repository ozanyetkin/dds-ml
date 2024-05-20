# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# Load the dataset and observe by printing
data = pd.read_csv("your_dataset.csv")
print(data)

# Split the dataset into training and testing sets
train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

# Identify the missing values in the dataset
missing_values = data.isnull().sum()

# Handle the missing values by dropping or filling them with the mean of the column
data = data.dropna()
data["column_name"].fillna(data["column_name"].mean(), inplace=True)

# Identify categorical features
categorical_features = data.select_dtypes(include=["object"]).columns

# Encode the categorical features using one-hot encoding or label encoding
encoded_data = pd.get_dummies(data, columns=categorical_features)

label_encoder = LabelEncoder()

for feature in categorical_features:
    data[feature] = label_encoder.fit_transform(data[feature])

# Normalize the numerical features
scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(data)
