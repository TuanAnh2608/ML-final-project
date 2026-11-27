"""
1. Xóa NaN cột ConvertedCompYearly
2. Lọc MainBranch = "I am a developer by profession" - Xóa cột MainBranch
3. Lọc Employment = "Employed" - Xóa cột Employment
4. Xóa 2 cột CompTotal và Currency do đã có ConvertedCompYearly
"""

import pandas as pd

df = pd.read_csv("./src/datasets/filtered_data.csv", low_memory=False)

# Remove rows with NaN in ConvertedCompYearly
df = df[df["ConvertedCompYearly"].notna()]
print(
    f"Sau khi lọc NaN tại cột ConvertedCompYearly: {df.shape[0]} hàng x {df.shape[1]} cột"
)
print("\n\n", "-" * 50, "\n\n")

# Keep only Dev
df = df[df["MainBranch"] == "I am a developer by profession"]
print(f"Sau khi lọc Dev trong cột MainBranch: {df.shape[0]} hàng x {df.shape[1]} cột")

# Remove MainBranch cols
print("Xoá cột MainBranch")
df = df.drop(columns=["MainBranch"])

print("\n\n", "-" * 50, "\n\n")

# Filter Employed in Employment
print("Lọc Employed trong cột Employment")
print("Các giá trị trong Employment: ")
print(df["Employment"].value_counts())
df = df[df["Employment"] == "Employed"].copy()
print("Xóa cột Employment")
df = df.drop(columns=["Employment"])


print(
    f"Sau khi lọc Employed trong cột Employment: {df.shape[0]} hàng x {df.shape[1]} cột"
)

print("\n\n", "-" * 50, "\n\n")

print("Các cột còn lại: ", df.columns.tolist())

print("\n\n", "-" * 50, "\n\n")

print("Xóa 2 cột CompTotal và Currency do đã có ConvertedCompYearly")
df = df.drop(columns=["CompTotal", "Currency"])
print("Kích thước sau khi xóa 2 cột: ", df.shape)

print("\n\n", "-" * 50, "\n\n")

# Lưu dữ liệu đã lọc vào filtered_data.csv
df.to_csv("./src/datasets/filtered_data.csv", index=False)


assert df.shape[1] == 24, df.shape
assert df["ConvertedCompYearly"].notna().all()
