print('Please think of a number between 1 and 100.')

low = 1
high = 100
state = True

while state:
    medium = (low + high) // 2
    print('Is your secret number ' + str(medium) + '?')
    guess = input("Enter 'l' if the guess is too low, 'h' if it's too high, or 'c' if it's correct: ")

    if guess == 'c':
        print('great. Your secret number was ' + str(medium) + '.')
        state = False
    elif guess == 'l':
        high = medium - 1
    elif guess == 'h':
        low = medium + 1
    else:
        print('Sorry, I did not understand your input. Please try again.')
