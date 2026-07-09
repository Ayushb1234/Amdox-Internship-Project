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
# Phase 4: Customer Segmentation

``` Goal

Customer ID

↓

Recency

↓

Frequency

↓

Monetary

↓

R Score

↓

F Score

↓

M Score

↓

RFM Score

↓

Segment

```

# Dashboard Will Display:

```
Champions

Loyal Customers

Potential Loyalists

Need Attention

At Risk

Lost Customers

```
# Output File:

```
outputs/

      segmentation/

            rfm_segmentation.csv
```

# Phase 5: Demand Forcasting

```
src/
│
├── forecasting/
│      ├── prepare_dataset.py
│      ├── feature_builder.py
│      ├── train_model.py
│      ├── evaluate.py
│      └── predict.py

```
# Outputs:

```
outputs/
│
├── forecasting/
│      ├── datasets/
│      ├── models/
│      ├── metrics/
│      └── plots/

```

# Demand Forcasting Dataset

```
outputs/

forecasting/

datasets/

daily_sales.csv
```

This daily dataset will also be reused later for:

1. Executive dashboard KPIs
2. Trend analysis
3. Demand forecasting
4. Inventory optimization

``` We are going to create

Lag Features
Revenue Yesterday

Revenue 7 Days Ago

Revenue 30 Days Ago
```

```Rolling Features
7-day Average

14-day Average

30-day Average

7-day Standard Deviation

30-day Standard Deviation
```

``` Growth Features

Revenue Change %

Week-over-Week Growth

Month-over-Month Growth
```

``` Calendar Features

Weekend

Quarter

Month

Week

Day

DayOfWeek

```
# Expected Output

```
Loading Daily Dataset

(604, ...)

Creating Lag Features

Creating Rolling Features

Creating Growth Features

Removing Initial NaNs

(574, ...)

```

# Outputs

```
outputs/

forecasting/

datasets/

forecast_features.csv

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
