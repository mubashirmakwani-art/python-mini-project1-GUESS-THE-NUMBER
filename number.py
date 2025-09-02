import random

print("Welcome dear user!")

top_of_range = input("Enter the range(ex:10): ")
if not top_of_range.isdigit() or int(top_of_range) <= 0:
    print("Please enter a number!")
    quit()

top_of_range = int(top_of_range)

chances = input("Enter how many chances you want: ")
if not chances.isdigit() or int(chances) <= 0:
    print("Enter number of chances!")
    quit()

chances = int(chances)

random_number = random.randint(1, top_of_range)

for attempt in range(1, chances + 1):
    user_guess = input(f"Chance {attempt}/{chances}: Make a guess: ")

    if not user_guess.isdigit():
        print("Enter a number !")
        continue

    user_guess = int(user_guess)

    if user_guess == random_number:
        print(" You got it! You win!")
        break
    elif user_guess > random_number:
        print(" Your guess is above the number.")
    else:
        print("Your guess is below the number.")

    if attempt == chances:
        print(f"\n U lost! Hahahahaha!!!! The number was {random_number}.")
