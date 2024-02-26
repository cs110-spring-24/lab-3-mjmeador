import random
death_trials = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Choose your destiny:")
for death_trial in death_trials:
    print(f"Death_trial {death_trial}")

bigdecision = int(input("Wanna play a game?: "))

#problem 1
if bigdecision == 1:
    for i in range(1, 1001):
        print(i)
#problem 2
elif bigdecision == 2:
    for i in range(1, 1001):
        if i % 2 != 0:
            print(i)
#problem 3
elif bigdecision == 3:
    for i in range(0, 1001):
        if i % 3 == 0:
            print(i)

#problem 4 ez pz
elif bigdecision == 4:
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
#problemo 5
elif bigdecision == 5:
    fart = int(input("Enter a number greater than 200: "))
    while fart <= 200:
        fart = int(input("PLEASE PLEASE PLEASE enter a number greater than 200: "))
    for i in range(1, fart + 1):
        if i % 11 == 0 or i % 13 == 0:
            print(i)
#problem 6
elif bigdecision == 6:
    string_input = input("Enter a stringy: ")
    for letter in string_input:
        print(letter)
elif bigdecision == 7:
    string_input = input("Enter a stringy: ")
    if len(string_input) <= 10:
        print("String must be more than 10 letters long DOOFUS.")
    else:
        for i in range(1, len(string_input), 2):
            print(string_input[i])


# Problem 8

elif bigdecision == 8:
    dice_rolls = [random.randint(1, 6) for _ in range(1000)]
    for i in range(1, 7):
       print(f"{i} was rolled {dice_rolls.count(i)} times wow")

# Problem 9 this one sucked ASS
elif bigdecision == 9:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    number = int(input("Enter a PRIME number: "))
    if is_prime(number):
          print(f"{number} Primey yipee.")
    else:
          print(f"{number} No prime. You get slimed.")

# Problem 10

elif bigdecision == 10:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, 1000):
        if is_prime(i):
            print(i)


