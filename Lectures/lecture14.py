# Dictionaries

emails = {'Shane': 'shane123@email.com', 'Ron': 'Ronald321@email.com', 'Larry': 'lar23@email.com'}

name = input('Please enter a name: ')

def checkEmail():
	print(emails)
	if name in emails:
		print('email is: ', emails[name])
	else:
		print(f'{name} does not have an email address on file')

checkEmail()