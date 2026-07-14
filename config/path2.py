from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
SRC_OUTPUTS_DIR = BASE_DIR / "src" / "outputs"
SRC_DIR = BASE_DIR / "src"


def output_path(*parts):
    path = OUTPUTS_DIR.joinpath(*parts)
    if path.exists():
        return path
    return SRC_OUTPUTS_DIR.joinpath(*parts)


SALES_FILE = DATA_DIR / "clean" / "clean_sales.csv"
CUSTOMER_FILE = output_path("customer", "customer_360.csv")
INVENTORY_FILE = output_path("inventory", "product_inventory.csv")
FORECAST_METRICS_FILE = output_path("forecasting", "metrics", "model_metrics.csv")
FORECAST_PLOTS_DIR = OUTPUTS_DIR / "forecasting" / "plots"
DASHBOARD_KPI_FILE = OUTPUTS_DIR / "dashboard" / "dashboard_kpis.json"
RECOMMENDATION_RULES_FILE = output_path("recommendation", "association_rules.csv")
