# NeuralRetail AI v2.0

**Enterprise Retail Intelligence Platform**

NeuralRetail AI is an end-to-end retail analytics and machine learning platform built to transform transactional sales data into business decisions. It combines data cleaning, feature engineering, customer intelligence, demand forecasting, inventory optimization, association-rule recommendations, and a multi-page Streamlit dashboard.

---

## ✨ Project Highlights

* **Sales analytics** with revenue trends, top products, and country-wise performance
* **Customer intelligence** with CLV, churn risk, customer tiers, and 360° profiles
* **Demand forecasting** using engineered time-series features and ML models
* **Inventory optimization** with ABC, XYZ, safety stock, reorder point, and priority scoring
* **Recommendation engine** using Apriori and association rules
* **Executive dashboard** built in Streamlit with reusable KPI panels and visual analytics

---

## 🧠 Business Value

NeuralRetail AI helps retail teams answer questions like:

* Which products should be reordered now?
* Which customers are high value or at risk of churn?
* What are the strongest product associations for cross-sell?
* How is revenue trending over time?
* Which forecasting model performs best?

---

## 🏗️ System Architecture

```text
Raw CSV Data
   ↓
Data Cleaning
   ↓
EDA + Business Summary
   ↓
Feature Engineering
   ↓
Customer Segmentation (RFM)
   ↓
Demand Forecasting (XGBoost / Baselines)
   ↓
Inventory Optimization (ABC / XYZ / Reorder Logic)
   ↓
Customer Intelligence (CLV / Churn / Tier)
   ↓
Recommendation Engine (Apriori)
   ↓
KPI Generation
   ↓
Streamlit Dashboard
```

---

## 📁 Project Structure

```text
NeuralRetail/
├── app.py
├── config/
│   ├── paths.py
│   └── settings.py
├── components/
├── css/
├── data/
├── pages/
├── outputs/
├── src/
│   ├── forecasting/
│   ├── inventory/
│   ├── customer/
│   ├── recommendation/
│   └── dashboard/
├── utils/
├── requirements.txt
└── README.md
```

---

## 📊 Modules Implemented

### 1) Data Loading & Cleaning

* Standardized column names
* Parsed date fields
* Removed duplicates
* Handled missing values
* Created total price column
* Split clean sales and customer-ready datasets

### 2) Exploratory Data Analysis

* Total revenue
* Total orders
* Total customers
* Top products
* Top countries
* Weekday and hourly trends

### 3) Feature Engineering

* Time features: year, month, week, day, hour
* Customer features: frequency, monetary value, recency
* Product features: demand, revenue, selling days
* Country features: revenue, orders, customers

### 4) Customer Segmentation

* RFM scoring
* Segment labels such as Champions, Loyal Customers, At Risk, and Lost

### 5) Demand Forecasting

* Daily sales aggregation
* Lag features
* Rolling mean and rolling std features
* Growth features
* Model training with Linear Regression, Random Forest, and XGBoost
* Evaluation using MAE, RMSE, and MAPE

### 6) Inventory Optimization

* Product-level sales statistics
* ABC classification
* XYZ classification
* Inventory classes like AX, AY, CZ
* Safety stock
* Reorder point
* Stockout risk
* Inventory priority

### 7) Customer Intelligence

* Customer lifetime value
* Customer tiers
* Churn risk scoring
* Customer health score
* Customer 360 dataset

### 8) Recommendation Engine

* Market basket analysis using Apriori
* Frequent itemsets
* Association rules
* Product recommendation outputs

### 9) KPI Generator

* Centralized dashboard KPI JSON and CSV
* Used to power the executive dashboard

### 10) Streamlit Dashboard

* Executive overview
* Sales analytics
* Customer intelligence
* Demand forecasting
* Inventory optimization
* Recommendation engine
* Model performance

---

## 📈 Key Outputs

The project generates the following artifacts:

* `outputs/customer/customer_360.csv`
* `outputs/inventory/product_inventory.csv`
* `outputs/forecasting/datasets/daily_sales.csv`
* `outputs/forecasting/datasets/forecast_features.csv`
* `outputs/forecasting/metrics/model_metrics.csv`
* `outputs/recommendation/association_rules.csv`
* `outputs/recommendation/frequent_itemsets.csv`
* `outputs/dashboard/dashboard_kpis.json`
* `outputs/dashboard/dashboard_kpis.csv`

---

## 🛠️ Tech Stack

**Language:** Python 3.11
**Data Processing:** pandas, numpy
**Machine Learning:** scikit-learn, xgboost, mlxtend
**Visualization:** plotly, matplotlib
**Dashboard:** Streamlit
**Utilities:** joblib, scipy, openpyxl

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd NeuralRetail
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit dashboard

```bash
streamlit run app.py
```

---

## ⚙️ How to Rebuild the Pipeline

Run the project modules in this order:

```bash
python src/data_loader.py
python src/data_cleaning.py
python src/eda.py
python src/feature_engineering.py
python src/customer_segmentation.py
python src/forecasting/prepare_dataset.py
python src/forecasting/feature_builder.py
python src/forecasting/train_model.py
python src/forecasting/evaluate_model.py
python src/inventory/inventory_optimizer.py
python src/customer/customer_intelligence.py
python src/recommendation/market_basket.py
python src/dashboard/generate_kpis.py
```

---

## 📊 Forecasting Results

The best forecasting model in the current pipeline is:

* **XGBoost**
* **MAPE:** ~11.78%

This makes it the selected production model for revenue forecasting in the dashboard.

---

## 📦 Inventory Intelligence Snapshot

Current inventory outputs include:

* **ABC classes** for revenue contribution
* **XYZ classes** for demand variability
* **Safety stock** for replenishment buffers
* **Reorder point** for stock planning
* **Priority labels** for operational action

---

## 👥 Customer Intelligence Snapshot

The customer intelligence layer provides:

* CLV estimation
* Tier assignment
* Churn risk classification
* Health scoring
* Customer-level 360 profiles

---

## 🤖 Recommendation Engine Snapshot

The recommendation engine produces:

* Frequent itemsets
* Association rules
* Product affinities
* Cross-sell signals

---

## 🧪 Sample Dataset

The sales dataset contains fields such as:

* Invoice
* StockCode
* Description
* Quantity
* InvoiceDate
* Price
* Customer ID
* Country
* Total Price

---

## 📌 Notes

* File paths are centralized in `config/paths.py`
* App settings are centralized in `config/settings.py`
* Generated outputs are stored in the `outputs/` folder
* The dashboard is designed to work as a modular analytics application

---

## 👨‍💻 Author

Built by **Ayush**

---

## ⭐ If this project helped you

Give the repository a star, fork it, and use it as a base for your own retail analytics or MLOps portfolio project.
