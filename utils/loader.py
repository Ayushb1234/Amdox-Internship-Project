import pandas as pd
import streamlit as st

from config.paths import (
    SALES,
    CUSTOMER,
    INVENTORY,
    FORECAST_METRICS,
    RULES
)


class DataLoader:

    @staticmethod
    @st.cache_data(show_spinner=False)
    def sales():

        return pd.read_csv(
            SALES,
            parse_dates=["InvoiceDate"],
            low_memory=False
        )

    #########################################################

    @staticmethod
    @st.cache_data(show_spinner=False)
    def customers():

        return pd.read_csv(
            CUSTOMER,
            low_memory=False
        )

    #########################################################

    @staticmethod
    @st.cache_data(show_spinner=False)
    def inventory():

        return pd.read_csv(
            INVENTORY,
            low_memory=False
        )

    #########################################################

    @staticmethod
    @st.cache_data(show_spinner=False)
    def forecast():

        return pd.read_csv(
            FORECAST_METRICS,
            low_memory=False
        )

    #########################################################

    @staticmethod
    @st.cache_data(show_spinner=False)
    def rules():

        return pd.read_csv(
            RULES,
            low_memory=False
        )