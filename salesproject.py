import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Student_data.csv")
print(data.head())

print(data.info())

print(data.describe())

print(data["Revenue"].sum())

print(data.groupby("City")["Revenue"].sum())

print(data.groupby("Category")["Revenue"].sum())

city_data=data.groupby("City")["Revenue"].sum()

city_data.plot(kind="bar")
plt.title("Revenue by City")        
plt.xlabel("City")
plt.ylabel("Revenue")
plt.show()

cat_data = data.groupby("Category")["Revenue"].sum()

cat_data.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()

cat_data = data.groupby("Category")["Revenue"].sum()

cat_data.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()

cust_data = data.groupby("Customer")["Revenue"].sum()

cust_data.plot(kind="bar")
plt.title("Revenue by Customer")

plt.show()