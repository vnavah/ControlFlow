name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#    print("Great, " + str(age) + " is enough to vote!!!")
#    print("Please put an X in the box")
# else:
#    print("Please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age >= 125:
    print("Sorry Yoda, you died in Return of the Jedi")
else:
    print("Great, " + str(age) + " is enough to vote!!!")
    print("Please put an X in the box")
