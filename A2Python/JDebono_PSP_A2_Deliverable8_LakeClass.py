
#JDebono_PSP_A2_Deliverable8_LakeClassProgram.py
#Jennifer Debono
# Nov 2020
#PSP Assignment 2, Deliverable 8
#lake class file to be used with lake class program


class Lake(object):
    """Class for representing lakes"""
    def __init__(self): #initialize function 
        self.Name = "name"
        self.SurfaceArea = 0
        self.Perimeter = 0

    def SDIndex(self, perimeter, area):
    #formula to calculate shoreline development index:
        self.DevelopmentIndex = 0
        