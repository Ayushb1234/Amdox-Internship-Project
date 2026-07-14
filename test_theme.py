import streamlit as st

from ui.layout import Layout

st.set_page_config(

    page_title="NeuralRetail AI",

    layout="wide"

)

Layout.load_css()

st.title("NeuralRetail AI")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Revenue","$20.47M")

c2.metric("Orders","40,078")

c3.metric("Customers","5,878")

c4.metric("Products","4,917")

st.button("Generate AI Insights")
