import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    "Fiscal Year": ["2020"]*7 + ["2021"]*7 + ["2022"]*7 + ["2023"]*7 + ["2024"]*7,
    "Category": ["Transaction Expense", "Sales And Marketing", "Technology & Development", 
                 "General & Administrative", "Crypto Asset Impairment, Net", "Restructuring", "Others"]*5,
    "Operating Expenses By Category": [
        135.5, 56.8, 271.7, 279.9, 0.0, 0.0, 124.6,
        1267.9, 663.7, 1291.6, 909.4, 153.2, 0.0, 477.1,
        629.9, 510.1, 2326.3, 1600.7, 722.2, 40.8, 74.6,
        420.8, 332.4, 1324.6, 1074.3, -34.7, 142.6, 10.3,
        897.7, 654.4, 1468.3, 1300.3, 0.0, 0.0, 7.9
    ]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses By Category",
    color="Category",
    barmode="stack",  # stack categories for clarity
    text="Operating Expenses By Category",
    title="Operating Expenses By Category ($ Millions)"
)

fig.update_traces(
    texttemplate="$%{text:,.1f}",  # show numbers with commas
    textposition="inside",        # place labels inside bars for readability
    textfont=dict(size=12, color="white", family="Arial")
)

fig_stack = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses By Category",
    color="Category",
    barmode="stack",
    text="Operating Expenses By Category",
    title="Operating Expenses By Category (Stacked)"
)

fig_stack.update_traces(
    texttemplate="$%{text:,.1f}",
    textposition="inside",
    textfont=dict(size=12, color="white", family="Arial")
)

fig_group = px.bar(
    df,
    x="Fiscal Year",
    y="Operating Expenses By Category",
    color="Category",
    barmode="group",
    text="Operating Expenses By Category",
    title="Operating Expenses By Category (Grouped)"
)

fig_group.update_traces(
    texttemplate="$%{text:,.1f}",
    textposition="outside",
    textfont=dict(size=12, color="blue", family="Arial")
)

fig_stack.update_yaxes(title="Operating Expenses (USD millions)")
fig_stack.update_layout(
    title=dict(text="Operating Expenses By Category $ (Millions)",
               font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    legend=dict(title="Category", font=dict(size=12, family="Arial"))
)

fig_group.update_yaxes(title="Operating Expenses (USD millions)")
fig_group.update_layout(
    title=dict(text="Operating Expenses By Category $ (Millions)",
               font=dict(size=22, family="Arial", color="black")),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    legend=dict(title="Category", font=dict(size=12, family="Arial"))
)

config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": False
}

st.plotly_chart(fig_stack, use_container_width=True, config=config)
## st.plotly_chart(fig_group, use_container_width=True, config=config)