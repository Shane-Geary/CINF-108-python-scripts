# Sets in Python

animals = set(['cat', 'dog', 'mouse'])

vowels = set('aeiou')

s1 = set([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 46, 44, 40, 38])

s2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

friends = set(['Bob', 'Mary', 'Sally'])

classRoster = set(['Alice', 'Bob', 'Chris', 'Mary', 'Sally', 'Robert'])

def handleSet():
	animals.update(['goose', 'lion', 'turtle'])
	
	for letter in vowels:
		print(letter)

	print(animals)
	# print(len(vowels))

# letter = input('Please enter a letter of the alphabet: ')
# letter = letter.lower()

def vowelChecker():
	if letter in vowels:
		print(f'{letter} is a vowel')
	else:
		print(f'{letter} is a constant')

def setOperations():
	# print(s1.union(s2)) # union can also be written as 's1 | s2'
	print(s1.intersection(s2)) # intersection can also be written as 's1 & s2'
	print(s1.difference(s2)) # difference can also be written as 's1 - s2'
	print(s1.symmetric_difference(s2)) # symmetric_difference can also be written as 's1 ^ s2'

def subSupersetOperations():
	print(friends.issubset(classRoster)) # Also written as 'friends <= classRoster'
	print(classRoster.issuperset(friends)) # Also witten as 'classRoster >= friends'

# handleSet()
# vowelChecker()
# setOperations()
subSupersetOperations()