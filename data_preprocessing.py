# Importing necessary libraries and modules
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
from sklearn.linear_model import LinearRegression

# Load the dataset and observe by printing
data = pd.read_csv("housing.csv")
print(data)

# Identify the missing values in the dataset
missing_values = data.isnull().sum()
print(missing_values)

# Handle the missing values by dropping or filling them with the mean of the column
# TODO: Choose your poison for NA values and activate only the preferred method
# Drop it like it's hot
data = data.dropna()
# Fill it up!
data["total_bedrooms"].fillna(data["total_bedrooms"].mean(), inplace=True)

# Identify categorical features
categorical_features = data.select_dtypes(include=["object"]).columns
print(categorical_features)

# TODO: Choose your poison for handling categorical values
# Encode the categorical features using one-hot encoding or label encoding
data = pd.get_dummies(data, columns=categorical_features)

"""
label_encoder = LabelEncoder()

for feature in categorical_features:
    data[feature] = label_encoder.fit_transform(data[feature])
"""
print(data)

# Determine the target feature and separate it from the dataset
target = "median_house_value"
X = data.drop(target, axis=1)
y = data[target]

# Normalize the numerical features
# TODO: Choose your poison for feature scaling or not to scale it at all
scaler = StandardScaler()
# scaler = MinMaxScaler()
# scaler = MaxAbsScaler()

X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Implement simple regression
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the target feature
predictions = model.predict(X_test)

# Print the predictions and the actual values
print(predictions)
print(y_test)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)
print(accuracy)
