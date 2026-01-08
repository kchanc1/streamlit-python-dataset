import streamlit as st
import pandas as pd
import plotly.express as px

# Data
data = {
    "Fiscal Year": ["FY2020", "FY2021", "FY2022", "FY2023", "FY2024"],
    "Customer Custodial Funds": [3763, 10526, 5041, 4571, 6159],
    "Cash On Hand": [1142, 7254, 5312, 5738, 9825]
}

df = pd.DataFrame(data)

# Melt data for stacked bar chart
df_melted = df.melt(id_vars="Fiscal Year", 
                    value_vars=["Customer Custodial Funds", "Cash On Hand"],
                    var_name="Category", 
                    value_name="Amount")

# Create stacked bar chart
fig = px.bar(
    df_melted,
    x="Fiscal Year",
    y="Amount",
    color="Category",
    title="Coinbase Global: Customer Custodial Funds vs <br>Cash On Hand ($ Millions)",
    text_auto=True
)

# Layout styling
fig.update_layout(
    barmode="stack",
    xaxis_title="Fiscal Year",
    yaxis_title="Amount (in Millions USD)",
    legend_title="Category",
    title_font=dict(size=22, family="Arial", color="black"),
    xaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue")),
    yaxis=dict(tickfont=dict(size=14, family="Arial", color="darkblue"))
)

# Show chart in Streamlit
config = {
    "displayModeBar": True,
    "scrollZoom": False,
    "responsive": False
}

st.plotly_chart(fig, config=config)

# Add footer link
st.markdown("Visit [StockDividendScreener.com](https://StockDividendScreener.com) for more statistics.")