# print("Please select an option")
# print("1. Have a coffee\n2. Have a donut\n3. Have a pastry\n4. Have some scrambled eggs\n0. exit")
# coffee = 1
# donut = 2
# pastry = 3
# scramble = 4
# choice = int(input())
#
# for choice in range(0, 5):
#     if choice == 1:
#         print("{} is a perfect choice to start the day".format(1))
#         break
#     elif choice == 2:
#         print("Our {} are tasty, just stay away form any more sugar for the day".format(2))
#         break
#     elif choice == 3:
#         print("Mind you, our {} are a mouthful".format(3))
#         break
#     elif choice == 4:
#         print("Nice, with our {} you'll start with a punch today".format(4))
#         break
#     elif choice == 0:
#         print("Have a nice day!")
#         break
#     continue

choice = "-"
while True:
    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    choice = input()