import pandas as pd


ISSUE_TYPE = "drift"
#  ISSUE_TYPE :
# "negative_sales"
# "missing_values"
# "invalid_discount"
# "drift"


df = pd.read_csv("data/baseline.csv")

if ISSUE_TYPE == "negative_sales":
    df.loc[:10, "Sales"] = -500
    output_file = "data/negative_sales.csv"

elif ISSUE_TYPE == "missing_values":
    n = int(len(df) * 0.3)
    df.loc[:n, "Sales"] = None
    output_file = "data/missing_values.csv"

elif ISSUE_TYPE == "invalid_discount":
    df.loc[:10, "Discount"] = 1.5
    output_file = "data/invalid_discount.csv"

elif ISSUE_TYPE == "drift":
    df["Sales"] = df["Sales"] * 3
    output_file = "data/drift.csv"

else:
    print("Invalid ISSUE_TYPE")
    exit()

df.to_csv(output_file, index=False)

print(f"{ISSUE_TYPE} file created successfully.")