numbers = [1, 45, 31, 24, 80]
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are acceptable")