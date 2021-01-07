# JDebono_PSP_A2_Deliverable2.py
# Created by: Jennifer Debono
# Nov 2020
# Calculates the speed of sound in salt water for a whale
# Uses the pressures of the temperature of the water (in degrees C), the depth of the whale (in metres)
# Assumes assumes salinity of the water is 35 PSA
# Calculates the position of a whale in water from a baseline between two hydrophones
# uses distance between hydrphones (in metres), speed of sound (m/s) and time difference (in seconds)
# speed of sound data taken from program calulations and not user input
# Inputs retrieved from whaledata.csv
# Outputs written to csv

import csv
import math
#function to calculate whale position (angle)
def CalcAngle (timeDifference, sos, hydrophoneDist): #pass thru variables for time, speed of sound and distance
    whaleAngle = math.degrees(math.cos((timeDifference * sos) / hydrophoneDist)**1)
    return whaleAngle

#function to calulate speed of sound
def CalcSpeed (waterTemp, whaleDepth): #pass thru variables for temperature and depth
    soundSpeed = 1448.96 + (4.591 * (waterTemp)) - ((5.304 * (10**-2)) * (waterTemp**2)) \
    + ((2.374 * (10**-4)) * (waterTemp**3)) + ((1.63 * (10**-2)) * whaleDepth) \
    + ((1.675 * (10**-7)) * (whaleDepth**2)) - ((7.139 * (10**-13)) * waterTemp * (whaleDepth**3))
    return soundSpeed

def main():
    print("This application calculates the speed of sound in salt water")
    print("This application aslo calulates the depth of a whale in metres")
    print("Assumption:  salinity is 35 PSA")
    print()
    print('************************************************************') 
    print()

    #################### Start of input ########################

    input_temperature =  []        			            # create empty list for temperature
    input_depth = []                   	                # create empty list for depth
    input_time = []                                     # create empty list for time difference
    input_distance = []                                 # create empty list for distance between hydrophones

    fo = open("whaledata.csv", "r")
    freader = csv.reader(fo)
    next(fo)
    for line in freader:
        input_temperature.append(float(line[0]))
        input_depth.append(float(line[1]))
        input_time.append(float(line[2]))
        input_distance.append(float(line[3]))
    fo.close()

    ############### End of input, Start of calculations ################

    # speedsound list to hold calculated results
    calc_speedsound = []   
    # whaleAngle list to hold calulated results           		                
    calc_anglewhale = []

    # For each data set, calculate speed sound and add to speedsound list
    # For each data set, calculate whale angle and add to whaleAngle list
    for index in range(len(input_depth)):   
        temperature = input_temperature[index]    # retrieve temperature in index position from input_temperature list
        depth = input_depth[index]                # retrieve depth in index position from input_depth list
        time = input_time[index]
        distance = input_distance[index]
                    
    speedsound = CalcSpeed(temperature, depth) #CALL FUNCTION HERE FOR CALCULATION 
    calc_speedsound.append(speedsound)        # add speedsound to calc_speedsound list
        
    anglewhale = CalcAngle(time, speedsound, distance) #call function for angle calc
    calc_anglewhale.append(anglewhale) # add whaleAngle to calc_whaleAngle list

    ############## End of calculations, Start of output #################

    print("--------------------------------------------------------------------------------------------")
    print()
    # Display column header line
    headings = ["Temp(C)", "Depth(m)", "Sound/Speed(m/s)", "Time Difference(s)", "HP Distance(m)", "Whale Angle (deg)"]
    newFile = []
    newFile.append(headings)
    writeFile = open(r"whaledata.csv", "w")
    fwriter = csv.writer(writeFile)
    for index in range(len(input_depth)):
        writeList = [input_temperature[index], input_depth[index], calc_speedsound[index], input_time[index], input_distance[index], calc_anglewhale[index]]
        newFile.append(writeList)
    fwriter.writerows(newFile)
    
    print() #used for spacing purposes
    print("Done")

if __name__ == '__main__':
    main() 