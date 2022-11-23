name = input("Please tell us your name: ")
age = int(input("Now your age "))

if 18 <= age < 31:
    print("Welcome aboard {0}".format(name))
else:
    print("Sorry you can´t come on board")