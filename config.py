# -*- coding: utf-8 -*

# Import packages
import arcpy
import os

# Define config variable
RELATIONAL_DICT = {
    'Polygon': ['Polygon', 'Point', 'Polyline'],
    'Polyline': ['Polyline', 'Point'],
    'Point': ['Point']
}

# Memory folder
productName = arcpy.GetInstallInfo()['ProductName']

if productName == 'ArcGISPro':
    MEMORY_FOLDER = 'memory'

else:
    MEMORY_FOLDER = 'in_memory'



