import math

import pandas as pd

labels = ["Low", "Medium", "High"]

df = pd.read_csv("src/datasets/results.csv", low_memory=False)

salary = df["ConvertedCompYearly"].copy().dropna()
salary = salary[(salary > 1000) & (salary < 2000000)]

salary = salary.sort_values()
n = salary.shape[0]

print(f"n: {n}")

t1 = (n - 1) / 3
t2 = (n - 1) * 2 / 3
t3 = n

print(f"t1: {t1}, t2: {t2}, t3: {t3}")

low = salary.iloc[: math.ceil(t1)]
medium = salary.iloc[math.ceil(t1) : math.ceil(t2)]
high = salary.iloc[math.ceil(t2) : math.ceil(t3)]

print(f"Low: {len(low)}, Medium: {len(medium)}, High: {len(high)}")

value1 = (salary.iloc[math.floor(t1)] + salary.iloc[math.ceil(t1)]) / 2
value2 = (salary.iloc[math.floor(t2)] + salary.iloc[math.ceil(t2)]) / 2

print(f"Value1: {value1}, Value2: {value2}")

# Use built in function
tertile_groups, bins = pd.qcut(salary, q=3, labels=labels, retbins=True)
print(tertile_groups.value_counts())
print(f"Value1 (33.3%): {bins[1]:.2f}, Value2 (66.7%): {bins[2]:.2f}")


# check salary
s1 = salary[((salary - 54527.0) < 1e-6) & ((salary - 54527.0) > -1e-6)]
print(s1)

s2 = salary[((salary - 104413.0) < 1e-6) & ((salary - 104413.0) > -1e-6)]
print(s2)
