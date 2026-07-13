from services.sales_service import SalesService

service = SalesService()

print(service.kpis())

print()

print(service.monthly_sales().head())

print()

print(service.country_sales().head())

print()

print(service.top_products().head())