import streamlit as st
from config.settings import *

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR
)

st.title("🛒 NeuralRetail AI Sales Intelligence")

st.markdown("---")

st.markdown("""

## Welcome

Enterprise AI Retail Analytics Platform

### Modules

- Executive Overview

- Sales Analytics

- Customer Intelligence

- Demand Forecasting

- Inventory Optimization

- Recommendation Engine

- Model Performance

""")