import os
import numpy as np
import pandas as pd


class InventoryOptimizer:

    def __init__(self, filepath):

        self.filepath = filepath

        os.makedirs("../outputs/inventory", exist_ok=True)

    ############################################################

    def load_data(self):

        print("=" * 60)
        print("Loading Sales Dataset")
        print("=" * 60)

        self.df = pd.read_csv(

            self.filepath,

            parse_dates=["InvoiceDate"],

            dtype={
                "Invoice": str,
                "StockCode": str
            },

            low_memory=False

        )

        print(self.df.shape)

    ############################################################

    def create_daily_product_sales(self):

        print("\nCreating Product Daily Sales...\n")

        self.df["Date"] = self.df["InvoiceDate"].dt.date

        daily = (

            self.df

            .groupby(

                ["StockCode", "Description", "Date"]

            )

            .agg(

                Daily_Quantity=("Quantity", "sum"),

                Daily_Revenue=("Total_Price", "sum")

            )

            .reset_index()

        )

        self.daily = daily

        print("Daily Product Records :", len(daily))

    ############################################################

    def product_statistics(self):

        print("\nCreating Product Statistics...\n")

        product = (

            self.daily

            .groupby(

                ["StockCode", "Description"]

            )

            .agg(

                Revenue=("Daily_Revenue", "sum"),

                Quantity=("Daily_Quantity", "sum"),

                Avg_Daily_Demand=("Daily_Quantity", "mean"),

                Demand_STD=("Daily_Quantity", "std"),

                Max_Demand=("Daily_Quantity", "max"),

                Min_Demand=("Daily_Quantity", "min"),

                Selling_Days=("Date", "count")

            )

            .reset_index()

        )

        product["Demand_STD"] = product["Demand_STD"].fillna(0)

        self.product = product

        print(product.shape)

    ############################################################

    def save(self):

        self.product.to_csv(

            "../outputs/inventory/product_statistics.csv",

            index=False

        )

        print("\nProduct Statistics Saved")

    ############################################################

    def run(self):

        self.load_data()

        self.create_daily_product_sales()

        self.product_statistics()

        self.save()

        print("\nInventory Module Step 1 Completed")


if __name__ == "__main__":

    obj = InventoryOptimizer(

        r"C:\Users\ka843\Coding\Amdox Internship_project\data\clean\clean_sales.csv"

    )

    obj.run()