import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2019", "FY2020", "FY2021", "FY2022"],
    "Ratio Of MTU To Verified Users": [3.4, 4.4, 9.4, 8.0]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Ratio Of MTU To Verified Users",
    title="Annual Average MTU To Verified Users Ratio (%)",
    text="Ratio Of MTU To Verified Users"
)

# Format labels as percentages
fig.update_traces(
    texttemplate="%{text:.1f}%",
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
st.markdown("Visit [StockDividendScreener.com](https://www.StockDividendScreener.com) for more statistics")
