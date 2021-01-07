#Jeonghyeok Seo
#Rock Paper Scissors minigame
#get user random selection Rock, Paper, or Scissors
#get computer's random selection Rock, Paper, or Scissors
#compare to computer choice
#turtle moves forward if user wins

def rps():
   #Options of Rock, Paper and Scissors

   options = ["Rock", "Paper", "Scissors"]
   attempts = 0

   #Loop if player lose or tie
   #Max 3 attempts allowed 
   while attempts < 3:

      #Get user selection
      user = input("Please choose one form Rock, Paper, and Scissors: ")
      user = user.capitalize()
      print("Player's Choice", user)

      #Error handling when user input other value
      while user.capitalize() not in options:
         print("Incorrect input. Please enter Rock, Paper, or Scissors")
         user = input("Please choose one form Rock, Paper, and Scissors:" )
         user = user.capitalize()
         print("Player's Choice", user)

      #Computer choose one value randomly

      import random
      Computer = random.choice(options)
      print("Computer's choice", Computer)

      #Compare the values
      winner = None

      #When Computer select Rock
      if Computer == "Rock":
         if user == "Scissors":
            winner = "Computer"
         elif user == "Paper":
            winner = "user"   
         else:
            winner == None


      #When Computer select Paper
      elif Computer == "Paper":
         if user == "Rock":
            winner = "Computer"
         elif user == "Scissors":
            winner = "user"
         else:
            winner == None  

      #When Computer select Scissors
      else: 
         if user == "Paper":
            winner = "Computer"
         elif user == "Rock":
            winner = "user"
         else:
            winner == None

      #Print the results

      #If player loose or tie
      attempts += 1
      if winner == "Computer" :
         print("You lose. Try again") 
               
      elif winner == None:
         print("Tied. Try again!")
      
      #If player win
      else:
         print("Congraturations. You win")
         return True

      #Print remaining attempts   
      print(f"You have {3 - attempts} attempts left.")

   #If player didn't win after 3 attempts   
   print("GAME OVER!")
   game = "gameover"
   return game # We don't need this if we are going to use exit code 0