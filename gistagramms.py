import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv("RGR1_A-10_X1-X4.csv")


def mean_manual(data):
    s = 0
    for x in data:
        s += x
    return s / len(data)


def variance_manual(data, mean):
    s = 0
    for x in data:
        s += (x - mean) ** 2
    return s / (len(data) - 1)


def std_manual(var):
    return math.sqrt(var)


def median_manual(data):
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 1:
        return data_sorted[n // 2]
    else:
        return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2


def skewness_manual(data, mean, std):
    n = len(data)
    s = 0
    for x in data:
        s += (x - mean) ** 3
    return (s / n) / (std ** 3)


def kurtosis_manual(data, mean, std):
    n = len(data)
    s = 0
    for x in data:
        s += (x - mean) ** 4
    return (s / n) / (std ** 4) - 3

# используется чтобы устанавливать фиксированное кол-во столбцов,у меня при методе стерджесса
# bins_count = 9
fig, axes = plt.subplots(2, 2, figsize=(16, 9))
axes = axes.ravel()
for i, col in enumerate(df.columns):
    data = df[col].dropna().tolist()
    n = len(data)
    mean_val = mean_manual(data)
    var_val = variance_manual(data, mean_val)
    std_val = std_manual(var_val)
    median_val = median_manual(data)
    skew_val = skewness_manual(data, mean_val, std_val)
    kurt_val = kurtosis_manual(data, mean_val, std_val)

    # использовать чтобы рассчитывать количества столбцов по Фридману
    iqr = np.percentile(data, 75) - np.percentile(data, 25)
    h = 2 * iqr / (n ** (1 / 3))
    bins_count = math.ceil((max(data) - min(data)) / h) if h > 0 else 10

    ax = axes[i]
    ax.hist(data, bins=bins_count, edgecolor='black')
    ax.axvline(mean_val, linestyle='--', linewidth=2, label="Среднее")
    ax.axvline(median_val, linestyle='-.', linewidth=2, label="Медиана")
    ax.axvspan(mean_val - std_val, mean_val + std_val, alpha=0.2, label="x̄ ± σ")
    legend_text = (
        f"Выборка объе ма n = {n}\n"
        f"Среднее: {mean_val:.2f}\n"
        f"Медиана: {median_val:.2f}\n"
        f"Дисперсия: {var_val:.2f}\n"
        f"Ст. откл.: {std_val:.2f}\n"
        f"Асимметрия: {skew_val:.2f}\n"
        f"Эксцесс: {kurt_val:.2f}"
    )
    ax.plot([], [], ' ', label=legend_text)
    ax.set_title(f"Гистограмма {col}")
    ax.set_xlabel("Значение")
    ax.set_ylabel("Частота")
    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.02, 0.5),
        fontsize=9,
        frameon=True
    )
plt.tight_layout(rect=[0, 0, 0.82, 1])
plt.show()


