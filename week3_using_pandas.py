#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:13:19 2025

@author: vivekmadhav
"""

import pandas as pd

df = pd.read_csv("concrete_data.csv")
print("\nOriginal DataFrame:\n", df)

df["Strength (Mpa)"] *= 1.05
df_sorted = df.sort_values(by="Strength (Mpa)", ascending=False)

df_sorted.to_csv("updated_concrete_data_pandas.csv", index=False)
print("\nUpdated CSV file saved as 'updated_concrete_data_pandas.csv'.")
