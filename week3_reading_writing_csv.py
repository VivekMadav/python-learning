#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:00:57 2025

@author: vivekmadhav
"""

import csv

#Reading a csv file
with open("concrete_data.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [row for row in reader]
    
print("CSV Data:", data)


#Modifying data
for row in data:
    row[3] = str(round(float(row[3])*1.05,2))
    
#Writing back to a new CSV file
with open("udpated_concrete_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("Updated CSV file saved as 'updated_concrete_data.csv'.")

