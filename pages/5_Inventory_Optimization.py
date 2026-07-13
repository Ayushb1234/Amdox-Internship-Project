import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📦 Inventory Optimization Dashboard")

# ==========================================================
# Load Inventory Data
# ==========================================================

df = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\src\outputs\inventory\product_inventory.csv"
)

# ==========================================================
# KPI Cards
# ==========================================================

products = len(df)

urgent = (df["Priority"] == "Urgent").sum()

reorder = (df["Priority"] == "Reorder").sum()

avg_safety = df["Safety_Stock"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", f"{products:,}")

c2.metric("Urgent Products", urgent)

c3.metric("Reorder Products", reorder)

c4.metric("Average Safety Stock", f"{avg_safety:.2f}")

st.divider()

# ==========================================================
# ABC Distribution
# ==========================================================

st.subheader("ABC Classification")

abc = df["ABC_Class"].value_counts().reset_index()

abc.columns = ["Class", "Products"]

fig = px.pie(

    abc,

    names="Class",

    values="Products",

    hole=0.45,

    title="ABC Analysis"

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# XYZ Distribution
# ==========================================================

st.subheader("XYZ Classification")

xyz = df["XYZ_Class"].value_counts().reset_index()

xyz.columns = ["Class", "Products"]

fig = px.bar(

    xyz,

    x="Class",

    y="Products",

    color="Class",

    text="Products",

    title="XYZ Analysis"

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Inventory Matrix
# ==========================================================

st.subheader("Inventory Matrix")

matrix = (

    df["Inventory_Class"]

    .value_counts()

    .reset_index()

)

matrix.columns = [

    "Inventory Class",

    "Count"

]

fig = px.bar(

    matrix,

    x="Inventory Class",

    y="Count",

    color="Inventory Class",

    text="Count"

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Stockout Risk
# ==========================================================

st.subheader("Stockout Risk")

risk = (

    df["Stockout_Risk"]

    .value_counts()

    .reset_index()

)

risk.columns = [

    "Risk",

    "Products"

]

fig = px.pie(

    risk,

    names="Risk",

    values="Products",

    hole=0.4

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Priority
# ==========================================================

st.subheader("Priority Distribution")

priority = (

    df["Priority"]

    .value_counts()

    .reset_index()

)

priority.columns = [

    "Priority",

    "Products"

]

fig = px.bar(

    priority,

    x="Priority",

    y="Products",

    color="Priority",

    text="Products"

)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Top Reorder Products
# ==========================================================

st.subheader("Products Needing Immediate Action")

urgent_df = (

    df

    .sort_values(

        "Reorder_Point",

        ascending=False

    )

)

st.dataframe(

    urgent_df[

        [

            "StockCode",

            "Description",

            "ABC_Class",

            "XYZ_Class",

            "Inventory_Class",

            "Safety_Stock",

            "Reorder_Point",

            "Priority"

        ]

    ].head(25),

    use_container_width=True

)

# ==========================================================
# Product Search
# ==========================================================

st.subheader("Search Product")

product = st.selectbox(

    "Select Product",

    sorted(df["StockCode"].unique())

)

st.dataframe(

    df[

        df["StockCode"] == product

    ],

    use_container_width=True

)