import random

highest = 1000
answer = random. randint(0, highest)
guess = 0   # initialise to any number different from answer
# print(answer)       #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Have a nice day.")
        break

    if guess == answer:
        print("Congratulations! You guessed the right number.")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else:   # guess must be greater than answer
            print("Please guess lower.")


        # guess = int(input())
        # if guess == answer:
        #     print("Congratulations! You guessed the right number.")
        # else:
        #     print("Sorry, you have not guessed correctly.")

