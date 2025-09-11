# def draw_box(width, height):
# 	for w in range(width):
# 		for h in range(height):
# 			print('*', end='')
# 		print('\n')

# draw_box(10, 5)

# Name formatter program

def main():
	first = input('What is your first name? \n')
	last = input('What is your last name? \n')
	format_name(first, last)

def format_name(fname, lname):
	print(f'\n{fname}, {lname}')

main()