

# A brief description of the project
# February 8, 2023
#CTI-110 P1HW2-Travel Expense
#Sarah Perkins
#


print('This program calculates and displays travel expenses')
#Get total budget#
user_budget = int(input('Enter Budget:\n'))
#Get destination#
user_dest = (input('Enter your travel destination:\n'))
#Get gas needed#
user_gas = int(input('How much do you think you will spend on gas?\n'))
#Get cost of hotel stay#
user_hotel = int(input('Approximately, how much will you need for accomodation/hotel?\n'))
#Get cost of food during stay#
user_food = int(input('Last, how much do you need for food?\n'))
#Subtract gas, hotel, and food from total budget to get remaining balance#
user_balance = user_budget - (user_gas + user_hotel + user_food)

#Output expesenses, destination, initial budget and remaining budget#
print('------------Travel Expenses------------')
print('Location:', user_dest)
print('Initial Budget:', user_budget)
print('Fuel:', user_gas)
print('Accomodation:', user_hotel)
print('Food:', user_food)
print('Remaining Balance:', user_balance)