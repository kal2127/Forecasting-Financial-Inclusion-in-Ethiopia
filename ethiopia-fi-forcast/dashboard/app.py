import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- 1. CONFIG & DATA LOADING ---
st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

@st.cache_data
def load_data():
    # Load your processed matrix and forecast data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    forecast_path = os.path.join(project_root, 'data', 'processed', 'forecast_2027.csv')
    
    if os.path.exists(forecast_path):
        return pd.read_csv(forecast_path)
    return None

df_forecast = load_data()

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Inclusion Projections", "Event Impacts"])

# --- 3. PAGE: OVERVIEW ---
if page == "Overview":
    st.title("🇪🇹 Ethiopia Financial Inclusion Overview")
    
    # KPI Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("2024 Baseline", "49%", "Findex Data")
    col2.metric("2027 Target", "60%", "Consortium Goal")
    col3.metric("Current Gap", "-11%", delta_color="inverse")

    st.write("### Historical Progress")
    hist_data = pd.DataFrame({
        "Year": [2011, 2014, 2017, 2021, 2024],
        "Ownership": [22, 22, 35, 46, 49]
    })
    fig = px.line(hist_data, x="Year", y="Ownership", markers=True, title="Account Ownership Over Time")
    st.plotly_chart(fig, use_container_width=True)

# --- 4. PAGE: INCLUSION PROJECTIONS ---
elif page == "Inclusion Projections":
    st.title("📈 2027 Inclusion Projections")
    
    # Scenario Selector
    scenario = st.selectbox("Select Scenario", df_forecast['Scenario'].unique())
    selected_val = df_forecast[df_forecast['Scenario'] == scenario]['2027 Forecast (%)'].values[0]
    
    st.write(f"### Predicted 2027 Rate: **{selected_val}%**")
    
    # Bar Chart comparison
    fig_bar = px.bar(df_forecast, x='Scenario', y='2027 Forecast (%)', 
                     color='Confidence', title="Comparison of 2027 Scenarios")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Download Button
    st.download_button("Download Forecast Data", df_forecast.to_csv(index=False), "forecast_2027.csv")

# --- 5. PAGE: EVENT IMPACTS ---
elif page == "Event Impacts":
    st.title("⚡ Policy & Event Impacts")
    st.write("This section shows how specific events change the national inclusion rate.")
    
    impact_data = pd.DataFrame({
        "Event": ["Fuel Digitization", "M-Pesa Launch", "Fayda Digital ID"],
        "Estimated Boost (%)": [8.0, 4.5, 5.0]
    })
    st.table(impact_data)