firstName = input("Your First Name: ")
lastName = input("Your Last Name: ")
age = int(input("Your Age: "))
birthYear = input("Your Year Birth: ")
list = [firstName, lastName, age, birthYear]

print("User Information")
for l in list:
    print("- ", l)

if age < 0:
    print("Invalid login !")
elif age < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")