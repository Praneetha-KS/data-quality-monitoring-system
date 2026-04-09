import pandas as pd
import json

df = pd.read_csv("data/baseline.csv")

stats = {
    "sales_mean": float(df["Sales"].mean()),
    "profit_mean": float(df["Profit"].mean())
}

with open("baseline_stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print("Baseline stats created successfully.")