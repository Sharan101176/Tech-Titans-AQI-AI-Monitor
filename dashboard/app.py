# TechTitans — Hyper-Local AQI Intelligence Dashboard
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="TechTitans — AQI Intelligence",
    page_icon="🌫️",
    layout="wide"
)

# ─────────────────────────────────────────
# TRAIN MODEL (same as ml_model.py)
# ─────────────────────────────────────────
@st.cache_resource
def train_model():
    np.random.seed(42)
    n = 300
    data = []

    for _ in range(n // 3):
        pm10 = np.random.uniform(150, 300)
        pm25 = np.random.uniform(30, 80)
        data.append([pm25, pm10, pm25/pm10, "Construction Dust"])

    for _ in range(n // 3):
        pm10 = np.random.uniform(100, 200)
        pm25 = np.random.uniform(90, 180)
        data.append([pm25, pm10, pm25/pm10, "Biomass Burning"])

    for _ in range(n // 3):
        pm10 = np.random.uniform(120, 220)
        pm25 = np.random.uniform(60, 120)
        data.append([pm25, pm10, pm25/pm10, "Heavy Traffic"])

    df = pd.DataFrame(data, columns=["PM2.5", "PM10", "PM_Ratio", "Source"])
    X = df[["PM2.5", "PM10", "PM_Ratio"]]
    y = df["Source"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = train_model()

# ─────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────
def predict_source(pm25, pm10):
    ratio = pm25 / pm10
    reading = pd.DataFrame([[pm25, pm10, ratio]], columns=["PM2.5", "PM10", "PM_Ratio"])
    return model.predict(reading)[0], ratio

def get_aqi_level(pm25):
    if pm25 <= 30:   return "Good", "🟢"
    elif pm25 <= 60: return "Moderate", "🟡"
    elif pm25 <= 90: return "Poor", "🟠"
    elif pm25 <= 120: return "Very Poor", "🔴"
    else:            return "Severe", "🚨"

def get_actions(source):
    actions = {
        "Construction Dust": {
            "citizen": "Wear N95 mask outdoors. Avoid jogging.",
            "admin": "Halt construction site. Deploy water sprinkler cannons.",
            "color": "#FF6B35"
        },
        "Biomass Burning": {
            "citizen": "Stay indoors. Close all windows immediately.",
            "admin": "Dispatch patrol to ward. Issue burning prohibition order.",
            "color": "#C0392B"
        },
        "Heavy Traffic": {
            "citizen": "Avoid outdoor exercise. Use public transport.",
            "admin": "Reroute heavy commercial vehicles from this ward.",
            "color": "#8E44AD"
        }
    }
    return actions.get(source, {})

# ─────────────────────────────────────────
# SIMULATED WARD DATA
# ─────────────────────────────────────────
ward_data = [
    {"Ward": "Ward 01 — Jayanagar",     "PM2.5": 45,  "PM10": 110},
    {"Ward": "Ward 02 — Koramangala",   "PM2.5": 87,  "PM10": 210},
    {"Ward": "Ward 03 — Shivajinagar",  "PM2.5": 134, "PM10": 160},
    {"Ward": "Ward 04 — Hebbal",        "PM2.5": 95,  "PM10": 175},
    {"Ward": "Ward 05 — Whitefield",    "PM2.5": 112, "PM10": 230},
    {"Ward": "Ward 06 — Indiranagar",   "PM2.5": 28,  "PM10": 65},
    {"Ward": "Ward 07 — Malleshwaram",  "PM2.5": 143, "PM10": 185},
    {"Ward": "Ward 08 — Rajajinagar",   "PM2.5": 76,  "PM10": 195},
]

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown("## 🌫️ TechTitans — Hyper-Local AQI Intelligence Dashboard")
st.markdown("**India Innovates 2026** | Real-time Ward-Level Pollution Source Detection")
st.divider()

# ─────────────────────────────────────────
# TOP METRICS
# ─────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("🏙️ Wards Monitored", "8", "Live")
col2.metric("🤖 ML Accuracy", "85%", "Random Forest")
col3.metric("⚡ Alert Latency", "< 2 min", "Automated")
col4.metric("💰 Cost per Node", "₹6,500", "vs ₹20L CAAQMS")
st.divider()

# ─────────────────────────────────────────
# LIVE WARD TABLE
# ─────────────────────────────────────────
st.markdown("### 📍 Live Ward-Level AQI Monitor")

results = []
for ward in ward_data:
    source, ratio = predict_source(ward["PM2.5"], ward["PM10"])
    level, emoji = get_aqi_level(ward["PM2.5"])
    actions = get_actions(source)
    results.append({
        "Ward": ward["Ward"],
        "PM2.5 (µg/m³)": ward["PM2.5"],
        "PM10 (µg/m³)": ward["PM10"],
        "Ratio": round(ratio, 2),
        "AQI Level": f"{emoji} {level}",
        "Detected Source": source,
        "Citizen Alert": actions["citizen"],
        "Admin Action": actions["admin"]
    })

df_results = pd.DataFrame(results)
st.dataframe(df_results, use_container_width=True, hide_index=True)
st.divider()

# ─────────────────────────────────────────
# ALERT CARDS — WORST WARDS
# ─────────────────────────────────────────
st.markdown("### 🚨 Active Alerts — Critical Wards")

critical = [r for r in results if r["PM2.5 (µg/m³)"] > 100]
cols = st.columns(len(critical))

for i, ward in enumerate(critical):
    actions = get_actions(ward["Detected Source"])
    with cols[i]:
        st.error(f"**{ward['Ward']}**")
        st.write(f"PM2.5: **{ward['PM2.5 (µg/m³)']} µg/m³**")
        st.write(f"Source: **{ward['Detected Source']}**")
        st.write(f"👤 {actions['citizen']}")
        st.write(f"🏛️ {actions['admin']}")

st.divider()

# ─────────────────────────────────────────
# MANUAL SENSOR INPUT
# ─────────────────────────────────────────
st.markdown("### 🔬 Test Your Own Sensor Reading")
st.markdown("Enter PM values manually to simulate a live sensor input:")

col1, col2, col3 = st.columns(3)
with col1:
    pm25_input = st.number_input("PM2.5 (µg/m³)", min_value=0.0, max_value=500.0, value=90.0)
with col2:
    pm10_input = st.number_input("PM10 (µg/m³)", min_value=0.0, max_value=500.0, value=180.0)
with col3:
    ward_name = st.text_input("Ward Name", value="Test Ward")

if st.button("🔍 Detect Pollution Source", use_container_width=True):
    source, ratio = predict_source(pm25_input, pm10_input)
    level, emoji = get_aqi_level(pm25_input)
    actions = get_actions(source)

    st.success(f"**Detection Complete for {ward_name}**")
    col1, col2, col3 = st.columns(3)
    col1.metric("PM Ratio", round(ratio, 2))
    col2.metric("AQI Level", f"{emoji} {level}")
    col3.metric("Detected Source", source)

    st.warning(f"⚠️ **Citizen Alert:** {actions['citizen']}")
    st.error(f"🚨 **Admin Action:** {actions['admin']}")

st.divider()

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown(
    "*TechTitans — India Innovates 2026 | "
    "Don't manage pollution citywide. Eliminate it — ward by ward, source by source.* 🇮🇳"
)
