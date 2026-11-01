#
#
#

import pandas as pd

products = pd.DataFrame({
    "item": ["Pen", "Notebook", "Pencil", "Eraser", "Ruler", "Marker", "Sharpener", "Stapler"],
    "category": ["Stationery", "Stationery", "Stationery", "Stationery", "Tools", "Stationery", "Tools", "Tools"],
    "price": [12, 45, 8, 5, 30, 25, 15, None],
    "stock": [120, 60, 200, 150, 40, 80, 90, 25]
})

# print the Shape and info

print(products)
print(products.shape)
products.info()

# Print the missing value in price column
# Fill the value then convert to int and print

products["price"] = products["price"].fillna(20).astype(int)
print(products["price"].tolist())

# print the items in Stationery category with price less than 30 and stock above 100
# display the item and stock columns using masking

mask = (products["category"] == "Stationery") & (products["price"] < 30) & (products["stock"] > 100)
print(products.loc[mask, ["item", "stock"]])

# display the sum, mean and count of stock grouped by category

cat_stats = products.groupby("category")["stock"].agg(["sum", "mean", "count"]).reset_index()
print(cat_stats)

# Print the single category with the lowest total stock using cat_stats
#idxmin is used to display the lowest/ minimum total stock
low_cat = cat_stats.loc[cat_stats["sum"].idxmin()]
print(low_cat["category"], low_cat["sum"])

# Add a new column "value" = price * stock and print the top 2 items by value

products["value"] = products["price"] * products["stock"]
print(products.sort_values("value", ascending=False).head(2)[["item", "value"]])
