def stringOperator(*args):
	wordList = list()
	for word in args:
		wordList.append(word) # Create a list from the post words

	wordList.sort() # Alphabetize in ascending order
	print(wordList)

	print(max(wordList)) # Find longest/largest word in the list

stringOperator('Sapphire', 'Ruby', 'Painite', 'Diamond', 'Quartz')