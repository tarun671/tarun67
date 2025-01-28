import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "customer_id": [1, 2, 3, 4],
    "gender": ["male", "female", "male", "female"],
    "city": ["hyderabad", "pune", "bangalore", "shimla"],
    "fruits": ["Apple", "orange", "kiwi", "banana"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city", "fruits"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
print("\nOne-hot encoded DataFrame with sklearn:")
print(encoded_df)


}


@2
label_encounter = label_encounter()
df['ranks'] = label_encoder.fit_transform(df['ranks'])
df['fruits'] = label_encoder.fit_transform(df['fruits'])
print("\ndataframe after label encoding:")
print(df)