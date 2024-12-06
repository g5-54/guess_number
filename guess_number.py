from random import randint

number = randint(1, 100)
print(number)
print('Guess a number from 1 to 100')

while True:
    guess = int(input('Enter the numbe '))

    if guess < number:
        print('Your number is lower than needed')

    if guess > number:
        print('Your number is higher than needed')

    if guess == number:
        break

print('Correct')