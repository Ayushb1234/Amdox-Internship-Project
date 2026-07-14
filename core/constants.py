from __future__ import annotations

from datetime import datetime


class App:
    """
    Application Information
    """

    NAME = "NeuralRetail AI"

    VERSION = "2.0.0"

    DESCRIPTION = (
        "Enterprise AI Retail Analytics Platform"
    )

    AUTHOR = "Ayush Choudhary"

    COPYRIGHT = (
        f"© {datetime.now().year} NeuralRetail AI"
    )


# ==========================================================
# UI
# ==========================================================

class UI:

    PAGE_TITLE = "NeuralRetail AI"

    PAGE_ICON = "🛒"

    LAYOUT = "wide"

    SIDEBAR_STATE = "expanded"


# ==========================================================
# Currency
# ==========================================================

class Currency:

    SYMBOL = "$"

    DECIMALS = 2


# ==========================================================
# Date
# ==========================================================

class DateFormat:

    DEFAULT = "%d-%m-%Y"

    MONTH = "%b %Y"

    YEAR = "%Y"

    DATETIME = "%d-%m-%Y %H:%M"


# ==========================================================
# Dashboard
# ==========================================================

class Dashboard:

    KPI_COLUMNS = 4

    CHART_HEIGHT = 420

    LARGE_CHART = 520

    TABLE_HEIGHT = 450


# ==========================================================
# Cache
# ==========================================================

class Cache:

    TTL = 3600


# ==========================================================
# Charts
# ==========================================================

class Charts:

    TEMPLATE = "plotly_white"

    MARGIN = dict(

        l=10,

        r=10,

        t=45,

        b=10

    )


# ==========================================================
# Animation
# ==========================================================

class Animation:

    SPEED = "0.35s"

    BORDER_RADIUS = "18px"

    SHADOW = (
        "0 8px 24px rgba(0,0,0,0.12)"
    )


# ==========================================================
# Status
# ==========================================================

class Status:

    SUCCESS = "success"

    WARNING = "warning"

    ERROR = "error"

    INFO = "info"