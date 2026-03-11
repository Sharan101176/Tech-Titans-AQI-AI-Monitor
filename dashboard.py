import streamlit as st
import pandas as pd
import datetime

# 1. Page Setup (Clean, Simple, Light Theme)
st.set_page_config(page_title="Hyper-Local AQI & AI Mitigation Dashboard", layout="wide")

st.title("🌍 Smart City AQI & AI Source Mitigation Dashboard")
st.write("Live Monitoring & Dynamic Policy Dispatch System (Phase 1 Mockup)")
st.divider()

# 2. Top-Level Metrics (City-Wide Overview)
st.header("📊 City-Wide Overview")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("City Average AQI", "185", "-12 from yesterday")
col2.metric("Critical Ward Hotspots", "3", "Action Required", delta_color="inverse")
col3.metric("Total Automated Actions Today", "14", "+2 since last hour")
# Metrics from your Scaling & Cost Analysis image
col4.metric("Active Nodes (Delhi Scale)", "1,750 / 1,750", "100% Online")
col5.metric("Cost Savings vs. CAAQMS", "~₹700 Cr", "99.9% Savings")

st.divider()

# 3. Zonal Performance & Scaling Panel
zone_col, scaling_col = st.columns([1.5, 1])

with zone_col:
    st.header("📍 Zonal (Quarter) AQI Breakdown")
    st.write("Tracking average pollution levels across different city quarters.")
    
    # Corrected line: Removed the typo inside the brackets!
    zone_data = pd.DataFrame({
        "City Quarter": ["North Zone", "South Zone", "East Zone", "West Zone", "Central District"],
        "Average AQI": [145, 110, 210, 165, 190] 
    })
    
    # Display a clean, simple bar chart natively in Streamlit
    st.bar_chart(zone_data.set_index("City Quarter")["Average AQI"])

with scaling_col:
    st.header("📈 Delhi-Scale Economy & Scaling")
    st.write("Cost analysis from our IoT network proposal vs. traditional CAAQMS infrastructure.")
    
    # Economy data from your cost comparison image
    scaling_data = pd.DataFrame({
        "Metric": ["Total Wards (MCD)", "Total Nodes (Full City)", "Total Deployment Cost", "Traditional CAAQMS Equivalent", "Cost Reduction"],
        "Value": ["250", "1,750", "₹1.1 Crore", "₹700+ Crore", "99.9%"]
    })
    st.dataframe(scaling_data, hide_index=True, use_container_width=True)

st.divider()

# 4. Detailed Ward-Wise Analysis (Core ML Logic & Mitigation)
st.header("🏢 Detailed Ward-Wise Analysis")
st.write("Real-time sensor data and AI-detected pollution sources with corresponding dynamic policies.")

# Your specific data, expanded to show standard features
ward_data = {
    "Ward Number": ["Ward 12", "Ward 07", "Ward 19", "Ward 42", "Ward 55"],
    "AQI": [220, 280, 160, 95, 115],
    "Classification": ["Unhealthy (>200)", "Unhealthy (>200)", "Poor", "Good", "Satisfactory"],
    "PM 2.5 (µg/m³)": [87, 134, 95, 35, 40],
    "PM 10 (µg/m³)": [210, 160, 175, 50, 60],
    "Ratio (PM2.5/PM10)": [0.41, 0.84, 0.54, 0.70, 0.66],
    "AI Detected Source": ["🏗️ Construction Dust", "🔥 Biomass Burning", "🚗 Heavy Traffic", "✅ Normal", "✅ Normal"],
    "Automated Policy Dispatched": ["Admin SMS (Halt Site Work)", "Citizen SMS (Masks Required)", "Reroute Advisory (Heavy Vehicles)", "None", "None"],
    "Mitigation Action Log": [
        "Water cannons activated on-site (Site 12A).",
        "One-way traffic rule enforced. Drone dispatched for fire check.",
        "API triggered detour routing for heavy vehicles.",
        "None",
        "None"
    ]
}

# Convert to Pandas DataFrame and display as a clean table
df_wards = pd.DataFrame(ward_data)
st.dataframe(df_wards, use_container_width=True, hide_index=True)

st.divider()

# 5. Active Mitigations & Performance Log (Specific Actions derived from images)
st.header("⚡ Active Mitigations & Real-Time Defense Log")
st.write("Dynamic responses triggered by the AI system based on real-time data and policy templates.")

now = datetime.datetime.now()
one_hour_ago = now - datetime.timedelta(hours=1)
two_hours_ago = now - datetime.timedelta(hours=2)
three_hours_ago = now - datetime.timedelta(hours=3)

# Log actions based on your provided data and policy images
st.error(f"🕒 {one_hour_ago.strftime('%H:%M %p')} - Admin Alert (Construction Dust): Halt work SMS sent for Ward 12. Water cannons activated at Site #12A (Treated sewage water).")
st.error(f"🕒 {two_hours_ago.strftime('%H:%M %p')} - Citizen Alert (Health Advisory): Masks required in Ward 07 (AQI 280). One-way traffic rule enforced on MG Road corridor.")
st.error(f"🕒 {three_hours_ago.strftime('%H:%M %p')} - Reroute Advisory (Heavy Traffic): API detour triggered for all heavy vehicles around Ward 19 junction.")
st.warning("General Policy: Precision Planting dispatch: 50 pollution-absorbing trees and 2 moss wall units sent to Ward 21 hotspot.")
st.warning("General Policy: Immediate inspection conducted at Site #44 in Ward 12 as AQI value > 200.")
st.success("General Policy: Weekly ward performance bonus awarded to Ward 44 (Best Improved AQI).")
st.success("System: Morning diagnostic complete. All 1,750 sensors across Delhi are online and calibrated.")

st.divider()

# 6. Ward Performance Ranking (Powerful New Feature)
st.header("🏆 Ward Rankings (Weekly)")
st.write("Ranking wards based on AQI and overall improvement, motivating citizens and workers.")
col_ranks1, col_ranks2 = st.columns(2)
with col_ranks1:
    st.subheader("Top 5 Best Performing Wards")
    rank_data1 = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "Ward": ["Ward 44", "Ward 18", "Ward 31", "Ward 03", "Ward 50"],
        "AQI Improvement (%)": ["+35%", "+28%", "+22%", "+19%", "+16%"],
        "Weekly Score": [98, 92, 88, 85, 82]
    })
    st.dataframe(rank_data1, hide_index=True, use_container_width=True)

with col_ranks2:
    st.subheader("Top 5 Critical Wards (Last Week)")
    rank_data2 = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "Ward": ["Ward 07", "Ward 12", "Ward 19", "Ward 21", "Ward 35"],
        "Average AQI": [270, 240, 210, 195, 180],
        "Status": ["Critical", "Unhealthy", "Unhealthy", "Poor", "Poor"]
    })
    st.dataframe(rank_data2, hide_index=True, use_container_width=True)

st.divider()
st.caption("*This is a Phase 1 system mockup with simulated real-time data.*")
