# Function to print hello in a box

def main():
	print('I would really like to welcome you!')
	for count in range(5):
		print_hello()
	print('Have a nice day!')

def print_hello():
	print('**********')
	print('* HELLO! *')
	print('**********')

main()