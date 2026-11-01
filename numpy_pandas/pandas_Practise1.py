

import pandas as pd

catalogue = pd.DataFrame({
    "product_code": ["P101", "P102", "P103", "P104", "P105"],
    "category": ["Kitchen", "Garden", "Kitchen", "Office", "Garden"],
    "price": [450, 1200, 300, 850, 640],
    "stock": [12, 5, 40, 0, 18],
})

by_code = catalogue.set_index("product_code")

print(catalogue)

print(by_code.shape)
print(by_code.loc["P103", "price"])
print(by_code.iloc[0:2, 0:2])
print(by_code.loc["P102":"P104", ["price", "stock"]])

