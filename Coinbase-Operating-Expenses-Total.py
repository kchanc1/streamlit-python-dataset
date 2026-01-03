import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["FY2020", "FY2021", "FY2022", "FY2023", "FY2024"],
    "Total Operating Expenses": [868.5, 4762.9, 5904.6, 3270.3, 4328.6]
}
df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Total Operating Expenses",
    title="Operating Expenses by Fiscal Year ($ Millions)",
    text="Total Operating Expenses"
)

# Format hover labels as currency
fig.update_traces(texttemplate="<b>$%{text:,.1f}</b>", textposition="outside", textfont=dict(size=12, color="blue", family="Arial")
)
fig.update_yaxes(title="Operating Expenses (USD)")


fig.update_layout(
    title=dict(text="Operating Expenses by Fiscal Year ($ Millions)", font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue"))
)

config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": True
}

st.plotly_chart(fig, width="stretch", config=config)
