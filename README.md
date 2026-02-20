# amazon-sales-data-analysis

Project Overview

This project performs an exploratory data analysis (EDA) on an Amazon sales dataset to uncover insights related to revenue, profit, customer behavior, product performance, regional trends, and delivery status. The analysis simulates a real-world business scenario, where raw transactional data is cleaned, engineered, analyzed, and visualized to support data-driven decisions.

# Objectives

- Understand overall sales performance

- Analyze revenue and profit trends

- Identify top-selling products and categories

- Explore country and state-wise order distribution

- Validate tax consistency and delivery outcomes

- Visualize key business metrics clearly

# Tools & Libraries Used

* Python

* Pandas – data manipulation and analysis

* NumPy – numerical operations

* Matplotlib – data visualization

# Dataset

Source: Amazon sales dataset (CSV format)

Key Columns:

OrderDate

ProductName, Category, Brand

Quantity, UnitPrice, Discount

ShippingCost, Tax, TotalAmount

Country, State

PaymentMethod, OrderStatus

# Data Preparation & Feature Engineering

The following steps were applied to prepare the dataset:

- Converted OrderDate to datetime format

- Extracted Year and Month from order dates

- Expanded U.S. state abbreviations to full names

- Handled inconsistent state values for non-U.S./Australia countries

- Verified missing and negative values

- Created derived metrics for revenue, cost, and profit

# Profit in this project is calculated as:
Revenue − Shipping Cost
(Other costs such as product cost are not available in the dataset.)

# Analysis Performed

1. Revenue & Profit Analysis

- Total revenue and operational profit

- Category-wise revenue and profit

- Monthly revenue and shipping cost trends

2. Product & Category Insights

- Total unique products and categories

- Top 10 most sold products

- Best-performing category by quantity

- Electronics category deep dive

- Top brands and smartwatch analysis

3. Country & Regional Analysis

- Country-wise order distribution

- Category preference by country

- Product popularity in the U.S.

- State-wise order analysis for the U.S.

4. Delivery, Tax & Payment Analysis

- Order status distribution

- Tax consistency check

- Most used payment methods

- Quantity validity checks

# Visualizations Included

The project contains 5 focused and business-relevant visualizations, including:

- Monthly revenue trend (line chart)

- Top Category and Top brand in Electronics Category
 
- Most used payment method

- Country-wise order distribution

- U.S. state-wise order volume

Each visualization supports a specific business question and avoids unnecessary clutter.

# Key Insights

- Electronics generate the highest revenue

- The U.S. contributes the majority of total orders

- Texas leads U.S. state-wise order volume

- Credit cards are the most used payment method

- No major tax inconsistencies detected

- Shipping cost significantly impacts operational profit

# Conclusion

This project demonstrates a complete data analysis workflow, from raw data cleaning to insight generation and visualization.
It reflects realistic analytical thinking, business awareness, and attention to data quality.

# Future Improvements

- Incorporate product cost for accurate net profit calculation

- Add dashboard-style visualizations

- Perform time-series forecasting

- Enhance geographic analysis with maps

# Author

Emon Sen
B.Sc. Engineering (CSE)
Aspiring Data Analyst 
