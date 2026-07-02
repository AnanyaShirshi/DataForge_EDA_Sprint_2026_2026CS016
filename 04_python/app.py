import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="DataForge Superstore Dashboard", 
                   layout="wide")

# Title
st.title("🛒 Global Superstore EDA Dashboard")
st.markdown("**DataForge EDA Hackathon — Final Submission**")

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel('dataset_cleaned.xlsx', engine='openpyxl')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Shipping Delay'] = (df['Ship Date'] - df['Order Date']).dt.days
    df['Profit Margin'] = df['Profit'] / df['Sales']
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect(
    "Select Region", 
    options=df['Region'].unique(),
    default=df['Region'].unique()
)
selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

# Apply filters
filtered_df = df[
    (df['Region'].isin(selected_region)) & 
    (df['Category'].isin(selected_category))
]

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Avg Discount", f"{filtered_df['Discount'].mean():.1%}")
col4.metric("Avg Shipping Delay", f"{filtered_df['Shipping Delay'].mean():.1f} days")

st.markdown("---")

# Charts Row
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")
    fig, ax = plt.subplots(figsize=(6,4))
    filtered_df.groupby('Region')['Sales'].sum().sort_values().plot(
        kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel("Total Sales")
    st.pyplot(fig)

with col2:
    st.subheader("Profit by Category")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x='Category', y='Profit', data=filtered_df, ax=ax)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Trend Over Time")
    fig, ax = plt.subplots(figsize=(6,4))
    filtered_df.groupby(
        filtered_df['Order Date'].dt.to_period('M'))['Sales'].sum().plot(
        ax=ax, color='green')
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(6,4))
    numeric_df = filtered_df.select_dtypes(include='number')
    sns.heatmap(numeric_df.corr(), annot=True, 
                cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)

# Raw data toggle
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df.head(100))
