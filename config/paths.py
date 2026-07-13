from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

DATA = BASE / "data"
OUTPUTS = BASE / "outputs"
SRC_OUTPUTS = BASE / "src" / "outputs"


def output_path(*parts):
    path = OUTPUTS.joinpath(*parts)
    if path.exists():
        return path
    return SRC_OUTPUTS.joinpath(*parts)

SALES = DATA / "clean" / "clean_sales.csv"
CUSTOMER = output_path("customer", "customer_360.csv")
INVENTORY = output_path("inventory", "product_inventory.csv")
FORECAST_METRICS = output_path("forecasting", "metrics", "model_metrics.csv")
DASHBOARD_KPI = output_path("dashboard", "dashboard_kpis.json")
RULES = output_path("recommendation", "association_rules.csv")
