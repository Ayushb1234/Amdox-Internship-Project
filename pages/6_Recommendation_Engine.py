import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("🤖 AI Product Recommendation Engine")

# ==========================================================
# Load Association Rules
# ==========================================================

rules = pd.read_csv(
    r"C:\Users\ka843\Coding\Amdox Internship_project\outputs\recommendation\association_rules.csv"
)

# Convert frozenset strings to readable text
def clean_text(x):
    return (
        str(x)
        .replace("frozenset({", "")
        .replace("})", "")
        .replace("{", "")
        .replace("}", "")
        .replace("'", "")
    )

rules["antecedents"] = rules["antecedents"].apply(clean_text)
rules["consequents"] = rules["consequents"].apply(clean_text)

# ==========================================================
# KPI Cards
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("Association Rules", len(rules))
c2.metric("Average Lift", f"{rules['lift'].mean():.2f}")
c3.metric("Average Confidence", f"{rules['confidence'].mean():.2f}")
c4.metric("Average Support", f"{rules['support'].mean():.3f}")

st.divider()

# ==========================================================
# Top Rules
# ==========================================================

st.subheader("Top Product Associations")

top_rules = rules.sort_values(
    "lift",
    ascending=False
).head(20)

st.dataframe(
    top_rules[
        [
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]
    ],
    use_container_width=True
)

# ==========================================================
# Lift Chart
# ==========================================================

fig = px.bar(
    top_rules,
    x="lift",
    y="antecedents",
    color="confidence",
    orientation="h",
    hover_data=["consequents"],
    title="Top Rules by Lift"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Scatter Plot
# ==========================================================

fig = px.scatter(
    rules,
    x="support",
    y="confidence",
    size="lift",
    color="lift",
    hover_data=["antecedents", "consequents"],
    title="Association Rule Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# Product Search
# ==========================================================

st.subheader("Search Recommendations")

products = sorted(rules["antecedents"].unique())

selected = st.selectbox(
    "Choose Product",
    products
)

recommend = rules[
    rules["antecedents"] == selected
].sort_values(
    "lift",
    ascending=False
)

if len(recommend) > 0:

    st.success(f"Products commonly bought with: {selected}")

    st.dataframe(
        recommend[
            [
                "consequents",
                "support",
                "confidence",
                "lift"
            ]
        ],
        use_container_width=True
    )

else:

    st.warning("No recommendations available.")

# ==========================================================
# Raw Rules
# ==========================================================

st.subheader("Association Rules Dataset")

st.dataframe(
    rules.head(100),
    use_container_width=True
)