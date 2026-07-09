# Amdox-Internship-Project
This is the Amodx Internship project Repo about retail AI intelligence system Buidling.

# Phase 1: Project Setup

Structure of Project Repo:

```
NeuralRetail/
│
├── data/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── reports/
│
├── dashboard/
│
├── outputs/
│
├── requirements.txt
│
└── README.md

```
# Required Libraries
```
pandas
numpy
matplotlib
plotly
seaborn
scikit-learn
streamlit
jupyter
openpyxl
joblib
scipy
```
PHase 1: Project setup and Data Preprocessing

# Phase 2 : Data Cleaning and EDA done in Notebooks

```
outputs/
    eda/
        monthly_sales.png
        top_products.png
        top_countries.png
        weekday_sales.png
        hourly_sales.png
```
Outputs be Like:

```
Total Transactions :
Total Customers :
Total Products :
Countries :
Revenue :
Units Sold :

```

# Phase 3 : Starts Here

Feature Engineering has been done in Notebooks.

# Feature Engineering


```
Forecasting
      ↑
Inventory
      ↑
Customer Segmentation
      ↑
Dashboard
      ↑
Feature Engineering

```
# Feature Engineering Architecture

```

Raw Sales
      │
      ▼
Time Features
      │
      ▼
Customer Features
      │
      ▼
Product Features
      │
      ▼
Country Features
      │
      ▼
Machine Learning Dataset

```

# Results:

```
outputs/
      features/
            customer_features.csv
            product_features.csv
            country_features.csv
            master_feature_dataset.csv
```

# Inventory Optimization Engine

```

Sales Data
      │
      ▼
Product Statistics
      │
      ▼
ABC Analysis
      │
      ▼
XYZ Analysis
      │
      ▼
Safety Stock
      │
      ▼
Reorder Point
      │
      ▼
Stockout Risk
      │
      ▼
Inventory Dashboard

```

# What is ABC Analysis?

```
ABC Analysis classifies products based on Revenue Contribution.

A Items → Top 80% Revenue
B Items → Next 15% Revenue
C Items → Last 5% Revenue

```

# Module 9 — AI Recommendation Engine

This is the module that makes interviewers say:

"This isn't just analytics, this actually recommends products."

We'll implement Market Basket Analysis using the Apriori Algorithm.

What we'll build

```
Customer Transactions
            │
            ▼
Transaction Matrix
            │
            ▼
Apriori Algorithm
            │
            ▼
Association Rules
            │
            ▼
Frequently Bought Together
            │
            ▼
Recommendation Engine
```
