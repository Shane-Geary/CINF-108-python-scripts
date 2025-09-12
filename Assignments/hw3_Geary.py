# Shane T Geary
# CINF: 108
# 09/11/2025
# University at Albany

import hw3_util

legoPieces = ['1x1, 6\n', '2x1, 2\n', '2x2, 2\n', '2x4, 1']

def createFile(filename):
	try:
		legosFile = open(filename, 'x')
		for lego in legoPieces:
			legosFile.write(lego)

		legosFile.close()
	except:
		print(f'The file, "{filename}" already exists')

createFile('legos.txt')

legos = hw3_util.read_legos('legos.txt')
print(legos)

legoRequest = input('What type of lego do you need?\n')
legoQuantity = int(input('How many pieces of this Lego do you need?\n'))

noMatch = False

def legoPieceArea(piece):
	sideX = int(piece.split('x')[0])
	sideY = int(piece.split('x')[1])
	
	return sideX * sideY

def checkLegoPieces():
	legoTypes = []
	for item in legos:
		item = item.strip("\n")
		legoInfo = item.split(",")
		types = legoInfo[0].strip()		
		legoTypes.append(types)

	legoTypes.reverse()
	legoTypes = list(dict.fromkeys(legoTypes))

	legoRequestArea = legoPieceArea(legoRequest)
	totalAreaNeeded = legoQuantity * legoRequestArea

	if (legos.count(legoRequest) == legoQuantity):
		print(f'I have {legos.count(legoRequest)} pieces of {legoRequest} for this')
	elif (legos.count(legoRequest) > legoQuantity):
		print(f'I have {legoQuantity} pieces of {legoRequest} for this')
	else:
		for lego in legoTypes:
			legoArea = legoPieceArea(lego)
			if (legoArea < legoRequestArea) and (legoRequestArea % legoArea == 0):
				piecesNeeded = totalAreaNeeded / legoArea
				if (piecesNeeded <= legos.count(lego)):
					print(f'I have {int(piecesNeeded)} pieces of {lego} for this')
					return
			else:
				noMatch = True
		print("I don't have enough pieces of this Lego")

	# Refactor of the above logic
	# for lego in legoTypes:
	# 	legoArea = legoPieceArea(lego)
	# 	totalAreaAvailable = legos.count(lego) * legoArea
	# 	# print(f'Area needed: {totalAreaNeeded}\n Area available: {totalAreaAvailable}')

	# 	piecesNeeded = totalAreaNeeded / legoArea
	# 	if (totalAreaNeeded == totalAreaAvailable) and (legoArea <= legoRequestArea):
	# 		print(f'I have {int(piecesNeeded)} pieces of {lego} for this')
	# 		noMatch = False
	# 		return
	# 	elif (legoRequest == lego) and (legoQuantity <= legos.count(lego)):
	# 		print(f'I have {int(legoQuantity)} pieces of {lego} for this')
	# 		noMatch = False
	# 		return
	# 	else:
	# 		noMatch = True
	
	# if noMatch:
	# 	print("I don't have enough pieces of this Lego")

checkLegoPieces()