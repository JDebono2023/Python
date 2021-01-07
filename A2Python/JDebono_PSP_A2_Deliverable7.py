#JDebono_PSP_A2_Deliverable7.py
#Jennifer Debono
# Nov 2020
#PSP Assignment 2, Deliverable 7
# Program to display a menu of restaurant options and get the user’s choice
# A dictionary of menu categories and options for each category will be used
print()
print("Welcome to Jenn's Tasty Stuff")
print("Here is our menu!")
print()
# Task 1: Create a variable named category and assign the variable a list containing a
# minimum of 3 menu categories (breakfast, lunch, dinner, snack, …)
category = ["Breakfast", "Lunch", "Dinner", "Dessert"] 
# Task 2: Create a variable named categoryOptions 
# assign the variable # lists of options for each category.  
categoryOptions = [["Eggs", "Oatmeal","Smoothie"], ["Tofu Stir Fry", "Quinoa Bowl", "Pasta Salad"],\
                  ["Cheese Burger", "Tempeh and Veggies"], ["Fruit Bowl", "Cheesecake"]]
# Task 3: Create an empty dictionary
orderOption = {} 
counter = 0
# Task 4: use category and category options to populate list
# Task 4.1: use dictionary list in a loop to print manu options
for i in category:
    orderOption[category[counter]] = categoryOptions[counter]
    counter +=1
    print ("Meal: " + str(i) + " Options: " + str(orderOption[i]))
# Task 5: Ask the user which category they would like to order from and get their
print()
print("We like to fill you up!")
print()
selection = input("Please choose a meal type: Breakfast, Lunch, Dinner or Dessert ")
# Task 6: Based on the user’s choice of menu category, use a loop and the dictionary
# Task 7: Ask the user which category option they would like to order and get their
# Display the user’s choice of category option
if selection == "Breakfast":
    selection = "Breakfast"
elif selection == "Lunch":
    selection = "Lunch"
elif selection == "Dinner":
    selection = "Dinner"
elif selection == "Dessert":
    selection = "Dessert"
print()
print("Thanks for choosing ", selection)
