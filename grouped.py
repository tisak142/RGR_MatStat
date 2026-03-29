import pandas as pd
import numpy as np
import math

df = pd.read_csv("RGR1_A-10_X1-X4.csv")

def fd_bins(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    h = 2 * iqr / (len(data) ** (1/3))
    return math.ceil((data.max() - data.min()) / h) if h > 0 else 10

for col in ["X1", "X2", "X3"]:
    data = df[col].dropna().values

    k = fd_bins(data)   # число интервалов
    counts, edges = np.histogram(data, bins=k)
    mids = (edges[:-1] + edges[1:]) / 2

    grouped_df = pd.DataFrame({
        "Левая граница": edges[:-1],
        "Правая граница": edges[1:],
        "Середина интервала": mids,
        "Частота": counts
    })

    grouped_df["Интервал"] = grouped_df.apply(
        lambda row: f"[{row['Левая граница']:.2f}; {row['Правая граница']:.2f})",
        axis=1
    )

    grouped_df = grouped_df[["Интервал", "Середина интервала", "Частота"]]

    n = len(data)
    mean_grouped = np.sum(grouped_df["Середина интервала"] * grouped_df["Частота"]) / n
    var_grouped = np.sum(
        grouped_df["Частота"] * (grouped_df["Середина интервала"] - mean_grouped) ** 2
    ) / n

    print(f"\n{col}")
    print(grouped_df)
    print(f"Среднее по сгруппированной выборке: {mean_grouped:.4f}")
    print(f"Дисперсия по сгруппированной выборке: {var_grouped:.4f}")

    grouped_df.to_csv(f"grouped_{col}.csv", index=False, encoding="utf-8-sig")