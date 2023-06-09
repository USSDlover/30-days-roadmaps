import pandas as pd

data = pd.read_csv("sales.csv")
print(data.groupby("Region")["Revenue"].max())
