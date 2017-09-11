# CTI-110 
# M2HW2 - Tip Tax Total 
# Samuel Blythe
# 9/10/17
#

#Greeting
print('Hello! Lets Calculate your Tip, Tax, and Total!')
print('\n')

#User Input for Meal cost
mealCost = float(input('How much was your meal? $'))

#Tip Calculation
mealTip = float(mealCost *.18)

#Tax Calculation
mealTax = float(mealCost *.07)

#Total Calculation
mealTotal = float(mealCost + mealTip + mealTax)

#Tip Display
print('Tip=$', format(mealTip, ',.2f'))

#Tax Display
print('Tax=$', format(mealTax, ',.2f'))

#Total Display
print('Total=$', format(mealTotal, ',.2f'))


