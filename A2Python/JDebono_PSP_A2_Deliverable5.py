# JDebono_PSP_A2_Deliverable5.py
# Jennifer Debono
# Nov 2020
# PSP Assignment 2, Deliverable 5
# Program for map manipulation as outlined in items a through g below
# a.	Moves the country layer below the Ecities layer
# b.    Add the layer, mjrivers, to the countries GDB and insert it between Ecities and country layers
# c.	Changes the symbology of the cities layer to use the Cross 4 symbol, Equal Interval method, 4 classes and the POP_RANK field instead of the PORT_ID field.
# d.	Changes the title to say “Population Ranks in Europe”
# e.	Moves the legend in line with the left side of the map
# f.	Adds your name to the credits
# g.	Exports the layout to a pdf with your login name followed by Europe

#############################################################################################################################

# a.	Moves the country layer below the Ecities layer
# Import arcpy module
import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\Question5.aprx")   # path parameter to reference map location
m = aprx.listMaps("Map")[0]                    # return the list of map objects in the project
rLyr = m.listLayers("ECities")[0]          # Assign reference layer to a variable with Index position
mLyr = m.listLayers("country")[0]         # Assign layer to be moved to a variable with Index position
m.moveLayer(rLyr, mLyr, "BEFORE")     # Identify move location of the move layer
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5A_JD.aprx") # Save new .aprx copy to not overwrite orig for reference
del aprx                                       # remove project lock

###############################################################################################################################

# b.    Add the layer, mjrivers, to the countries GDB and insert it between Ecities and country layers
# Import arcpy module
import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5A_JD.aprx")   # path parameter to reference map location
m = aprx.listMaps("Map")[0]                    # return the list of map objects in the project
rLyr = m.listLayers("ECities")[0]              # Assign reference layer to a variable with Index position
lyr = arcpy.mp.LayerFile(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\mjrivers.lyrx")  # Set Layer file to insert into map
m.insertLayer(rLyr, lyr,"AFTER")                  # Add the layer and order after reference Layer
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5B_JD.aprx")   # Save a copy
del aprx                                       # remove project lock


# ###############################################################################################################################

# c.	Changes the symbology of the cities layer to use the Cross 4 symbol, Equal Interval method, 4 classes and the POP_RANK field instead of the PORT_ID field.

import arcpy  # import arcpy
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5B_JD.aprx") # path parameter to reference map location
m = aprx.listMaps("Map")[0]                    # return the list of map objects in the project
lyrs = m.listLayers()                           # variable assigned to check layer symbology
for lyr in lyrs:
    sym = lyr.symbology
    if lyr.isFeatureLayer:
        if hasattr(sym, "renderer"):
            print(lyr.name + ": " + sym.renderer.type) # symbology types: Ecities: GraduatedColoursRenderer, mjrivers & country: SimpleRender

lyr = m.listLayers("ECities")[0]              # identify layer to modify
sym = lyr.symbology                           # create symbology object

if lyr.isFeatureLayer and hasattr(sym, "renderer"):
    sym.renderer.classificationField = "POP_RANK"
    sym.renderer.classificationMethod = "EqualInterval"
    sym.renderer.breakCount = 4
    lyr.symbology = sym        # apply symbology changes to the layer
if hasattr(sym, "renderer"):
    if sym.renderer.type == ("GraduatedColoursRenderer"):
        sym.UpdateRenderer("GraduatedSymbolsRenderer") # Change symbols from graduated colours to symbols
        symTemp = sym.renderer.symbolTemplate
        symTemp = sym.renderer.applySymbolFrontGallery("Cross 1")
        sym.renderer.updatesSymbolTemplate (symTemp)
        sym.renderer.minimumSymbolSize = 5
        sym.renderer.maximumSymbolSize = 20
        lyr.symbology = sym        # apply symbology changes to the layer
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5C_JD.aprx")   # Save a copy in aprx
del aprx 

# ###############################################################################################################################

#d.	Changes the title to say “Population Ranks in Europe”

import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5C_JD.aprx")   # path parameter to reference map location
m = aprx.listMaps("Map")[0]                               # return the list of map objects in the project
lyt = aprx.listLayouts("Layout")[0]                       # Set the map layout
TitleElm = lyt.listElements("TEXT_ELEMENT", "Title")[0]   # List elements will be assigned to the varable elements of the layout
TitleElm.text = "Population Ranks in Europe"              # change map title
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5D.aprx")   # Save a copy in aprx
del aprx                                                  # delete aprx

# ###############################################################################################################################

# # e.	Moves the legend in line with the left side of the map

import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5D.aprx")   # path parameter to reference map location
lyt = aprx.listLayouts("Layout")[0]                # set map Layout
legend = lyt.listElements("LEGEND_ELEMENT", "Legend")[0]  # Assign list elemnts to legend element  
mf = legend.mapFrame                               # Set to map frame if MOVING something                            
legend.elementPositionX = mf.elementPositionX = 0  # align to left
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5E.aprx")   # Save a copy in aprx
del aprx 

# ###############################################################################################################################

# # f.	Adds your name to the credits

import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5E.aprx")   # path parameter to reference map location
lyt = aprx.listLayouts("Layout")[0]                          # Set the map layout
CreditsElm = lyt.listElements("TEXT_ELEMENT", "Cred*")[0]   # List elements will be assigned to the variable elements of the layout
CreditsElm.text = "Credits: J. Debono"                       # Credit with myname
aprx.saveACopy(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5F.aprx")   # Save a copy in aprx
del aprx                                                     # delete aprx

# ###############################################################################################################################

# # g.	Exports the layout to a pdf with your login name followed by Europe

import arcpy                                   
aprx = arcpy.mp.ArcGISProject(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\A2_Question5F.aprx")   # path parameter to reference map location
lyt = aprx.listLayouts("Layout")[0] # identify the layout to be printed to PDF
lyt.exportToPDF(r"D:\Fleming\GEOM067\Assignments\JDebono_GEOM67_Assignment2\jdebono_Europe.pdf") #print to pdf