import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

# Load your data
df = pd.read_csv('data.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df['numeric_column'] = imputer.fit_transform(df[['numeric_column']])

# Encode categorical variables
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[['categorical_column']]).toarray()
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['categorical_column']))

# Normalize and standardize numerical features
scaler = StandardScaler()
df['standardized_column'] = scaler.fit_transform(df[['numeric_column']])
