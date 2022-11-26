# if guess == answer:
#     print("You got it first time")
# elif guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed right")
#     else:
#         print("Sorry, you have not guessed the answer")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed right")
#     else:
#         print("Sorry, you have not guessed the answer")
#
import random

highest = 10
answer = random.randint(1, highest)
print(answer)       #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("Nice! You got it first time.")
else:
    if guess < answer:
        print("Please guess higher.")
    else:   # guess must be greater than answer
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Congratulations! You guessed the right number.")
    else:
        print("Sorry, you have not guessed correctly.")

