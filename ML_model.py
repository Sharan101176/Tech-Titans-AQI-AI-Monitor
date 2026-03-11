# TechTitans - AQI Pollution Source Classifier
# Team: Santosh Ryaka, Sharan Kumar KS, Shashidhar S Hugar,
#       Shishir Gowda S, Shravanth Kumar M, Shreesha Nagendra Gowda

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ─────────────────────────────────────────
# STEP 1: SIMULATE SENSOR DATA
# (Replace this with real SPS30 sensor data later)
# ─────────────────────────────────────────

np.random.seed(42)
n = 300  # number of samples

def generate_data():
    data = []

    # Construction Dust: High PM10, Low PM2.5, ratio < 0.5
    for _ in range(n // 3):
        pm10 = np.random.uniform(150, 300)
        pm25 = np.random.uniform(30, 80)
        ratio = pm25 / pm10
        data.append([pm25, pm10, ratio, "Construction Dust"])

    # Biomass Burning: High PM2.5, ratio > 0.8
    for _ in range(n // 3):
        pm10 = np.random.uniform(100, 200)
        pm25 = np.random.uniform(90, 180)
        ratio = pm25 / pm10
        data.append([pm25, pm10, ratio, "Biomass Burning"])

    # Heavy Traffic: Both high, ratio ~0.5
    for _ in range(n // 3):
        pm10 = np.random.uniform(120, 220)
        pm25 = np.random.uniform(60, 120)
        ratio = pm25 / pm10
        data.append([pm25, pm10, ratio, "Heavy Traffic"])

    df = pd.DataFrame(data, columns=["PM2.5", "PM10", "PM_Ratio", "Source"])
    return df

# ─────────────────────────────────────────
# STEP 2: TRAIN THE ML MODEL
# ─────────────────────────────────────────

df = generate_data()

X = df[["PM2.5", "PM10", "PM_Ratio"]]
y = df["Source"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ─────────────────────────────────────────
# STEP 3: EVALUATE MODEL
# ─────────────────────────────────────────

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("   TechTitans AQI Source Classifier")
print("=" * 50)
print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ─────────────────────────────────────────
# STEP 4: PREDICT FROM NEW SENSOR READING
# ─────────────────────────────────────────

def predict_source(pm25, pm10):
    ratio = pm25 / pm10
    reading = pd.DataFrame([[pm25, pm10, ratio]], columns=["PM2.5", "PM10", "PM_Ratio"])
    source = model.predict(reading)[0]
    return source, ratio

def get_action(source):
    actions = {
        "Construction Dust": {
            "citizen": "⚠️  Heavy dust detected. Wear N95 mask outdoors.",
            "admin":   "🚨 Deploy water sprinklers. Halt construction site work."
        },
        "Biomass Burning": {
            "citizen": "⚠️  Toxic smoke detected. Stay indoors, close windows.",
            "admin":   "🚨 Dispatch patrol to ward. Issue burning prohibition order."
        },
        "Heavy Traffic": {
            "citizen": "⚠️  High exhaust levels. Avoid outdoor exercise.",
            "admin":   "🚨 Reroute heavy commercial vehicles from this ward."
        }
    }
    return actions.get(source, {})

# ─────────────────────────────────────────
# STEP 5: DEMO — SIMULATE LIVE WARD READINGS
# ─────────────────────────────────────────

print("\n" + "=" * 50)
print("   LIVE WARD SIMULATION")
print("=" * 50)

ward_readings = [
    {"ward": "Ward 12 - Koramangala", "pm25": 87,  "pm10": 210},
    {"ward": "Ward 07 - Shivajinagar", "pm25": 134, "pm10": 160},
    {"ward": "Ward 19 - Hebbal",       "pm25": 95,  "pm10": 175},
]

for reading in ward_readings:
    source, ratio = predict_source(reading["pm25"], reading["pm10"])
    actions = get_action(source)
    print(f"\n📍 {reading['ward']}")
    print(f"   PM2.5: {reading['pm25']} µg/m³ | PM10: {reading['pm10']} µg/m³ | Ratio: {ratio:.2f}")
    print(f"   🔍 Detected Source : {source}")
    print(f"   {actions['citizen']}")
    print(f"   {actions['admin']}")

print("\n" + "=" * 50)
