#
#
#

import pandas as pd

emp = pd.DataFrame({
    "name": ["Anil", "Bela", "Chand", "Dipa", "Eshan", "Fiza", "Gopal", "Hema"],
    "dept": ["Sales", "Tech", "Sales", "HR", "Tech", "Tech", "HR", "Sales"],
    "salary": [52, 88, 61, 47, 95, 79, 50, 58],
    "rating": [4, 5, 3, 4, 4, 5, None, 2]
})

#print the Shape and info

print(emp)
print(emp.shape)
emp.info()

#Print the missing value in rating column
# Fill the value then convert to int and print 

emp["rating"] = emp["rating"].fillna(3).astype(int)
print(emp["rating"].tolist())

# print the employees who work in Tech or sales and earn more than 55 and 
# display the name and salary columns
# using masking here.

mask = emp["dept"].isin(["Tech", "Sales"]) & (emp["salary"]> 55)
print(emp.loc[mask, ["name", "salary"]])

# display the sum, mean and count of the dept salary

dept_stats = emp.groupby("dept")["salary"].agg(["sum", "mean", "count"]).reset_index()
print(dept_stats)

#Print the single department with the highest average salary using dept_stats

top_dept = dept_stats.loc[dept_stats["mean"].idxmax()]

print("*******************************")
print(top_dept["dept"], top_dept["mean"])



