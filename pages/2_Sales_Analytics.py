import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📈 Sales Analytics Dashboard")

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

df = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\data\clean\clean_sales.csv",
    parse_dates=["InvoiceDate"],
    low_memory=False
)

# ----------------------------------------------------
# Time Features
# ----------------------------------------------------

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

revenue = df["Total_Price"].sum()
orders = df["Invoice"].nunique()
customers = df["Customer_ID"].nunique()
products = df["StockCode"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Revenue", f"${revenue:,.0f}")
c2.metric("Orders", f"{orders:,}")
c3.metric("Customers", f"{customers:,}")
c4.metric("Products", f"{products:,}")

st.divider()

# ----------------------------------------------------
# Monthly Revenue
# ----------------------------------------------------

monthly = (

    df.groupby("Month")["Total_Price"]

    .sum()

    .reset_index()

)

fig = px.line(

    monthly,

    x="Month",

    y="Total_Price",

    title="Monthly Revenue"

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# Top Products
# ----------------------------------------------------

top_products = (

    df.groupby("Description")["Total_Price"]

    .sum()

    .sort_values(ascending=False)

    .head(10)

    .reset_index()

)

fig = px.bar(

    top_products,

    x="Total_Price",

    y="Description",

    orientation="h",

    title="Top 10 Products"

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# Revenue by Country
# ----------------------------------------------------

country = (

    df.groupby("Country")["Total_Price"]

    .sum()

    .sort_values(ascending=False)

    .head(10)

    .reset_index()

)

fig = px.bar(

    country,

    x="Country",

    y="Total_Price",

    title="Top Countries"

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# Sales by Weekday
# ----------------------------------------------------

df["Weekday"] = df["InvoiceDate"].dt.day_name()

weekday = (

    df.groupby("Weekday")["Total_Price"]

    .sum()

    .reindex(
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

    .reset_index()

)

fig = px.bar(

    weekday,

    x="Weekday",

    y="Total_Price",

    title="Revenue by Weekday"

)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# Raw Data
# ----------------------------------------------------

st.subheader("Sales Dataset")

st.dataframe(df.head(100))