import random

random_num = random.randint(1,100)
guess = 0

while True:
    guess_num = int(input("Guess a any number between 1 to 100: "))

    if guess_num == random_num:
        print("Congrats you got it right")
        print("Number of guesses",guess)
        exit()

    elif guess_num > random_num:
        print("The num is too big try again")
        guess = guess + 1

    else:
        print("Number is too small try again")
        guess = guess + 1





