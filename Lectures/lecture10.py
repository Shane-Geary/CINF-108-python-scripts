colors = ['red', 'blue', 'green', 'purple']

primes = [2, 3, 7, 11, 13, 17]

nums = list(range(1, 33, 3))

my_friends = ['Joe', 'Mary', 'Mike']
your_friends = ['Jane', 'Bobby']

my_friends += your_friends

print(my_friends)

def printLoops():
	for count in range(len(colors)):
		print(colors[count])

printLoops()