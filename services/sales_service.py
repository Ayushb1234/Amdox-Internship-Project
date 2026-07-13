import pandas as pd

from utils.loader import DataLoader


class SalesService:

    def __init__(self):

        self.df = DataLoader.sales()

        self.prepare()

    #########################################################

    def prepare(self):

        self.df["Year"] = self.df["InvoiceDate"].dt.year

        self.df["Quarter"] = self.df["InvoiceDate"].dt.quarter

        self.df["Month"] = (
            self.df["InvoiceDate"]
            .dt.to_period("M")
            .astype(str)
        )

        self.df["Weekday"] = (
            self.df["InvoiceDate"]
            .dt.day_name()
        )

        self.df["Hour"] = (
            self.df["InvoiceDate"]
            .dt.hour
        )

    #########################################################

    def kpis(self):

        return {

            "Revenue":

                self.df["Total_Price"].sum(),

            "Orders":

                self.df["Invoice"].nunique(),

            "Customers":

                self.df["Customer_ID"].nunique(),

            "Products":

                self.df["StockCode"].nunique()

        }

    #########################################################

    def monthly_sales(self):

        return (

            self.df

            .groupby("Month", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

        )

    #########################################################

    def yearly_sales(self):

        return (

            self.df

            .groupby("Year", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

        )

    #########################################################

    def quarterly_sales(self):

        return (

            self.df

            .groupby("Quarter", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

        )

    #########################################################

    def weekday_sales(self):

        order = [

            "Monday",

            "Tuesday",

            "Wednesday",

            "Thursday",

            "Friday",

            "Saturday",

            "Sunday"

        ]

        data = (

            self.df

            .groupby("Weekday", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

        )

        data["Weekday"] = pd.Categorical(

            data["Weekday"],

            categories=order,

            ordered=True

        )

        return (

            data

            .sort_values("Weekday")

        )

    #########################################################

    def hourly_sales(self):

        return (

            self.df

            .groupby("Hour", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

        )

    #########################################################

    def country_sales(self):

        return (

            self.df

            .groupby("Country", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue",

                ascending=False

            )

        )

    #########################################################

    def category_sales(self):

        return (

            self.df

            .groupby("Category", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue",

                ascending=False

            )

        )

    #########################################################

    def subcategory_sales(self):

        return (

            self.df

            .groupby("Sub-Category", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue",

                ascending=False

            )

        )

    #########################################################

    def top_products(self, n=10):

        return (

            self.df

            .groupby("Description", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue",

                ascending=False

            )

            .head(n)

        )

    #########################################################

    def bottom_products(self, n=10):

        return (

            self.df

            .groupby("Description", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue"

            )

            .head(n)

        )

    #########################################################

    def top_customers(self, n=10):

        return (

            self.df

            .groupby("Customer_ID", as_index=False)

            .agg(

                Revenue=("Total_Price", "sum")

            )

            .sort_values(

                "Revenue",

                ascending=False

            )

            .head(n)

        )

    #########################################################

    def dashboard_summary(self):

        return {

            "KPIs": self.kpis(),

            "Monthly": self.monthly_sales(),

            "Country": self.country_sales(),

            "Top Products": self.top_products()

        }