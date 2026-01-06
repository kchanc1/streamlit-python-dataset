import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["2020"]*7 + ["2021"]*7 + ["2022"]*7 + ["2023"]*7 + ["2024"]*7,
    "Category": ["Transaction Expense", "Sales And Marketing", "Technology & Development", 
                 "General & Administrative", "Crypto Asset Impairment, Net", "Restructuring", "Others"]*5,
    "Operating Expenses By Category In Percentage": [
        15.6, 6.5, 31.3, 32.2, 0.0, 0.0, 14.3,
        26.6, 13.9, 27.1, 19.1, 3.2, 0.0, 10.0,
        10.7, 8.6, 39.4, 27.1, 12.2, 0.7, 1.3,
        12.9, 10.2, 40.5, 32.9, -1.1, 4.4, 0.3,
        20.7, 15.1, 33.9, 30.0, 0.0, 0.0, 0.2
    ]
}

df = pd.DataFrame(data)

fig_stack = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses By Category In Percentage",
    color="Category",
    barmode="stack",
    text="Operating Expenses By Category In Percentage",
    title="Operating Expenses By Category (%)"
)

fig_stack.update_traces(
    texttemplate="%{text:,.1f}%",
    textposition="inside",
    textfont=dict(size=12, color="white", family="Arial")
)

fig_stack.update_yaxes(title="Operating Expenses In Percentage")
fig_stack.update_layout(
    title=dict(text="Operating Expenses By Category (%)",
               font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    autosize=True,
    legend=dict(title="Category", font=dict(size=12, family="Arial"))
)

config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": False
}

st.plotly_chart(fig_stack, use_container_width=True, config=config)
st.markdown("Visit [StockDividendScreener.com](https://www.StockDividendScreener.com) for more statistics.")
