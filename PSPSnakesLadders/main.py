# Awesome Snakes & Turtles Game
# Created By: IPGRP2 - J. Debono, K. Perdue, J. Seo, H. Wei
# Date Modified December 04, 2020


# Turtle Library Reference
# https://realpython.com/beginners-guide-python-turtle/

# Imported necessary modules to run the game
# Mini games were split up for individual work
# Mini games are later incorporated to main function via import 
import turtle
from questions import MultiChoice
from CoinFlip import Coinflip
from dice import diceroll
from rockpaperscissors import rps

# This function allows the user to replay the game again
def replay():
    
    # A post test loop used to replay game, variable user is the test condition
    user = ""
    while user.upper() not in ["Y","N"]:

        print("Would you like to play again?")
        user = input("Y/N:\n>>")
        # Simple conditions to rerun the program
        if user.upper() == "Y":
            main()
        elif user.upper() == "N":
            print("See you next time!")
        else: 
            print("Sorry I didn't understand that. Enter 'N' to quit\n")

# Main Function, the actual gameboard and gameplay
def main():

    # A post test loop to check if player fails at any part of the game
    # Game failure mechanism, breaks loop based on imported game return values
    while True:

        # Asks for player name
        Guest = input("\nWelcome to Group 2's Awesome Snakes and Ladders Game\nI'm Turtles, what's your name? >>")
        print ("Welcome", Guest)
        print()

        # Game introduction message
        print("There are a series of questions and 3 minigames")
        print("Help me move through the squares!")
        print()
        print("Each correct answer and win in the game moves me forward")
        print("If you fail 3 times then the game is over! GOOD LUCK")
        print()

        # Background image set up
        screen = turtle.Screen()
        screen.setup(900,600)
        screen.bgpic('boardgamegrid-01.png')

        # initialized turtle object to go to start position
        # gave the turtle its shape and color 
        user = turtle.Turtle()
        user.penup()
        user.goto(-275,185)
        user.shape("turtle")
        user.color("green")

        # Round 1 Game imported from questions
        # Example of returning function value to break loop, if necessary
        # Global settings for post test condition difficult due to import
        if MultiChoice() == "gameover":
            break
        # Moves the turtle object (the player avatar)
        user.forward(275)
        user.shapesize(2,2,1)
        print()

        # Round 2
        if rps() == "gameover":
            break
        user.forward(275)
        user.shapesize(3,3,1)
        print()
        
        # Round 3
        if MultiChoice() == "gameover":
            break
        user.right(85)
        user.forward(190)
        user.right(95)
        user.shapesize(4,4,1)
        print()

        # Round 4
        if diceroll() == "gameover":
            break
        user.forward(275)
        user.shapesize(5,5,1)
        print()

        # Round 5
        print("\nBONUS QUESTION")
        if MultiChoice() == "gameover":
            break
        print("Congrats you move two squares!")
        user.forward(270)
        user.shapesize(6,6,1)

        user.left(80)
        user.forward(190)
        user.left(100)
        user.shapesize(7,7,1)
        print()

        # Round 6
        if Coinflip() == "gameover":
            break
        user.forward(270)
        user.shapesize(8,8,1)
        print()
        
        # Round 7
        if MultiChoice() == "gameover":
            break
        user.forward(270)
        user.shapesize(9,9,1)
        print()

        # Congratulates player through message and on turtle window
        print("\nCongrats Master", Guest, ", you have beaten the game!")
        screen.update()
        screen.bgpic('victory-01.png')

        # Celebration Animation, triggers post test loop break 
        user.left(90)
        user.forward(360)
        user.left(90)
        user.forward(540)
        user.left(90)
        user.forward(360)
        user.left(90)
        user.forward(900)
        break
    
    # Exits the game and calls replay function
    print("Click Game Screen to Exit")
    screen.exitonclick()
    replay()

# main function driver
main()