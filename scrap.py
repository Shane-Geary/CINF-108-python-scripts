
# for num in range (1, 11):
# 	print (f"{num}\t{num * num}")

# Degrees conversions—Celcius to Farenheight in X steps of temperature
# print('Celcius\tfarenheight')
# print('---------------------')

# limit = int(input('Please enter the upper limit'))
# step = int(input('Please enter the step size'))

# for degrees in range(0, limit + 1, step):
# 	fah = degrees * (9.0 / 5.0) + 32
# 	print(f"{degrees}\t{fah}")

# Banck account deposit

balance = 0.0

maximum = int (input ('How many deposits would you like to make? '))

for count in range(1, maximum + 1):
	deposit = float(input(f'Please enter the amount for deposit #{count}: '))
	balance = balance + deposit

print(f'Your total balance on the account is ${balance:.2f}')

