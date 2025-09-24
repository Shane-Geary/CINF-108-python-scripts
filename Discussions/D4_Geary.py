geary_set = set([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 46, 44, 40, 38])

example_set = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

def setOperations():
	setIntersection = geary_set & example_set # Find intersection between two sets
	setUnion = geary_set | example_set # Find union between two sets
	setSymmetricDifference = geary_set ^ example_set # Find symmetric difference of the two sets

	print(
		f'The intersection contains {len(setIntersection)} elements: {setIntersection}\n'
		f'The union contains {len(setUnion)} elements: {setUnion}\n'
		f'The symmetric difference contains {len(setSymmetricDifference)} elements: {setSymmetricDifference}\n'
	)

setOperations()