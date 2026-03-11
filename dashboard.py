import streamlit as st
import pandas as pd

# Set up the dashboard title
st.title("🌍 Smart City AQI & AI Source Mitigation Dashboard")
st.write("STATUS: Phase 1 Mockup UI - Waiting for live Firebase Hardware Data")

# Create the data exactly like your presentation table
data = {
    "Ward": ["Ward 12", "Ward 07", "Ward 19"],
    "PM 2.5 (µg/m³)": [87, 134, 95],
    "PM 10 (µg/m³)": [210, 160, 175],
    "Ratio": [0.41, 0.84, 0.54],
    "AI Detected Source": ["🏗️ Construction Dust", "🔥 Biomass Burning", "🚗 Heavy Traffic"],
    "Automated Alert Sent": ["✅ Admin SMS (Halt Work)", "✅ Citizen SMS (Masks)", "✅ Traffic Reroute"]
}

# Convert data into a table
df = pd.DataFrame(data)

# Display the table on the website
st.subheader("Live Ward Monitoring & Automated Actions")
st.dataframe(df, hide_index=True, use_container_width=True)

st.success("System Active: AI Mitigation Rules running normally.")
