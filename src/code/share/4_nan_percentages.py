"""
Tính phần trăm giá trị NaN trong từng cột của trong data.
KL: Cột có tỷ lệ NaN cao nhất: AIModelsHaveWorkedWith - 48.65%. Không cần phải bỏ cột nào nữa.

1. Điền "" vào các cột multi-hot có NaN
2. Điền 0 vào WorkExp nếu Age = "18-24 years old"
3. Điền "Unknown" vào AISelect và AIAgents nếu có NaN
4. Các cột còn lại có NaN xử lý sau train/test.
"""

import pandas as pd

df = pd.read_csv("./src/datasets/filtered_data.csv", low_memory=False)

N = df.shape[0]
nan_counts = df.isna().sum()
print("Số lượng mẫu: ", N)
print("Số lượng giá trị NaN trong từng cột: \n", nan_counts)

print("-" * 50)

# Tính phần trăm
nan_percentages = (nan_counts / N) * 100
print("Phần trăm giá trị NaN trong từng cột: \n", nan_percentages)

print("-" * 50)

print(df.columns.tolist())

print("-" * 50)

# Fill na thành "" tại các cột multi-hot
print("Xử lý Na cho các cột multi-hot")
cols = [
    "LanguageHaveWorkedWith",
    "DatabaseHaveWorkedWith",
    "PlatformHaveWorkedWith",
    "WebframeHaveWorkedWith",
    "DevEnvsHaveWorkedWith",
    "OpSysPersonal use",
    "OpSysProfessional use",
    "OfficeStackAsyncHaveWorkedWith",
    "AIModelsHaveWorkedWith",
]
for col in cols:
    df[col] = df[col].fillna("")

print(df.isna().sum())

print("-" * 50)

print("Xử lý Na cho cột số WorkExp")
print("Thống kê các dòng có WorkExp là NaN")
print(df[df["WorkExp"].isna()][["Age", "YearsCode"]].describe(include="all"))
print()
print(
    "Số lượng dòng có WorkExp và YearsCode đều là NaN: ",
    df[df["WorkExp"].isna() & df["YearsCode"].isna()].shape[0],
)

df.loc[(df["WorkExp"].isna()) & (df["Age"] == "18-24 years old"), "WorkExp"] = 0
remove = df["WorkExp"].isna()

df = df[~remove].copy()
print("Thống kê sau khi xử lý Na tại WorkExp")
print(df.isna().sum())

print("-" * 50)

print("Xử lý Na cho cột AISelect và AIAgents bằng cách thay Na thành 'Unknown'")
df["AISelect"] = df["AISelect"].fillna("Unknown")
df["AIAgents"] = df["AIAgents"].fillna("Unknown")
print(df.isna().sum())

print("-" * 50)

print("Kết thúc bước lọc Na thứ 2.")
print("Kích thước tập dữ liệu còn lại: ", df.shape)

df.to_csv("./src/datasets/filtered_data.csv", index=False)
