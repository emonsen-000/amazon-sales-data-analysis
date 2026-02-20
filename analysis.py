import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Amazon.csv")

### DATA PREPARATION & FEATURED ENGINEERING

# Change OrderDate to datetime
print("Data type before changing to datetime:",df["OrderDate"].dtype)      
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
print("\nData type after changing to datetime:",df["OrderDate"].dtype)   

# changing the state name form
state_map = {
    "TX": "Texas",
    "CA": "California",
    "NC": "North Carolina",
    "FL": "Florida",
    "WA": "Washington",
    "OH": "Ohio",
    "DC": "District of Columbia",
    "IL": "Illinois",
    "PA": "Pennsylvania",
    "CO": "Colorado",
    "IN": "Indiana",
    "NY": "New York",
    "AZ": "Arizona"
}
df["State"]=df["State"].replace(state_map)
print("\nafter changing state name:\n",df["State"])

# adding year and month column

df["Year"]=df["OrderDate"].dt.year
df["Month"]=df["OrderDate"].dt.month

# REVENUE & PROFIT
revenue=df["TotalAmount"].sum()
print("\nTotal Revenue:\n",revenue)

total_shipping_cost=df["ShippingCost"].sum()
profit=revenue-total_shipping_cost
print("\nTotal PROFIT:\n",profit)

# REVENUE & PROFIT (CATEGORY WISE)
rev_cat_wise=df.groupby("Category")["TotalAmount"].sum()
print("\nCategory wise Revenue:\n",rev_cat_wise.sort_values(ascending=False))

cost_cat_wise=df.groupby("Category")["ShippingCost"].sum()
print("\nCategory wise Cost:\n",cost_cat_wise.sort_values(ascending=False))

profit_cat_wise=rev_cat_wise-cost_cat_wise
print("\nCategory wise profit:\n",profit_cat_wise.sort_values(ascending=False))

# Monthly Revenue
monthly_revenue=df.groupby("Month")["TotalAmount"].sum()
print("\nMonthly Revenue:\n",monthly_revenue.sort_index())
monthly_cost=df.groupby("Month")["ShippingCost"].sum()
print("\nMonthly Revenue:\n",monthly_cost.sort_index())

# Extracting state names where country is not Australia or U.S.
df.loc[~df["Country"].isin(["Australia","United States"]),"State"]="Not Given"

### PRODUCT & CATEGORY ANALYSIS

# TOTAL TYPE OF PRODUCTS
print("\nTotal type of products:",df["ProductName"].nunique())
# TOTAL TYPE OF CATEGORIES
print("\nTotal type of categories:",df["Category"].nunique())
# TOTAL QUANTITY SOLD
print("\nTotal quantity sold:",df["Quantity"].sum())

# TOP 10 MOST SOLD PRODUCT
most_sold_product=df.groupby("ProductName")["Quantity"].sum()
sorted_products=most_sold_product.sort_values(ascending=False)
print("\nTop 10 Most Sold Product:\n",sorted_products.head(10))

# NO1 CATEGORY (according to how many product sold)
top_category=df.groupby("Category")["Quantity"].sum()
sorted_category=top_category.sort_values(ascending=False)
print("\nNo 1 Category:\n",sorted_category.head(1))

# Electronics category generates the highest revenue, indicating strong demand.

# Top 10 Most Sold Product In Electronics Category
cat_elec=df[df["Category"]=="Electronics"]
most_in_elect=cat_elec.groupby("ProductName")["Quantity"].sum()
print("\nTop 10 Most sold product in Electronics:\n",most_in_elect.sort_values(ascending=False).head(10))

top_brand_in_elect=cat_elec.groupby("Brand")["Quantity"].sum()
print("\nTop 5 Brand in Electronics:\n",top_brand_in_elect.sort_values(ascending=False).head(5))

# UrbanStyle RANKED 1...

# Top Smartwatch Brand
watches=df[df["ProductName"]=="Smartwatch"]
top_smartwatch=watches.groupby("Brand")["Quantity"].sum()
print("\nTop Smartwatch Brand:\n",top_smartwatch.sort_values(ascending=False).head(1))

# HomeEase sold the most smartwatches. They are not in top 5, but people are liking there Smart watches..

### COST, QUANTITY, TAX & DELIVERY ANALYSIS

total_tax=df["Tax"].sum()
print("\nTotal amount of tax:\n",total_tax)

print("\nTotal shipping cost:\n",total_shipping_cost)

