while(1):
    inp=int(input('Enter your age'))
    if inp < 3:
        print('free')
    elif inp > 3 and inp < 12:
        print('10$')
    else:
        print('15$')