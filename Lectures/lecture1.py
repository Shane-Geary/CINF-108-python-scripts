# for minutes in range(60):
# 	for seconds in range(60):
# 		print(f'{minutes}:{seconds}')

# Program that will print rectangle using '*' based on input dimensions

rows = int(input('Please enter number of rows for rectangle: '))
cols = int(input('Please enter the number of cols for the rectangle: '))

for r in range(rows):
	for c in range(cols):
		print('*', end='')
	print('\n')
