zoo = ['cat', 'dog', 'bird', 'snake', 'zebra']

# animal = input("Which animal are you looking for? ")
# animal.index

# if animal in zoo:
# 	print(f'{animal} is indeed in our zoo!')
# else:
# 	print(f'Sorry, but we do not have a {animal} in our zoo.')

def petLoop():
	petfile = open('pets.txt', 'w')

	for pet in zoo:
		petfile.writelines(pet + '\n')
	
	petfile.close()

petLoop()