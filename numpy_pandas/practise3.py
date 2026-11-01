import numpy as np
import pandas as pd

country = ["Ireland", "Germany", "England", "France", "India"]
series = pd.Series(country)

print(series)          # prints the full Series with index
print(series.dtype)    # prints the data type
print(series.size)
print(series.loc[1])


import numpy as np
import pandas as pd

data_i = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data_i, index = ["day1", "day2", "day3"])

print(df)
#print(df.loc[2])
print(df.loc["day3"])


import numpy as np

scores = np.array([78, 67, 99, 87, 56, 93])

print(scores > 75)
print((scores > 75).dtype)

print(scores + 5)
print(scores)
print(scores * 2)
print(scores / 100)
print(scores // 10)



# Boolean Masking in numpy
import numpy as np

temperatures = np.array([28, 30, 31, 27, 29, 35])
mask = temperatures > 29
print(temperatures[mask])                # [30 31 35]
print(temperatures[temperatures > 29])


#broadcasting

import numpy as np

sales = np.array([[100, 200, 300], [120, 230, 350]])

monthly_bonus = np.array([10, 20, 30])

total_sales = sales + monthly_bonus
print(total_sales)
print(sales.shape, monthly_bonus.shape)
print(sales.sum(axis=0))
print(sales.sum(axis=1))
print(sales.mean(axis=1))