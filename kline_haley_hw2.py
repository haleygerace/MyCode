# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''
def sales_tax():
	# your code here
	# Variable declaration
	purchase = 0.0
	stateTax = 0.0
	countyTax = 0.0
	totalTax = 0.0
	totalSale = 0.0
	# Constants for state and county tax rates
	STATE_TAX_RATE = 0.05
	COUNTY_TAX_RATE = 0.025
	# Amount of purchase
	purchase = float(input("Enter the amount of purchase: "))
	# Calculate the state sales tax
	stateTax = purchase * STATE_TAX_RATE
	# Calculate the county tax rate
	countyTax = purchase * COUNTY_TAX_RATE
	# Caluclate the total tax
	totalTax = stateTax + countyTax
	# Calculate total sale
	totalSale = purchase + totalTax
	print("Purchase Amount: " + format(purchase, ".2f") + "\n" + "State Tax: " + format(stateTax, ".2f"))
	print("County Tax: " + format(countyTax, ".2f") + "\n" + "Total Tax: " + format(totalTax, ".2f"))
	print("Sale Total: " + format(totalSale, ".2f"))


# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	# your code here
	# Variable Declaration
	acct_bal = 0.0
	principal = 0.0
	interest_rate = 0.0
	coumpounded = 0.0
	years = 0.0
	# Amount of principal
	principal = float(input("Enter the starting principal: "))
	# Annual interest rate paid by the account
	interest_rate = float(input("Enter the annual interest rate: "))
	# Number of times interest in compounded
	compounded = float(input("How many times per year is the interest compounded? "))
	# Number of years
	years = float(input("For how many years will the account earn interest? "))
	# Calculate ammount in account
	acct_bal = principal * (1 + (interest_rate/100)/compounded)**(compounded*years)
	print("Principal Amount: " + str(principal) + "Interest Rate: " + str(interest_rate) + "\n")
	print("At the end of 10 years you will have " + "$" + " " + format(acct_bal, ".2f"))


# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	# your code here
	# Variable declaration
	pennies = 0.0
	nickels = 0.0
	dimes = 0.0
	quarters = 0.0
	# Penny amount
	pennies = float(input("Enter the number of pennies: "))
	# Nickel amount
	nickels = float(input("Enter the number of nickels: "))
	# Dime amount
	dimes = float(input("Enter the number of dimes: "))
	# Quarter amount
	quarters = float(input("Enter the number of quaters: "))

	# Calculate dollar amount
	dollar_amount = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25
	if dollar_amount == 1:
		print('''
		Congradulations!
		The amount you entered was exactly one dollar!
		You win the game!''')
	elif dollar_amount > 1:
		print("Sorry, the amount you entered was more than one dollar.")
	elif dollar_amount < 1:
		print("Sorry, the amount you entered was less than one dollar.")

# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
'''
Enter the number of packages purchased: 10
'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	# your code here
	#Variable Declaration
	packages = 0.0
	discount = 0.0
	discount_amt = 0.0
	total_amt = 0.0
	low = float(99 * 0.1)
	low_med = float(99 * 0.2)
	med = float(99 * 0.3)
	high = float(99 * 0.4)
	pack_low = float(packages * low)
	pack_lowmed = float(packages * low_med)
	pack_med = float( packages * med)
	pack_high = float(packages * high)
	#Number of packages
	packages = float(input("Enter the number of packages purchased: "))
	# Discount
	if packages < 10:
		print("Discount amount: $ 0")
		print("Total Amount: " + "$" + " " + format(packages * 99, ".2f"))
	elif 10 <= packages < 20:
		print("Discount Amount: " + "$ " + format(packages * low, ".2f")) 
		print("Total Amount: " + "$ " + (format(packages * 99 - packages * low, ".2f")))
	elif 20 <= packages < 50:
		print("Discount Amount: " + "$ " + format(packages * low_med, ".2f"))
		print("Total Amount: " + "$ " + (format(packages * 99 - packages * low_med, ".2f")))
	elif 50 <= packages < 100:
		print("Discount Amount: " + "$ " + format(packages * med, ".2f"))
		print("Total Amount: $ " + (format(packages * 99 - packages * med, ".2f")))
	elif packages >= 100:
		print("Discount Amount: $ " + format(packages * high, ".2f"))
		print("Total Amount: $ " + (format(packages * 99 - packages * high, ".2f")))



# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
'''
Enter the weight of the package: 10
'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	# your code here
	# Variable Declaration
	weight = 0.0
	shipping = 0.0
	# Enter weight
	weight = float(input("Enter the weight of the package: "))
	# SHipping charges
	if weight <= 2:
		print("Shipping charge: " + "$ " + format(weight * 1.50, ".2f"))
	elif 2 < weight <= 6:
		print("Shipping charge: " + "$ " + format(weight * 3, ".2f"))
	elif 6 < weight <= 10:
		print("Shipping charge: " + "$ " + format(weight * 4, ".2f"))
	elif weight < 10:
		print("Shipping charge: " + "$ " + format(weight * 4.75, ".2f"))


# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	# your code here
	budget_amount = float(input("Enter amount budgeted for the month: "))

	#get the amount they spent
	spent = float(input("Enter an amount spent(0 to quit): "))

	while spent > 0:
		spent = float(input("Enter an amount spent(0 to quit): "))
		total_spent += spent
		print(total_spent)

		if total_spent < budget_amount:
			print("You are $ " + (budget_amount - total_spent) + " under budget. WELL DONE!")

		elif total_spent == budget_amount:
			print("Spending matches budget. GOOD PLANNING!")

		elif total_spent > budget_amount:
			print("You are $ " + (total_spent - budget_amount) + " over budget. PLAN BETTER NEXT TIME!")


# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	# your code here
	#Variable declaration
	total_inches_rain = 0
	total_months = 0
	# Find years

	number_years = int(input("Enter the number of years: "))

	print("For year " + str(number_years))

	for years in range(1, number_years + 1):
		for current_month in range(1,13):
			rain_amount = float(input("Enter the rainfall for the month: " + format(current_month, "d")))
			total_inches_rain += rain_amount
			total_months += 1

	# Total rainfall 

	total_rain = sum(amount for amount in range(12))

	print(total_rain)

	average_rain = total_inches_rain / total_months

	print("For 12 Months")
	print("Total Rainfall: " + format(total_inches_rain, ".2f") + " inches")
	print("Average Monthly Rainfall: " + format(average_rain, ".2f") + " inches")


# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
'''
Enter a nonnegative integer: 10
'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	# your code here
	# Variable declaration 
	num = 0.0
	fac = 0.0
	# Enter number
	num = int(input("Enter a nonnegative integer: "))
 
	fac = 1
 
	for i in range(1, num + 1):
    	fac = fac * i
 
	print("The factorial of ", num, " is ", fac)


# Exercise 4-12
# PROMPT(S) (Example user input of 'python'):
'''
Enter the string to be converted to Morse code: python
'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	# your code here
	morse_code=	{ 'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ', ':'--..--', '.':'.-.-.-',
	'?':'..--..', '/':'-..-.', '-':'-....-',
	'(':'-.--.', ')':'-.--.-'}


	user_string = input("Enter the string to be converted to Morse code: ")



	for char in user_string:
		ch = ch.upper()

	for character in user_string:
		print(CODE[character])

# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	# run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()