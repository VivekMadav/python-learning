#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:13:25 2025

@author: vivekmadhav
"""

#List Example
sensor_readings = [23.5, 25.0, 22.8]
sensor_readings.append(24.1)
sensor_readings.remove(22.8)
print(sensor_readings)

#Tuple Example
location = (51.5074, -0.1278)
print(location)

#Dictionary Example
sensor_data = {"2025-02-26 10:00": 24.5, "2025-02-26 11:00": 25.1}
print(sensor_data["2025-02-26 10:00"])

#Set Example
materials = {"Cement", "Sand", "Gravel"}
materials.add("Limestone")
materials.remove(("Sand"))
print(materials)
