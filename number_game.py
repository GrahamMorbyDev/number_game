import random


def start_game():
    winner = False
    user_name = input('Welcome to the number guessing game! What is your name?   ')
    solution = random.randint(0, 100)

    while not winner:
        user_guess = input("We have stored a random number between 0 and 100! What could it be?   ")
        try:
            user_guess = int(user_guess)
            if user_guess > 100 or user_guess < 0:
                raise ValueError('It can only be as high as 100 or as low as 0 {}, please try again'.format(user_name))
        except ValueError as err:
            print("Sorry that's not quite right! Please use a number between 1 and 100")
        else:
            if int(user_guess) < solution:
                print("That's sadly the wrong answer {}, maybe try a little higher".format(user_name))
            elif int(user_guess) > solution:
                print("That's sadly the wrong answer {}, maybe try a little lower".format(user_name))
            else:
                winner = True

    print('Yay! You have found the secret code {}! Welcome to the cool side'.format(user_name))
    print('Thank you for playing my game...')


start_game()
