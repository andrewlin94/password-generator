import random, sys, re

def generate_char_set(upper_case, lower_case, numbers, symbols):
	set = []
	if upper_case:
		for i in range(26):
			set.append(chr(65+i))
	if lower_case:
		for i in range(26):
			set.append(chr(97+i))
	if numbers:
		for i in range(10):
			set.append(chr(48+i))
	if symbols:
		for i in range(15):
			set.append(chr(33+i))
	return set

def generate_password(length, set):
	password = ''
	for i in range(length):
		random.seed(random.randrange(sys.maxsize))
		random.shuffle(set)
		password += set[random.randrange(len(set))-1]
	return password
def validate_regex(ans):
	yes_regex = 'y'
	no_regex = 'n'
	if not(re.search(yes_regex, ans, re.IGNORECASE) != None or re.search(no_regex, ans, re.IGNORECASE) != None):
		return False
	return True

def interpret_answer(ans):
	yes_regex = 'y'
	no_regex = 'n'
	if re.search(yes_regex, ans, re.IGNORECASE) != None:
		return True
	if re.search(no_regex, ans, re.IGNORECASE) != None:
		return False

if __name__ == '__main__':
	try:
		# Length check
		try:
			length = int(input('Type the length of the password: '))
		except Exception:
			raise Exception('Please enter a number.')
		# Upper case check
		upper_case = input('Use upper case? Y/N: ')
		if not validate_regex(upper_case):
			raise Exception('Please enter a valid input.')
		upper_case = interpret_answer(upper_case)
		# Lower case check
		lower_case = input('Use lower case? Y/N: ')
		if not validate_regex(lower_case):
			raise Exception('Please enter a valid input.')
		lower_case =  interpret_answer(lower_case)
		# Numbers check
		numbers = input('Use numbers? Y/N: ')
		if not validate_regex(numbers):
			raise Exception('Please enter a valid input.')
		numbers =  interpret_answer(numbers)
		# Symbols check
		symbols = input('Use symbols? Y/N: ')
		if not validate_regex(symbols):
			raise Exception('Please enter a valid input.')
		symbols = interpret_answer(symbols)	
		# Get the set of characters
		set = generate_char_set(upper_case, lower_case, numbers, symbols)
		print('Running Password generator')
		# Generate password
		print('Your password is: ' +  generate_password(length, set))
	except Exception as e:
		print('')
		print(e)
		sys.exit(1)
	sys.exit(0)