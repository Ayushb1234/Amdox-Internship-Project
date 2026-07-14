import streamlit as st

from components.cards import Cards

st.set_page_config(layout="wide")

c1, c2, c3, c4 = st.columns(4)

with c1:
    Cards.revenue(20476634)

with c2:
    Cards.orders(40078)

with c3:
    Cards.customers(5878)

with c4:
    Cards.products(4917)