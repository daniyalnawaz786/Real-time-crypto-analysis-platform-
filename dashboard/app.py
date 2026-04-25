import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DB_PATH = "crypto.db"

st.set_page_config(page_title="Crypto Dashboard", page_icon="📈", layout="wide")
st.title("🚀 Real-Time Crypto Analytics Dashboard")

# Function to load data mapping to SQLite locally
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM crypto_prices", conn)
    conn.close()
    
    if not df.empty:
        # Convert timestamp strings back to proper datetime objects
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()

if df.empty:
    st.warning("No data available yet. Run the ETL pipeline first!")
else:
    # Top KPI Metrics Section
    st.markdown("### 📊 Market Overview (Live metrics)")
    latest_data = df.groupby("coin_name").last().reset_index()
    
    # Render Streamlit columns for each crypto coin dynamically
    cols = st.columns(len(latest_data))
    for i, row in latest_data.iterrows():
        with cols[i]:
            st.metric(
                label=f"{row['coin_name'].capitalize()}", 
                value=f"${row['price']:,.2f}", 
                delta=f"{row['change_24h']:.2f}%"
            )
            
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📈 Live Price Trends")
        # Creating an interactive line chart overlapping coins
        fig_line = px.line(df, x="timestamp", y="price", color="coin_name", 
                           title="Price Movement Over Time", markers=True)
        # Add smooth trendline styling
        fig_line.update_traces(line=dict(width=3))
        fig_line.update_layout(xaxis_title="Time", yaxis_title="Price (USD)", hovermode="x unified")
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        st.markdown("### 📉 24H Price Change")
        # Bar Chart showing performance context
        fig_bar = px.bar(latest_data, x="coin_name", y="change_24h", color="change_24h",
                         color_continuous_scale=px.colors.diverging.RdYlGn,
                         title="Market Gainers/Losers (%)")
                         
        fig_bar.update_layout(xaxis_title="Cryptocurrency", yaxis_title="24h Change (%)")
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📋 Raw Latest Data")
    st.dataframe(latest_data[["coin_name", "price", "change_24h", "timestamp"]], use_container_width=True)