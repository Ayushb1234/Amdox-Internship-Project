from config.path2 import SALES_FILE, CUSTOMER_FILE
import pandas as pd

pd.read_csv(SALES_FILE, low_memory=False)
pd.read_csv(CUSTOMER_FILE, low_memory=False)
