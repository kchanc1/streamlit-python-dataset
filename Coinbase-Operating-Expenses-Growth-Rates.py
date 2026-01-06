import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2021", "FY2022", "FY2023", "FY2024"],
    "Operating Expenses Growth Rates": [448.4, 24.0, -44.6, 32.4]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses Growth Rates",
    title="Operating Expenses Growth Rates (%)",
    text="Operating Expenses Growth Rates"
)

# Format labels as percentages
fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    textfont=dict(size=12, color="blue", family="Arial")
)

# Add axis styling
fig.update_yaxes(title="Growth Rate (%)")
fig.update_layout(
    title=dict(text="Operating Expenses Growth Rates (%)", font=dict(size=22, family="Arial", color="black")),
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
st.markdown("Visit [StockDividendScreener.com](https://www.StockDividendScreener.com) for more statistics")
