# -*- coding: utf-8 -*-

# Import packages
import arcpy

# Arcpy env options
arcpy.env.overwriteOutput = True

# Import functions from functions
from functions import validate, erase

# Import functions from util
from util import getFormattedException, arcpyPrint

# Import inputs
inputFeature = arcpy.GetParameterAsText(0)
featureToEraseInput = arcpy.GetParameterAsText(1)
outputFeatureClass = arcpy.GetParameterAsText(2)

# Import config variables


# Define main function
def main():
    try:
        isValid, message = validate(inputFeature, featureToEraseInput)

        if not isValid:
            raise Exception(message)

        arcpyPrint('MESSAGE', message)

        _, message = erase(inputFeature, featureToEraseInput, outputFeatureClass)

        arcpyPrint('MESSAGE', message)

        return [True, message]

    except:
        formattedException = getFormattedException()

        message = 'There was a problem while running function.\nError:\n{}'.format(formattedException)

        return[False, message]


if __name__ == '__main__':
    runSuccessfully, message = main()

    if not runSuccessfully:
        arcpyPrint('ERROR', message)
