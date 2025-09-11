# 
import random

numList = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

randfile = open('random_ints.txt', 'w')

for num in numList:
	randfile.write(str(num) + '\n')

randfile.close()