import pandas as pd
import numpy as np

products = pd.DataFrame({
    "product": ["Desk Lamp", None, "Notebook", "Kettle", "Mug", "Stapler", "Toaster"],
    "category": ["Home", "Office", "Office", "Kitchen", "Kitchen", "Office", "Kitchen"],
    "price": [40.0, 25.0, np.nan, 30.0, np.nan, 15.0, 50.0],
})

def fill_gaps(df):
    filled = df.copy()
    filled["price"] = filled["price"].fillna(filled["price"].mean())
    filled["product"] = filled["product"].fillna("Unknown")
    return filled

if __name__ == "__main__":
    print(products.isnull().sum())
    print("Missing before:", products.isnull().sum().sum())
    result = fill_gaps(products)
    if result is not None:
        print("Missing after:", result.isnull().sum().sum())
        print("Rows before:", len(products), "| Rows after:", len(result))
        print(result)
