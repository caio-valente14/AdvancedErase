# -*- coding: utf-8 -*-

# Import packages
import arcpy
import os
import sys
import traceback

# Import config variables
from config import MEMORY_FOLDER as memoryFolder

# Define utils functions
def getFormattedException():
    excType, excValue, excTb = sys.exc_info()

    formattedException = traceback.format_exception(excType, excValue, excTb)

    return '\n'.join(formattedException)


def arcpyPrint(type, message):
    if type == 'WARNING':
        arcpy.AddWarning(message)
        arcpy.AddMessage(u'\u200B')

    elif type == 'ERROR':
        arcpy.AddError(message)
        arcpy.AddMessage(u'\u200B')

    elif type == 'MESSAGE':
        arcpy.AddMessage(message)
        arcpy.AddMessage(u'\u200B')

    else:
        raise Exception('There are only 3 options for type argument:\n "ERROR", "WARNING" and "MESSAGE"\n')


def getDissolvedGeometry(featureClass):
    outputDissolve = os.path.join(memoryFolder, 'outDissolve')
    arcpy.Dissolve_management(featureClass, outputDissolve)

    sCursor = arcpy.da.SearchCursor(outputDissolve, 'SHAPE@')

    for row in sCursor:
        geometry = row[0]
        break

    del sCursor

    return geometry


