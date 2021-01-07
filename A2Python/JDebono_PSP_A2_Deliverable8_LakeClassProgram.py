#JDebono_PSP_A2_Deliverable8_LakeClassProgram.py
#Jennifer Debono
# Nov 2020
#PSP Assignment 2, Deliverable 8
#program to create a new Lake class
#user to input lake name, surface area and perimeter
#input to be used to calculate Development Index,
#lake shape (is it round) determined by Development Index (index value of 1=round)

import math
from JDebono_PSP_A2_Deliverable8_LakeClass import Lake


#2. In a code or form module, define an object
#variable (myDog) which is type “Dog” and
#instantiate (assign it) a new “Dog” object
myLake = Lake()

#b.	Create’s the lake object with the name specified by the user and assigns the lake object the surface area and perimeter specified by the user
myLake.Name = input("Enter the lake name: ")
myLake.SurfaceArea = float(input("Enter surface area of the lake: "))
myLake.Perimeter = float(input("Enter perimeter of the lake: "))

#c.	Determines the lake’s shoreline development index using the SDIndex method
myLake.DevelopmentIndex = myLake.Perimeter/(2*(math.sqrt(math.pi*myLake.SurfaceArea)))


#e.	Displays the lake’s name, shoreline development index and whether it is a round lake or not
aMsg = "DevelopmentIndex: " + str(myLake.DevelopmentIndex)
print(aMsg)

#d.	Determines whether the lake is a round lake or not.  A round lake has a shoreline development index of 1.
if myLake.DevelopmentIndex == 1:
    print("The lake " + myLake.Name + " with a shoreline development of " + str(myLake.DevelopmentIndex) + " is round.")
else:
    print("The lake " + myLake.Name + " with a shoreline development of " + str(myLake.DevelopmentIndex) + " is not round.")

