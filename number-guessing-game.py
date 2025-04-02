import random
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
number_to_guess  = random.randrange(100)
chances = 7
guess_counter = 0
while guess_counter < chances:
    guess_counter+=1
    guess = int(input("Enter your guess: "))
    if guess == number_to_guess:
        print("Congratulations! You have guessed the number in " + str(guess_counter) + " attempts")
        break
    elif guess < number_to_guess:
        print('your guss is too low')
    elif guess >number_to_guess:
        print('your guss is too high')
    elif guess_counter>=chances and guess!=number_to_guess:
        print("Sorry! You have used all the chances. The number was " + str(number_to_guess))
        