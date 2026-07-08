import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")

st.title("📊 Machine Learning Model Performance")

# ==========================================================
# Load Metrics
# ==========================================================

metrics = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\forecasting\metrics\model_metrics.csv"
)

best = metrics.sort_values("MAPE").iloc[0]

# ==========================================================
# KPI Cards
# ==========================================================

c1,c2,c3,c4 = st.columns(4)

c1.metric("Best Model",best["Model"])
c2.metric("MAPE",f"{best['MAPE']*100:.2f}%")
c3.metric("MAE",f"{best['MAE']:.2f}")
c4.metric("RMSE",f"{best['RMSE']:.2f}")

st.divider()

# ==========================================================
# Model Comparison
# ==========================================================

st.subheader("Model Comparison")

fig = px.bar(
    metrics,
    x="Model",
    y="MAPE",
    color="Model",
    text="MAPE"
)

st.plotly_chart(fig,use_container_width=True)

# ==========================================================
# MAE Comparison
# ==========================================================

fig = px.bar(
    metrics,
    x="Model",
    y="MAE",
    color="Model",
    text="MAE",
    title="Mean Absolute Error"
)

st.plotly_chart(fig,use_container_width=True)

# ==========================================================
# RMSE Comparison
# ==========================================================

fig = px.bar(
    metrics,
    x="Model",
    y="RMSE",
    color="Model",
    text="RMSE",
    title="Root Mean Squared Error"
)

st.plotly_chart(fig,use_container_width=True)

# ==========================================================
# Metrics Table
# ==========================================================

st.subheader("Complete Metrics")

st.dataframe(
    metrics,
    use_container_width=True
)

# ==========================================================
# Saved Evaluation Images
# ==========================================================

st.subheader("Evaluation Charts")

folder = r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\forecasting\plots"

charts = [

    ("Actual vs Predicted","actual_vs_predicted.png"),

    ("Residual Plot","residual_plot.png"),

    ("Feature Importance","feature_importance.png")

]

for title,file in charts:

    path = os.path.join(folder,file)

    if os.path.exists(path):

        st.markdown(f"### {title}")

        st.image(path,use_container_width=True)

# ==========================================================
# Best Model Summary
# ==========================================================

st.success(f"""
🏆 Best Forecasting Model : {best['Model']}

Forecast Error (MAPE) : {best['MAPE']*100:.2f}%

This model has been selected as the production model for the Retail AI Platform.
""")