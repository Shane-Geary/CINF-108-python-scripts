# Shane T Geary
# CINF: 108
# 09/24/2025
# University at Albany

# Create file variable and open Alice (Alice.txt) in Wonderland 
aliceInWonderland = open('Alice.txt', 'r')

# Create file variable and open WordCount.txt for writing
wordcount = open("AliceWordCount.txt", 'w')

# Read contents of Alice.txt into a string variable
aliceIWString = aliceInWonderland.read()
 
# Create a list from the string variable and covert all text to lower-case
aliceIWList = aliceIWString.lower().split()

# Create a dictionary variable -- note your dictionary will have 'words' as    #  keys and an integer as a value (which will be the number of words seen in #  the file)

aliceIWWordCount = {}

# loop through each word in your list and
#   1) if it is not in the dictionary, add it with the key pair = 1
#   2) if already in the dictionary, increment key pair by 1

for word in aliceIWList:
	if word not in aliceIWWordCount:
		aliceIWWordCount[word] = 1
	else:
		aliceIWWordCount[word] += 1
		
print(aliceIWWordCount['about'])

# Now, Loop through each word and write it to your output file in the format #  specified Note that your dictionary contains some non alphabetic 'words
#  before writing to the file, check first if it is a legitimate word.  
#  Hint: use isalpha()

# Create columns for the output file's format
columns = [
	'Word\t\t\t\t',
	'Count\n',
	'\t\t\t\t\t|\n',
	'-------------------- -----\n'
]

# Write columns to the output file
for column in columns:
	wordcount.write(column)

# Initialize empty rows list before looping through dictionary
rows = []
for key, value in aliceIWWordCount.items():
	if str(key).isalpha():
		rows.append(
			f'{key:<20}'
			f' {value}\n'
		)

# Sort alphabetically before writing rows to output file
rows.sort()
for row in rows:
	wordcount.write(row)

# Close both the input and output files
aliceInWonderland.close()
wordcount.close()