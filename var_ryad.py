import pandas as pd

# загрузка файла
df = pd.read_csv("RGR1_A-10_X1-X4.csv")

# вариационные ряды
X1_sorted = df["X1"].sort_values()
X2_sorted = df["X2"].sort_values()
X3_sorted = df["X3"].sort_values()
X4_sorted = df["X4"].sort_values()

for col in ["X1", "X2", "X3", "X4"]:
    print(col)
    print("min =", df[col].min())
    print("max =", df[col].max())
    print()