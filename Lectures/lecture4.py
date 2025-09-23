import random
# Simulate coin flips
num_heads = 0
num_tails = 0

flips = int(input('How many coin flips? \n'))

for num in range(flips):
	coin = random.randint(1, 2)
	if coin == 1:
		# print('HEADS')
		num_heads = num_heads + 1
	else: 
		# print('TAILS')
		num_tails = num_tails + 1
	
print(f'Total Heads: {num_heads}')
print(f'Total Tails: {num_tails}')
