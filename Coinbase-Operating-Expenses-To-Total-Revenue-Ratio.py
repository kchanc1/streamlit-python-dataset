import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2020", "FY2021", "FY2022", "FY2023", "FY2024"],
    "Operating Expenses To Total Revenue Ratio": [68.0, 60.8, 184.9, 105.2, 65.9]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses To Total Revenue Ratio",
    title="Operating Expenses To Total Revenue Ratio (%)",
    text="Operating Expenses To Total Revenue Ratio"
)

# Format labels as percentages
fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    textfont=dict(size=12, color="blue", family="Arial")
)

# Add axis styling
fig.update_yaxes(title="To Total Revenue Ratio (%)")
fig.update_layout(
    title=dict(text="Operating Expenses To Total Revenue Ratio (%)", font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue"))
)

config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": False
}

# Correct Streamlit call
st.plotly_chart(fig, use_container_width=True, config=config)