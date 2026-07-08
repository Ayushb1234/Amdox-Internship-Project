import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(layout="wide")

st.title("📈 Demand Forecasting Dashboard")

# =====================================================
# Load Files
# =====================================================

metrics = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\forecasting\metrics\model_metrics.csv"
)

forecast = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\data\forecasting\forecast_dataset.csv"
)

forecast["Date"] = pd.to_datetime(forecast["Date"])

# =====================================================
# KPI Cards
# =====================================================

best = metrics.sort_values("MAPE").iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Best Model", best["Model"])
c2.metric("MAPE", f"{best['MAPE']*100:.2f}%")
c3.metric("MAE", f"{best['MAE']:.2f}")
c4.metric("RMSE", f"{best['RMSE']:.2f}")

st.divider()

# =====================================================
# Model Comparison
# =====================================================

st.subheader("Model Comparison")

fig = px.bar(
    metrics,
    x="Model",
    y="MAPE",
    color="Model",
    text="MAPE"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# Revenue Trend
# =====================================================

st.subheader("Daily Revenue")

fig = px.line(
    forecast,
    x="Date",
    y="Revenue",
    title="Revenue Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# Moving Average
# =====================================================

forecast["7-Day MA"] = forecast["Revenue"].rolling(7).mean()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=forecast["Date"],
    y=forecast["Revenue"],
    name="Revenue"
))

fig.add_trace(go.Scatter(
    x=forecast["Date"],
    y=forecast["7-Day MA"],
    name="7-Day Moving Average"
))

fig.update_layout(title="Revenue vs Moving Average")

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# Monthly Revenue
# =====================================================

forecast["Month"] = forecast["Date"].dt.to_period("M").astype(str)

monthly = (

    forecast

    .groupby("Month")["Revenue"]

    .sum()

    .reset_index()

)

fig = px.bar(
    monthly,
    x="Month",
    y="Revenue",
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# Metrics Table
# =====================================================

st.subheader("Forecast Metrics")

st.dataframe(metrics, use_container_width=True)