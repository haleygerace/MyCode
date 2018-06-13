# Haley Kline Hw 3

# 5.5 Property Tax
def property_tax():

	# Variable Declaration
	property_tax = 0.0
	assessed_value = 0.0
	actual_value = 0.0
	# Enter the actual value
	actual_value = float(input("Enter the actual value: "))
	# Calculate assessed value
	assessed_value = actual_value * .6
	# Calculate tax
	property_tax = assessed_value * .0072
	print("Assessed value: " + "$" + format(assessed_value, ".2f"))
	print("Property Tax: " + "$" + format(property_tax, ".2f"))

# 5.9 Future Value
def future_value():

	# Variable Declaration
	present_value = 0.0
	months = 0.0
	monthly_interest_rate = 0.0
	future_value = 0.0
	# Enter present value
	present_value = float(input("Enter the present value of the account in dollars: "))
	# Enter monthly interest rate
	monthly_interest_rate = float(input("Enter the monthly interest rate as a percentage: "))
	# Enter the number of months
	months = float(input("Enter the number of months: "))
	# Calculate ammount in account
	future_value = present_value * ((1 + monthly_interest_rate/100) ** months)
	print("The information for your account is: ")
	print("Present Value: " + "$" + format(present_value, ".2f"))
	print("Interest Rate: " + format(monthly_interest_rate, ".2f") + "%")
	print("After 12 months, the value in your account will be " + "$" + format(future_value, ".2f"))
	
# 7.8 Generation Z Search
def genz_search():
	# Variable Declaration
	boyname = 0.0
	girlname = 0.0

	# Enter boy and girl names
	boyname = str(input("Enter a boy's name, or N if you do not wish to enter a boy's name: "))
	girlname = str(input("Enter a girl's name, or N if you do not wish to enter a girl's name: "))
	
	# Open file
	myfile = open('BoyNames.txt', 'r')
	boynamesR = myfile.readlines()
	myfile1 = open('GirlNames.txt', 'r')
	girlnamesR = myfile.readlines()

	# Are the names popular
	if boyname in boynamesR:
		print(str(boyname) + " is one of the most popular boy's names.") 
	elif boyname == "N":
		print("You chose not to enter a boy's name.")
	else:
		print(str(boyname) + " is not one of the most popular boy's names.")
	if girlname in girlnamesR:
		print(str(girlname) + " is one of the most popular girl's names.")
	elif girlname == "N":
		print("You chose not to list a girl's name.")
	else:
		print(str(girlname) + " is not one of the most popular girl's names.")

# 7.12 Prime Number Generation 
def prime_gen():
	user_integer = input("Enter an integer greater than 1: ")

	for i in range(2, int(user_integer) + 1):
		num = 0
		for j in range (2, i):
			if (i % j == 0):
				num = 1
		if (num == 0):
			print(i, " is prime.")
		elif (num == 1):
			print(i, " is composite.")


# 9.10 Jean Tirole Nobel Index

# 12.7 Recursive Power Method
def pow_recursive(x,y):
	if y == 0:
		return 1
	elif y % 2 == 0:
		c = pow(x, y/2)
		return c * c
	else: 
		return x * pow(x, y-1)

