[README.md](https://github.com/user-attachments/files/25915520/README.md)
# 🌫️ TechTitans — Hyper-Local AQI Intelligence System
### India Innovates 2026

---

## 👥 Team Members
| Name | Affiliation |
|---|---|
| Santosh Ryaka | Vidyavardhaka College of Engineering |
| Sharan Kumar K S | Vidyavardhaka College of Engineering |
| Shashidhar S Hugar | Vidyavardhaka College of Engineering |
| Shishir Gowda S | Vidyavardhaka College of Engineering |
| Shravanth Kumar M | Vidyavardhaka College of Engineering |
| Shreesha Nagendra Gowda | Vidyavardhaka College of Engineering |

---

## 🚨 Problem Statement
Urban air quality monitoring relies on macro-level, city-wide AQI averages — failing to detect hyper-local pollution spikes at the ward level. With fewer than 800 CAAQMS stations across 640,000+ Indian wards, granular source attribution remains impossible. Administrators cannot pinpoint emission sources — whether construction particulates, biomass combustion, or vehicular exhaust — and citizens receive no localized health advisories.

---

## 💡 Solution
An end-to-end, ward-wise AI dashboard that:
- **Detects** — Dense IoT sensor network capturing PM2.5 & PM10 at street level
- **Analyzes** — ML classifier identifies pollution source from particle ratios
- **Acts** — Auto-generates ward-specific health advisories and admin policy triggers

---

## 🏗️ System Architecture
```
SPS30 Sensor
     ↓
ESP32 Microcontroller (JSON packaging)
     ↓
Firebase Realtime Database (via MQTT)
     ↓
Python Backend (data processing)
     ↓
Random Forest ML Classifier
     ↓
Streamlit Dashboard (Ward map + AQI levels + Alerts)
```

---

## 🤖 ML Model — Pollution Source Classification

| PM Ratio | Detected Source | Citizen Alert | Admin Action |
|---|---|---|---|
| < 0.5 | Construction Dust | Wear N95 mask | Halt site, deploy water cannons |
| > 0.8 | Biomass Burning | Stay indoors | Dispatch patrol, shutdown site |
| 0.5–0.7 | Heavy Traffic | Avoid outdoor exercise | Reroute heavy vehicles |
| Low both | Clean Air | No action needed | Continue monitoring |

---

## 📁 Project Structure
```
TechTitans-AQI/
│
├── ml/
│   └── pollution_classifier.py   # Random Forest ML model
│
├── data/
│   └── sensor_data.csv           # Simulated sensor readings
│
├── dashboard/
│   └── (Streamlit dashboard — in progress)
│
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚙️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/TechTitans-AQI.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the ML classifier demo
python ml/pollution_classifier.py
```

---

## 📊 Coverage & Scale

| | Bengaluru | Delhi |
|---|---|---|
| Total Wards | 225 | 250 |
| Nodes Needed | ~1,125 | ~1,750 |
| Total Cost | ~₹73 Lakh | ~₹1.1 Crore |
| Govt. CAAQMS Equivalent | ₹11 Crore | ₹700+ Crore |

> **1 node covers ~300–500m radius. 1 ward needs only 4–6 nodes.**

---

## 🔧 Tech Stack

| Tool | Purpose |
|---|---|
| ESP32 + SPS30 | IoT Hardware — PM2.5/PM10 sensing |
| Firebase + MQTT | Real-time cloud database |
| Python + Scikit-Learn | ML model — Random Forest Classifier |
| React / Streamlit | Frontend dashboard |

---

## 📚 References
- SPS30 Sensor: https://sensirion.com/products/catalog/SPS30
- CPCB Air Quality: https://cpcb.nic.in
- PM2.5/PM10 Basics (EPA): https://www.epa.gov/pm-pollution/particulate-matter-pm-basics
- BBMP Ward Data: https://bbmp.gov.in
- Scikit-Learn: https://scikit-learn.org
- Firebase: https://firebase.google.com/docs/database
- GRAP Policy: https://caqm.nic.in

---

## 🚧 Current Status

| Component | Status | Notes |
|---|---|---|
| ✅ ML Classifier | **Functional** | 85% accuracy, all 3 sources detected |
| ✅ System Architecture | **Functional** | Full pipeline designed & documented |
| 🔄 Streamlit Dashboard | **In Progress** | Ward map & alert UI under development |
| 🔄 Firebase Integration | **In Progress** | Real-time data pipeline being built |
| ⏳ ESP32 Firmware | **Upcoming** | Hardware prototyping post-selection |
| ⏳ SPS30 Sensor Deployment | **Upcoming** | Field testing planned for Ward pilot |

> Core intelligence layer — ML model and architecture — is complete and working.
> Hardware and full-stack integration actively in progress.

---

*India Innovates 2026 — Fighting pollution, one ward at a time.* 🇮🇳
