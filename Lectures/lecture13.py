# Program will read in a file of students and their grades for a course
# Print each student's name: First, Last, then their final average

studentfile = open('students.csv', 'r')

for line in studentfile:
	studentrecord = line.split(',')
	studentrecord[-1] = studentrecord[-1].rstrip('\n')
	grades = studentrecord[-4:]
	average = int(grades[0]) + int(grades[1]) + int(grades[2]) + int(grades[3])
	average = average / 4.0

	print(studentrecord[1], studentrecord[0], f'{average:.2f}')

studentfile.close()