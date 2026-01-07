import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2019", "FY2020", "FY2021", "FY2022"],
    "Verified Users": [32, 43, 89, 110]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Verified Users",
    title="Verified Users (In Millions)",
    text="Verified Users"
)

# Format labels as percentages
fig.update_traces(
    texttemplate="%{text:.1f}",
    textposition="outside",
    textfont=dict(size=12, color="blue", family="Arial")
)

# Add axis styling
fig.update_yaxes(title="Verified Users")
fig.update_layout(
    title=dict(text="Verified Users (In Millions)", font=dict(size=22, family="Arial", color="black")),
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
