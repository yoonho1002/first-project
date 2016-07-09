import random

number = random.randint(1, 20)

guesstime = 0

print('Hi! What is your name?')
myname = input()
print('Yo, ' + myname + ' I am thinking of a number between 1 and 20.')

while guesstime < 6:
	print('Guess it')
	guessnumber = input()
	guessnumber = int(guessnumber)

	guesstime + 1

	if guessnumber < number:
		print('Your gusss is too low.')

	if guessnumber > number:
		print('your guess is too high.')

	if guessnumber == number:
		break

if guessnumber == number:
	guesstime = str(guesstime)
	print('Wow, ' + myname + 'You guessed my number in' + guesstime + ' times!')

if guessnumber != number:
	number = str(number)
	print('Nope, The number was '+ number)	