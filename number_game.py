import random



def start_game():
    winner = False
    print('Welcome to my number guessing game!')
    user_name = input('Can you tell me your name?   ')
    solution = random.randint(0, 100)
    guesses = 0

    while not winner:
        
        user_guess = input(
            "Please tell me your answer, remember it must be between 0 - 100!    ")
        try:
            user_guess = int(user_guess)
            if user_guess > 100 or user_guess < 0:
                raise ValueError('It can only be as high as 100 or as low as 0 {}, please try again'.format(user_name))
        except ValueError as err:
            print("Remember {} you can only enter a number between 1 - 100".format(user_name))
            print("({})".format(err))
        else:
            if int(user_guess) < solution:
                print("That's sadly the wrong answer {}, maybe try a little higher".format(
                    user_name))
                guesses += 1
                print('You have had {} guesses! Please try again'.format(guesses))
            elif int(user_guess) > solution:
                print(
                    "That's sadly the wrong answer {}, maybe try a little lower".format(user_name))
                guesses += 1
                print('You have had {} guesses! Please try again'.format(guesses))
            else:
                winner = True
                print('Yay! You have found the secret code {} in {} tries! Welcome to the cool side'.format(user_name, guesses))
                user_replay =  input('Thank you for playing my game! Would you like to play again? Y/N   ')
                
                if user_replay.lower() == 'y':
                    winner = False
                    solution = random.randint(0, 100)
                    print('The current high score is {}! Maybe you can beat that this time...'.format(guesses))
                    guesses = 0
                else: 
                   print('Closing game... See you again soon!') 

start_game()
