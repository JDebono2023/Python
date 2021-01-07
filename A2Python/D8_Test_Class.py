

import math

class Lake(object):
    """Class for representing lakes"""
    def __init__(self, name, area, perimeter): #initialize function 
        self.Name = name
        self.SurfaceArea = float(area)
        self.Perimeter = float(perimeter)

    def SDIndex(self):
    #formula to calculate shoreline development index:
        sdi = self.DevelopmentIndex / (2*(math.sqrt(math.pi/self.area)))
        return sdi