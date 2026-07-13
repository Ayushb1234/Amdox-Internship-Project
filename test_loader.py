from utils.loader import DataLoader

sales = DataLoader.sales()
customer = DataLoader.customers()
inventory = DataLoader.inventory()
forecast = DataLoader.forecast()

print("Sales      :", sales.shape)
print("Customer   :", customer.shape)
print("Inventory  :", inventory.shape)
print("Forecast   :", forecast.shape)