# -*- coding: utf-8 -*-

# Import packages
import arcpy

# import utils functions
from util import arcpyPrint, getDissolvedGeometry

# Import config variables
from config import RELATIONAL_DICT as relationalDict


# Define functions
def validate(inputFeature, featureToEraseInput):
    arcpyPrint('MESSAGE', 'Initializing validation...')

    inputFeatureType = arcpy.Describe(inputFeature).shapeType
    featureToEraseInputType = arcpy.Describe(featureToEraseInput).shapeType

    possibleInputTypes = relationalDict[featureToEraseInputType]

    dissolvedEraseGeometry = getDissolvedGeometry(featureToEraseInput)
    dissolvedInputGeometry = getDissolvedGeometry(inputFeature)

    featuresDisjoint = dissolvedInputGeometry.disjoint(dissolvedEraseGeometry)

    if featuresDisjoint:
        message = "The feature classes don't share any geometry relationship."
        return [False, message]

    if not inputFeatureType in possibleInputTypes:
        message = "It's not possible a {} erase a {}".format(featureToEraseInputType, inputFeatureType)
        return [False, message]

    else:
        message = 'Validation process was successfully completed and it can proceed to processing!'
        return [True, message]


def erase(inputFeature, featureToEraseInput, outputFeature):
    arcpy.CopyFeatures_management(inputFeature, outputFeature)
    dissolvedEraseGeometry = getDissolvedGeometry(featureToEraseInput)

    uCursor = arcpy.da.UpdateCursor(outputFeature, 'SHAPE@')
    for row in uCursor:
        row[0] = row[0].difference(dissolvedEraseGeometry)

        uCursor.updateRow(row)

    del uCursor

    message = 'The erase process has been successfully done!'

    return [True, message]




