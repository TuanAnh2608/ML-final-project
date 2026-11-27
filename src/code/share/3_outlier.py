"""
1. Giới hạn lương từ 3.000 đến 1.000.000
2. Lọc các dòng 'Prefer not to say' trong Age
3. Lọc outlier cho cột WorkExp theo Age
4. Lọc outlier cho cột YearsCode theo Age
5. Clip số lượng tool đã dùng xuống còn max 50
"""

import pandas as pd

df = pd.read_csv("./src/datasets/filtered_data.csv", low_memory=False)

bottom = 3000
top = 1000000

print("Lọc lương dưới 3.000 và trên 1.000.000")
print("Kích thước trước khi lọc: ", df.shape)
df = df[df["ConvertedCompYearly"].between(bottom, top)]
# print(
#     "Các giá trị trong ConvertedCompYearly sau khi lọc: ",
#     df["ConvertedCompYearly"].value_counts().sort_index(),
# )
print("Kích thước sau khi lọc: ", df.shape)

print("-" * 50)

print("Lọc các dòng 'Prefer not to say' trong Age")
df = df[df["Age"] != "Prefer not to say"]
print("Kích thước sau khi lọc: ", df.shape)

print("-" * 50)

print("Lọc outlier cho cột WorkExp")
max_exp = {
    "18-24 years old": 8,
    "25-34 years old": 20,
    "35-44 years old": 30,
    "45-54 years old": 40,
    "55-64 years old": 50,
    "65 years or older": 55,
}

limit = df["Age"].map(max_exp)
outlier_exp = df["WorkExp"] > limit
# print("Các giá trị không hợp lệ trong WorkExp: \n", df[outlier_exp][["Age", "WorkExp"]])
print("Số lượng outlier: ", outlier_exp.sum())
print("Xóa các outlier trong WorkExp")
df = df[~outlier_exp]
print("Kích thước sau khi lọc: ", df.shape)

print("-" * 50)

print("Lọc outlier cho YearsCode")
# print(df["YearsCode"])
max_code = {
    "18-24 years old": 14,
    "25-34 years old": 24,
    "35-44 years old": 34,
    "45-54 years old": 44,
    "55-64 years old": 54,
    "65 years or older": 60,
}
limit = df["Age"].map(max_code)
outlier_code = df["YearsCode"] > limit
print("Số lượng outlier: ", outlier_code.sum())
print("Xóa các outlier trong YearsCode")
df = df[~outlier_code].copy()
print("Kích thước sau khi lọc: ", df.shape)

print("-" * 50)
# print(df.columns.tolist())
print("Clip số lượng tool đã dùng xuống còn max 50")
df["ToolCountWork"] = df["ToolCountWork"].clip(upper=50)
print("Kích thước sau khi clip: ", df.shape)

print("-" * 50)
df.to_csv("./src/datasets/filtered_data.csv", index=False)
