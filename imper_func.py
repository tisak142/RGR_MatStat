import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("RGR1_A-10_X1-X4.csv")

for col in ["X1", "X2", "X3", "X4"]:
    x = np.sort(df[col].values)
    n = len(x)
    y = np.arange(1, n + 1) / n

    plt.figure(figsize=(7, 4))
    plt.step(x, y, where='post')
    plt.xlabel("x")
    plt.ylabel("Fn(x)")
    plt.title(f"Эмпирическая функция распределения для {col}")
    plt.grid(True, alpha=0.3)
    plt.show()