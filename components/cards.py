import streamlit as st

from config.settings import (
    CURRENCY,
    SUCCESS,
    WARNING,
    DANGER
)


class Cards:

    #########################################################
    # Number Formatter
    #########################################################

    @staticmethod
    def format_number(value):

        if value >= 1_000_000_000:

            return f"{value/1_000_000_000:.2f}B"

        elif value >= 1_000_000:

            return f"{value/1_000_000:.2f}M"

        elif value >= 1_000:

            return f"{value/1_000:.2f}K"

        return f"{value:.0f}"

    #########################################################
    # Currency Formatter
    #########################################################

    @staticmethod
    def format_currency(value):

        return f"{CURRENCY}{Cards.format_number(value)}"

    #########################################################
    # Percentage Formatter
    #########################################################

    @staticmethod
    def format_percent(value):

        return f"{value:.2f}%"

    #########################################################
    # KPI Card
    #########################################################

    @staticmethod
    def metric(

        title,

        value,

        delta=None,

        help=None

    ):

        st.metric(

            label=title,

            value=value,

            delta=delta,

            help=help

        )

    #########################################################
    # Revenue Card
    #########################################################

    @staticmethod
    def revenue(

        value,

        delta=None

    ):

        Cards.metric(

            "💰 Revenue",

            Cards.format_currency(value),

            delta

        )

    #########################################################
    # Orders Card
    #########################################################

    @staticmethod
    def orders(

        value,

        delta=None

    ):

        Cards.metric(

            "📦 Orders",

            Cards.format_number(value),

            delta

        )

    #########################################################
    # Customers
    #########################################################

    @staticmethod
    def customers(

        value,

        delta=None

    ):

        Cards.metric(

            "👥 Customers",

            Cards.format_number(value),

            delta

        )

    #########################################################
    # Products
    #########################################################

    @staticmethod
    def products(

        value,

        delta=None

    ):

        Cards.metric(

            "🛒 Products",

            Cards.format_number(value),

            delta

        )

    #########################################################
    # Profit
    #########################################################

    @staticmethod
    def profit(

        value,

        delta=None

    ):

        Cards.metric(

            "📈 Profit",

            Cards.format_currency(value),

            delta

        )

    #########################################################
    # Percentage KPI
    #########################################################

    @staticmethod
    def percentage(

        title,

        value,

        delta=None

    ):

        Cards.metric(

            title,

            Cards.format_percent(value),

            delta

        )