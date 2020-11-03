# import random
# chars = 'abcdefghijklmsopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+?><'

# length = input('password length-')
# length= int(length)
# password = ''
# for c in range(length):
# 	password += random.choice(chars)
# print(password)


import random
chars = 'abcdefghijklmsopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #~!@#$%^&*()_+?><
number = int(input('number of password-'))
length = int(input('password length-'))
for pass_num in range(number):
	password = ''
	for pass_len in range(length):
		password += random.choice(chars)
	print(password)

