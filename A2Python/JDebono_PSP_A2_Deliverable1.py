# JDebono_PSP_A2_Deliverable1.py
# Created by: Jennifer Debono
# Nov 2020
# Calculates the speed of sound in salt water for a whale
# Uses the pressures of the temperature of the water (in degrees C), the depth of the whale (in metres)
# Assumes assumes salinity of the water is 35 PSA
# Calculates the position of a whale in water from a baseline between two hydrophones
# uses distance between hydrphones (in metres), speed of sound (m/s) and time difference (in seconds)
# speed of sound data taken from program calulations and not user input
# Inputs entered with keyboard
# Outputs displayed on screen
import csv
import math
import csv
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

    # Obtain temperature and depth for multiple locations, time difference, 
    # and distance between hydrophones from the user
    # while True: 
    #     temperature = float(input("Input the temperature of water in degrees celsius: "))
    #     input_temperature.append(temperature) 			 # add temeprature to input_temperature list
        
    #     depth = float(input("Input the depth in metres: "))
    #     input_depth.append(depth) 			             # add depth to input_depth list
        
    #     time = float(input("Input the time difference in seconds: "))
    #     input_time.append(time) 			             # add time to input_time list
        
    #     distance = float(input("Input the distance between hydrophones in metres: "))
    #     input_distance.append(distance) 			     # add distance to input_distance list

    #     print()
    #     end = input("Do you want to stop entering values (Y/N)? ")
    #     print()
    #     if  end.upper() == 'Y' :
    #         break 
    fo = open("whaledata.csv", "r")
    freader = csv.reader(fo)
    next(fo)
    for line in freader:
        input_temperature.append(float(line[0]))
        input_depth.append(float(line[1]))
        input_time.append(float(line[3]))
        input_distance.append(float(line[4]))
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
    print("Temperature (deg C)\tDepth (m)\tTime Difference (s)\tDistance (m)\t Speed of Sound\t\tDegrees") #createing columns

    # Display temperature, depth, speedsound, time and distance from lists in table format
    
    for index in range(len(input_depth)):
             
      # print temperature, depth, speed sound from lists
        # formatted to two decimals with decimals aligned
        print('\t', format((input_temperature[index]), '.2f'),'\t\t', format((input_depth[index]), '.2f'),'\t\t', format((input_time[index]), '.2f'),'\t\t\t', format((input_distance[index]), '.2f'), '\t\t', format((calc_speedsound[index]), '.2f'), '\t\t', format((calc_anglewhale[index]), '.2f'))

    
    print() #used for spacing purposes
    print("Done")

if __name__ == '__main__':
    main() 