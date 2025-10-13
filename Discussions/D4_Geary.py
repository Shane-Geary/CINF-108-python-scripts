ye_set = set([10, 45, 18, 26, 16, 44, 34, 6, 31, 28, 50, 19, 46, 29, 32, 33, 4, 42, 21, 9])

geary_set = set([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 46, 44, 40, 38])

def setOperations():
	setIntersection = geary_set & ye_set # Find intersection between two sets
	setUnion = geary_set | ye_set # Find union between two sets
	setSymmetricDifference = geary_set ^ ye_set # Find symmetric difference of the two sets

	print(
		f'The intersection contains {len(setIntersection)} elements: {setIntersection}\n'
		f'The union contains {len(setUnion)} elements: {setUnion}\n'
		f'The symmetric difference contains {len(setSymmetricDifference)} elements: {setSymmetricDifference}\n'
	)

setOperations()