import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="ML Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Machine Learning Model Performance Dashboard")

# ==========================================================
# Load Metrics
# ==========================================================

metrics = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\src\outputs\forecasting\metrics\model_metrics.csv"
)

best = metrics.sort_values("MAPE").iloc[0]

# ==========================================================
# KPI Cards
# ==========================================================

st.subheader("📌 Overall Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🏆 Best Model", best["Model"])
c2.metric("MAPE", f"{best['MAPE']*100:.2f}%")
c3.metric("MAE", f"{best['MAE']:.2f}")
c4.metric("RMSE", f"{best['RMSE']:.2f}")

st.divider()

# ==========================================================
# Comparison Charts
# ==========================================================

st.subheader("📈 Model Comparison")

left, right = st.columns(2)

with left:

    fig = px.bar(
        metrics,
        x="Model",
        y="MAPE",
        color="Model",
        text="MAPE",
        title="MAPE Comparison"
    )

    fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.bar(
        metrics,
        x="Model",
        y="MAE",
        color="Model",
        text="MAE",
        title="MAE Comparison"
    )

    fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# RMSE Chart
# ==========================================================

fig = px.bar(
    metrics,
    x="Model",
    y="RMSE",
    color="Model",
    text="RMSE",
    title="RMSE Comparison"
)

fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# Metrics Table
# ==========================================================

st.subheader("📋 Complete Performance Metrics")

st.dataframe(
    metrics.style.highlight_min(subset=["MAPE"], color="lightgreen"),
    use_container_width=True
)

st.divider()

# ==========================================================
# Evaluation Images
# ==========================================================

st.subheader("🖼 Evaluation Charts")

folder = r"C:\Users\ka843\Coding\Amdox Internship_project\src\outputs\forecasting\plots"

charts = [
    ("Actual vs Predicted", "actual_vs_predicted.png"),
    ("Residual Plot", "residual_plot.png"),
    ("Feature Importance", "feature_importance.png")
]

cols = st.columns(len(charts))

for col, (title, file) in zip(cols, charts):

    path = os.path.join(folder, file)

    if os.path.exists(path):

        with col:
            st.markdown(f"**{title}**")
            st.image(path, use_container_width=True)

st.divider()

# ==========================================================
# Best Model Summary
# ==========================================================

st.subheader("🏆 Best Model Summary")

st.success(
    f"""
### Selected Production Model

**Model:** {best['Model']}

**MAPE:** {best['MAPE']*100:.2f}%  
**MAE:** {best['MAE']:.2f}  
**RMSE:** {best['RMSE']:.2f}

This model achieved the lowest forecasting error and has been selected as the production model for the Retail AI Platform.
"""
)