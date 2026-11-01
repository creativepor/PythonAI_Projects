#
#
#
import pandas as pd

sales = pd.DataFrame({
    'order_id': [201, 202, 203, 204, 205, 206, 207],
    'region': ['North', 'South', 'North', 'East', 'South', 'North', 'East'],
    'amount': [300, 150, 500, 220, 250, 100, 380]
})

print(sales)

def summarize_regions(df):
    # TODO: group by region, aggregate amount with sum and mean,
    # reset the index, then sort by sum (highest first)

    sales_stats = df.groupby("region")["amount"].agg(["sum", "mean"]).reset_index()
    sales_stats = sales_stats.sort_values(by= 'sum', ascending=False)
    return sales_stats
    #pass

print(summarize_regions(sales))
