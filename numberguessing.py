import random

top_of_range = input('Type a number:')


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ( 'Please type a number larger than 0 next time.')
        quit()
else:
                    print('Please type a number next time')
                    quit()

random_number = random.randint(0, 20)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ") # get the user to provide their guess
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess ==random_number:
            print ('You got it right')
            break # This will exit the loop when the guess is correct
        else:
            print('You got it wrong!')
    
        print('Please type a number next time.')
        continue
    break
    if user_guess == random_number:
        print('You got it right')
    else:
            print("You got it wrong!")
else:
            print('Please type a number next time')
print ('You got it in', guesses, 'guesses')
            
    
