import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2020", "FY2021", "FY2022", "FY2023", "FY2024"],
    "Total Cash": [1142, 7254, 5312, 5738, 9825]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Total Cash",
    title="Total Cash On Hand ($ Millions)",
    text="Total Cash"
)

# Format labels as percentages
fig.update_traces(
    texttemplate="$%{text:.1f}",
    textposition="outside",
    textfont=dict(size=12, color="blue", family="Arial")
)

# Add axis styling
fig.update_layout(
    title=dict(font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue"))
)

config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": False
}

# Correct Streamlit call
st.plotly_chart(fig, config=config)
st.markdown("Visit [StockDividendScreener.com](https://StockDividendScreener.com) for more statistics")
