import pandas as pd

df = pd.read_csv("./src/datasets/filtered_data.csv", low_memory=False)

values = df["Country"].value_counts().to_dict()

print(values)

print("-" * 50)

country = "Viet Nam"
data = df[df["Country"] == country]
print(data)
