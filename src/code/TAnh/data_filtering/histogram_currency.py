import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("src/datasets/results.csv", low_memory=False)

col = "ConvertedCompYearly"
d = df[
    df[col].notna()
    & (df[col] > 0)
    & (df["MainBranch"] == "I am a developer by profession")
    & (df["Employment"] == "Employed")
].copy()
d["usd"] = d[col]

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].hist(d["usd"], bins=100)
ax[0, 0].set_title("usd (gốc)")

ax[0, 1].hist(np.log10(d["usd"]), bins=100)
ax[0, 1].set_title("log10(usd)")

ax[1, 0].boxplot(np.log10(d["usd"]), vert=False)
ax[1, 0].set_title("Boxplot log10(usd)")

ax[1, 1].hist(d.loc[d["usd"] < 5000, "usd"], bins=50)
ax[1, 1].set_title("usd < 5.000 (đuôi dưới)")

plt.tight_layout()
plt.show()


hi = d[d["usd"] > 1_000_000]
print(len(hi))
print(
    hi[["usd", "CompTotal", "Currency", "Country", "WorkExp", "DevType", "OrgSize"]]
    .sort_values("usd", ascending=False)
    .head(30)
    .to_string()
)
