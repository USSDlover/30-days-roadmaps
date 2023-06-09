import pandas as pd

data = pd.read_csv("orders.csv")


def identify_bad_data():
    bad_rows = data[data.isnull().any(axis=1)]
    print(bad_rows)
    # Fill the data backward
    print(bad_rows.fillna(method="bfill"))


def cleanup_bad_rows():
    cleaned_data = data.dropna()
    print(cleaned_data)


def total_revenue_by_customer():
    data["revenue"] = data["quantity"] * data["price"]
    revenue_per_customer = data.groupby("customer_id")["revenue"].describe()
    print(revenue_per_customer)


total_revenue_by_customer()
