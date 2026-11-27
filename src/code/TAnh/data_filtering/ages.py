import pandas as pd

df = pd.read_csv("./src/datasets/results.csv")

age = df["Age"]
age_unique = age.dropna().value_counts()
print("Unique ages:", age_unique)

edlevel = df["EdLevel"]
edlevel_unique = edlevel.dropna().value_counts()
print("Unique education levels:", edlevel_unique)

workexp = df["WorkExp"]
workexp_unique = workexp.dropna().value_counts()
print("Unique work experience:", workexp_unique)

devtype = df["DevType"]
devtype_unique = devtype.dropna().value_counts()
print("Unique developer types:", devtype_unique)

comptotal = df["CompTotal"]
comptotal_unique = comptotal.dropna().value_counts().sort_index(ascending=False)
print("Unique compensation totals:", comptotal_unique)
