import json
import streamlit as st

st.set_page_config(layout="wide")

st.title("📊 Executive Overview")

with open(

r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\dashboard\dashboard_kpis.json"

) as f:

    kpi = json.load(f)

col1, col2, col3 = st.columns(3)

col1.metric(

    "Revenue",

    f"${kpi['Revenue']:,.0f}"

)

col2.metric(

    "Orders",

    kpi["Orders"]

)

col3.metric(

    "Customers",

    kpi["Customers"]

)

col4, col5, col6 = st.columns(3)

col4.metric(

    "Forecast MAPE",

    f"{kpi['Forecast_MAPE']*100:.2f}%"

)

col5.metric(

    "Urgent Products",

    kpi["Urgent_Products"]

)

col6.metric(

    "High Risk Customers",

    kpi["High_Risk_Customers"]

)

st.markdown("---")

st.success("NeuralRetail AI Platform Running Successfully")
