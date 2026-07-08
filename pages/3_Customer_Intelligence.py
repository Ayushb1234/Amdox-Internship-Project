import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("👥 Customer Intelligence")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\customer\customer_360.csv"
)

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

total_customers = len(df)
avg_clv = df["CLV"].mean()
avg_orders = df["Total_Orders"].mean()
avg_revenue = df["Total_Revenue"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", f"{total_customers:,}")
c2.metric("Average CLV", f"${avg_clv:,.2f}")
c3.metric("Avg Orders", f"{avg_orders:.2f}")
c4.metric("Avg Revenue", f"${avg_revenue:,.2f}")

st.divider()

# ---------------------------------------------------
# Customer Tier
# ---------------------------------------------------

tier = df["Tier"].value_counts().reset_index()
tier.columns = ["Tier", "Count"]

fig = px.pie(
    tier,
    names="Tier",
    values="Count",
    title="Customer Tier Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Churn Risk
# ---------------------------------------------------

risk = df["Churn_Risk"].value_counts().reset_index()
risk.columns = ["Risk", "Customers"]

fig = px.bar(
    risk,
    x="Risk",
    y="Customers",
    color="Risk",
    title="Customer Churn Risk"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Customer Health
# ---------------------------------------------------

health = df["Health"].value_counts().reset_index()
health.columns = ["Health", "Customers"]

fig = px.bar(
    health,
    x="Health",
    y="Customers",
    color="Health",
    title="Customer Health"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# CLV Distribution
# ---------------------------------------------------

fig = px.histogram(
    df,
    x="CLV",
    nbins=30,
    title="Customer Lifetime Value Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Top Customers
# ---------------------------------------------------

top = df.sort_values(
    "Total_Revenue",
    ascending=False
).head(20)

st.subheader("Top Revenue Customers")

st.dataframe(
    top[
        [
            "Customer_ID",
            "Total_Revenue",
            "CLV",
            "Tier",
            "Churn_Risk",
            "Health"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------------------
# Customer Search
# ---------------------------------------------------

st.subheader("Customer 360 Search")

customer = st.selectbox(
    "Select Customer",
    sorted(df["Customer_ID"].unique())
)

row = df[df["Customer_ID"] == customer]

st.dataframe(row, use_container_width=True)