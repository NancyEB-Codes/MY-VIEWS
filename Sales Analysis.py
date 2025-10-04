import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Load dataset from repo ---
file_path = os.path.join("data", "Clean_Superstore_Data.xlsx")
df = pd.read_excel(DATA/Clean_Superstore_Data.xlsx)

# --- Clean/transform dates ---
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Year'] = df['Order_Date'].dt.year
df['Quarter'] = df['Order_Date'].dt.to_period('Q').astype(str)

# --- Yearly Sales ---
yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()

st.title("📊 Superstore Sales Analysis")

st.subheader("Total Yearly Sales (2011–2014)")
fig_year = px.bar(
    yearly_sales,
    x="Year", y="Sales",
    text="Sales", color="Sales",
    color_continuous_scale="Blues",
    title="Total Sales by Year"
)
fig_year.update_traces(texttemplate='%{text:,.0f}', textposition="outside")
fig_year.update_layout(yaxis_title="Total Sales", xaxis_title="Year")
st.plotly_chart(fig_year, use_container_width=True)
st.dataframe(yearly_sales)

# --- Quarterly Sales ---
quarterly_sales = df.groupby('Quarter')['Sales'].sum().reset_index()
best_quarter = quarterly_sales.loc[quarterly_sales['Sales'].idxmax()]

st.subheader("Best Performing Quarter")
st.success(f"🏆 {best_quarter['Quarter']} with Sales of ${best_quarter['Sales']:,.2f}")

fig_quarter = px.bar(
    quarterly_sales,
    x="Quarter", y="Sales",
    text="Sales", color="Sales",
    color_continuous_scale="Blues",
    title="Quarterly Sales Performance"
)
fig_quarter.update_traces(texttemplate='%{text:,.0f}', textposition="outside")
fig_quarter.update_layout(xaxis_title="Quarter", yaxis_title="Total Sales")
st.plotly_chart(fig_quarter, use_container_width=True)
st.dataframe(quarterly_sales)

