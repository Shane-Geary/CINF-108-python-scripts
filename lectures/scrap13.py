# Tuples and String Manipulation
## Tuples are just lists/arrays that cannot be changed/mutated

# primes = (2, 3, 5, 7, 11, 13, 17)

# print(primes[3:])

# state = "Colorado"

# for l in state:
# 	print(l.capitalize())

# count = 0
# for o in state:
# 	if o == 'o':
# 		count += 1
# 	print(count)


# username = 'gearz1994'

# id_num = username[-3:]

# print(id_num)

# phrase = '	I am a remote student at UAlbany		'
# phrase = phrase.strip()

# print('UAlbany' in phrase)
# print(phrase.replace('UAlbany', 'MIT'))

# combo = '12345'
# print(combo.isdigit())

phone = '555-687-5309'
phoneList = phone.split('-')

print(phoneList)
