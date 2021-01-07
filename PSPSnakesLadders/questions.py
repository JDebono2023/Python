# A CSV file contains our list of questions in rows and columns
# This program extracts that list and makes it playable
# This allows us to update/modify questions efficiently using CSV
# Creator Honglin (Jim) Wei
# Modified: Dec 4, 2020
#Questions sources: https://www.transum.org/Software/Fun_Maths/Trivia.asp;
#https://icebreakerideas.com/math-trivia/#Number_Trivia; 
#https://www.usefultrivia.com/geography_trivia/index.html;
#https://play.howstuffworks.com/quiz/could-you-pass-this-canadian-geography-quiz

# import the modules necessary for program
import csv
import random

def MultiChoice():
    
    # opening the csv file
    with open('SnakesQs.csv') as csvfile:
        # the csv file reader uses comma as delimiter
        readCSV = csv.reader(csvfile, delimiter=',')
        # generate blank lists to store the question and option variables
        question = []
        option1 = []
        option2 = []
        option3 = []
        option4 = []
        answers = []

        # loops into the csv to pull each column variable into list
        for row in readCSV:
            # column 0 in csv is the question, col 1 is choice A etc.
            Q = row[0]
            A = row[1]
            B = row[2]
            C = row[3]
            D = row[4]
            answer = row[5]
            
            # Puts the variables back into the empty lists with append
            # Then our list will be populated with questions, options and answers
            question.append(Q)
            option1.append(A)
            option2.append(B)
            option3.append(C)
            option4.append(D)
            answers.append(answer)
        
        # closing the csv file
        csvfile.close()

        # We want to know how many questions we have
        length = len(question)
        # An empty list is populated with number of questions
        nums = []
        # populates list from position 1 to length of questions
        # Excluded the header
        nums.extend(range(1,length))
        
        # A counter is set up to count incorrect responses
        # Post test loop 1 begins
        counter = 0
        while counter < 3:
            
            # We shuffle the questions so the questions are random
            random.shuffle(nums)
            
            # The question is always the first question in the nums list
            q = nums[0]

            # Post test loop 2 to handle invalid entries
            while True:
                print("Question: " + question[q])
                print("A) " + option1[q])
                print("B) " + option2[q])
                print("C) " + option3[q])
                print("D) " + option4[q])
                print("Please answer this question using letters A, B, C, D")

                # Prompts user for input
                # Uses conditions to determine correct or incorrect answers
                user_answer = input(">>")
                if user_answer.upper() == answers[q]:
                    print("You've got it!")
                    break # Breaks post test loop 2 if answered successfuly
                
                # Handles in valid responses
                elif user_answer.upper() not in ["A", "B", "C", "D"]:
                    print("I didn't understand your input\n")

                # Bad responses adds 1 to counter
                else:
                    print("Sorry that's not it, try again")
                    counter += 1
                    print("That's strike", counter, "!\n")
                    
                    # Game ending mechanism
                    # When counter is 3, returns variable game to main function
                    # Will break main game post test loop
                    if counter == 3:
                        print("GAME OVER")
                        game = "gameover"
                        return game
            
            # breaks post test loop 1
            break 
                

# Individual testing, should be commented out
# MultiChoice()