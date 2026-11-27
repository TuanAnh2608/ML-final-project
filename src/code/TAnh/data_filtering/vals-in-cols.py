import pandas as pd

df = pd.read_csv("src/datasets/results.csv", low_memory=False)


# print("Country")
# countries = df["Country"].value_counts().to_dict()
# print(countries)

print("-" * 50)
print("WorkExp")
work_exp = df["WorkExp"].value_counts().to_dict()
print(work_exp)


print("-" * 50)
ai_select = df["AISelect"].value_counts().to_dict()
print(ai_select)

print("-" * 50)
ai_agent = df["AIAgents"].value_counts().to_dict()
print(ai_agent)
