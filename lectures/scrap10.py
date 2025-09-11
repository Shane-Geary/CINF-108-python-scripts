def main():
	zoofile = open('favorite_animals.txt', 'w')

	done = False # Flag to exit loop

	print('We are going to ask you for your favorite animals')
	print('Type "done" when done entering animals')
	try:
		while not done:
			new_animal = input("Please enter an animal name: ")
		if new_animal == 'done':
			done = True
		else:
			zoofile.write(new_animal + '\n')
	
		zoofile.close()
	except IOError:
		print(f'An error occurred when attempting to open the file {zoofile}')

if __name__ == '__main__':
	main()