import random

a = random.randint(1,30)

inp = int(input('guess the number'))

if inp < a:
    print('your number is smaller')

else:
    print('your number is greater')