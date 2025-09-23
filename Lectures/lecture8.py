# Read in and print a list of animals

def main():
	print('Welcome to the animal sanctuary!')
	print('The following animals are in this sanctuary: ')

	zoofile = open('animals.txt')

	for animal in zoofile:
		animal = animal.rstrip('\n')
		print(animal)

	zoofile.close()

if __name__ == '__main__':
	main()