# any quantity<=0?
check_nan=df["Quantity"].isnull().sum()
print("No of missing value in quantity:",check_nan)
#negative value
check_neg=df[df["Quantity"]<0]
print("\nNumber of negative values:\n",check_neg)

# how many deliveries are pending, delivered, shipped, canceled, returned
print("\nDelivery Results:\n",df["OrderStatus"].value_counts())

# TAX mismatch?
gross = df["UnitPrice"] * df["Quantity"]
discounted = gross - (gross * df["Discount"])
approx_tax_rate = df["Tax"] / discounted
print("\nCheck for mismatch:\n",approx_tax_rate.describe())          # no mismatch

# which payment method used most
most_used_method=df["PaymentMethod"].value_counts().sort_values(ascending=False)
print("\nMost used payment methods:\n",most_used_method.head(1))   # CREDIT CARDS are most used method by the customers

### Country & Region Insights
top_country=df["Country"].value_counts()
print("\nTop Country:\n",top_country.head(1))

# Orders from U.S. are the most. Almost 5X more than 2nd ranked India.

# Which country bought most Electronics
high_in_elect=df.groupby("Category")["Country"].value_counts()
print("\nEach categories record of orders from countries:\n",high_in_elect)
print("\nOrders from Countries in Electronics Category:\n",high_in_elect["Electronics"])

# U.S. ordered the most electronic products.

# top categories in each country
high_in_cat=df.groupby("Country")["Category"].value_counts()
print("\nTop categories in each country\n",high_in_cat)
print("\nTop categories in U.S.:\n",high_in_cat["United States"])    # Orders on Books are most in U.S.

# top products in each country
high_in_prod=df.groupby("Country")["ProductName"].value_counts()
print("\nTop Products in each country\n",high_in_prod)
print("\nTop Products in U.S.:\n",high_in_prod["United States"].head(10))

# profit & revenue according to countries
rev_country_wise=df.groupby("Country")["TotalAmount"].sum()
print("\nCountry wise Revenue:\n",rev_country_wise.sort_values(ascending=False))

cost_country_wise=df.groupby("Country")["ShippingCost"].sum()
print("\nCountry wise Cost:\n",cost_country_wise.sort_values(ascending=False))

profit_country_wise=rev_country_wise-cost_country_wise
print("\nCountry wise profit:\n",profit_country_wise.sort_values(ascending=False))

# Most order from which state of U.S.
most_order_in_state=df.groupby("Country")["State"].value_counts()
most_order_in_US=most_order_in_state["United States"]
print("\nOrders from states of U.S.:\n",most_order_in_US)      # Orders from Texas are most

# VISUALIZATION

# monthly revenue (Line Chart)

plt.plot(monthly_revenue.index,monthly_revenue.values,color="green",marker="o",label="Monthly Revenue")
plt.title("Monthly Revenue")
plt.xlabel("Month (Jan-Dec)")
plt.xlim(0,13)
plt.ylabel("Revenue (In Millions)")
plt.grid(linestyle="--",color="gray")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()

# payment method (pie)
methods=most_used_method.index
explode=[0.1,0,0,0,0,0]
plt.pie(most_used_method,labels=methods,autopct="%1.1f%%",explode=explode)
plt.title("Most used payment method")
plt.tight_layout()
plt.show()

# orders by country
plt.bar(top_country.index,top_country.values,label="Orders by country",alpha=0.8,color="green")
plt.title("Total Orders from Countries")
plt.xlabel("Countries")
plt.xticks(rotation=45)
plt.ylabel("Order Amount")
plt.grid(linestyle="--",color="gray",alpha=0.3)
plt.legend(loc="upper right")
plt.tight_layout()
for i in range(len(top_country.index)):
    plt.text(i,top_country.values[i],top_country.values[i],ha="center",va="bottom")
plt.show()

# top categories
categories=sorted_category.index
explode=[0.1,0,0,0,0,0]
plt.subplot(1,2,1)
plt.pie(sorted_category,labels=categories,autopct="%1.1f%%",explode=explode)
plt.title("Top Categories")
plt.tight_layout()

# top brands in electronics
brands=top_brand_in_elect.index
plt.subplot(1,2,2)
plt.pie(top_brand_in_elect,labels=brands,autopct="%1.1f%%")
plt.title("Top Brands in Electronics")
plt.show()

# orders in US
plt.barh(most_order_in_US.index,most_order_in_US.values,label="Orders from U.S. states")
plt.title("Orders in U.S")
plt.xlabel("States")
plt.xticks(rotation=45)
plt.ylabel("No of Orders")
plt.grid(linestyle="--",color="gray")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()

print(df.to_csv("New Data after analysis.csv"))