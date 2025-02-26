#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:27:21 2025

@author: vivekmadhav
"""

import pandas as pd
import json

sensor_data = {
    "timestamp": ["2025-02-26 10:00", "2025-02-26 11:00", "2025-02-26 12:00"],
    "sensor_id": ["S-101", "S-101", "S-101"],
    "temperature (C)": [22.5, 23.0, 23.2],
    "humidity (%)": [45.0, 44.5, 44.3],
    "predicted_strength (MPq": [26.0, 27.2, 28.1]
}

df_sensors = pd.DataFrame(sensor_data)
df_sensors.to_csv("sensor_readings.csv", index=False)
print("\nSample 'sensor_readings.csv' created.")

df = pd.read_csv("sensor_readings.csv")

#Convert to Json
df = pd.read_csv("sensor_readings.csv")

df.to_json("sensor_readings.json", orient="records", indent=4)
print("\nSensor readings converted to JSON and saved as 'sensor_readings.json'.")

# Load JSON data
with open("sensor_readings.json", "r") as file:
    sensor_data = json.load(file)

# Extract data for sensor "S-101" at a specific timestamp
filtered_data = [entry for entry in sensor_data if entry["sensor_id"] == "S-101" and entry["timestamp"] == "2025-02-26 11:00"]

print("\nFiltered Sensor Data:", filtered_data)