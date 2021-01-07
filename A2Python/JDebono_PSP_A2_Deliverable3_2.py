# Name: JDebono_PSP_A2_Deliverable3_2.py
# Jennifer Debono
# Nov 2020
# Deliverable 3, Question 2
# code to use AddGeometryAttributes tool
# adding perimeter (in KM) and centroid to lakes.shp
# adding coordinate_syetem as: Canada Lambert Conformal Conic to lakes.shp

# import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = r"D:\Fleming\GEOM067\WeelyWork\Week10\AutomationData\CANADA"
arcpy.env.outputCoordinateSystem = arcpy.Describe("lakes.shp").spatialReference
env.overwriteOutput = True

# set variables for perimeter attributes
Input_Features = "lakes.shp" # input feature to be update
Geometry_Properties_P = "PERIMETER_LENGTH_GEODESIC"
Length_Unit = "Kilometers"
Area_Unit = ""
Coordinate_System = "102002" # Canada Lambert Conformal Conic is ESRI code: 102002
# Generate the extent coordinates using Add Geometry Properties tool
arcpy.AddGeometryAttributes_management(Input_Features, Geometry_Properties_P, Length_Unit, Area_Unit, Coordinate_System)

# set variables for centroid
Input_Features = "lakes.shp" # input feature to be update
Geometry_Properties_C = "CENTROID"
Length_Unit = "Kilometers"
Area_Unit = ""
Coordinate_System = "102002" # Canada Lambert Conformal Conic is ESRI code: 102002
# Generate the extent coordinates using Add Geometry Properties tool
arcpy.AddGeometryAttributes_management(Input_Features, Geometry_Properties_C, Length_Unit, Area_Unit, Coordinate_System)

print("Done")